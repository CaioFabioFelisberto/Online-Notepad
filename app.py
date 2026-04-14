from pymongo import MongoClient
from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
import markdown
from flask import session

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')


def get_collection():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv('DB_NAME')]
    return db[os.getenv('COLLECTION_NAME')]


def get_users_collection():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv('DB_NAME')]
    return db[os.getenv('USER_COLLECTION_NAME')]


def get_note(query):
    collection = get_collection()
    note = collection.find_one(query)
    return note['content'] if note else ''


def check_password(stored_password, provided_password):
    return stored_password == provided_password


@app.route('/notepad/<note_name>', methods=['GET', 'POST'])
def notepad(note_name):

    if 'user_id' not in session:
        return redirect(url_for('login'))

    note_from_database = get_note(
        {'name': note_name, 'user_id': session['user_id']})
    if request.method == 'POST':
        button = request.form.get('action')
        if button == 'save':
            now = datetime.now(timezone.utc)
            new_note = request.form['note_text']

            collection = get_collection()
            collection.update_one(
                {'name': note_name, 'user_id': session['user_id']},
                {'$set': {'content': new_note, 'updated_at': now}},
                upsert=True
            )

            return redirect(url_for('notepad', note_name=note_name))
        elif button == 'delete':
            collection = get_collection()
            collection.delete_one(
                {'name': note_name, 'user_id': session['user_id']})

            return redirect(url_for('select_note'))
        elif button == 'go_back':
            return redirect(url_for('select_note'))

    html_translated_text = markdown.markdown(note_from_database)

    return render_template('index.html', content=note_from_database, html_content=html_translated_text, title=note_name)


@app.route('/', methods=['GET', 'POST'])
def select_note():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        button = request.form.get('action')
        if button == 'get_note':
            note_to_get = request.form.get('note_name')
            collection = get_collection()
            if collection.find_one({'name': note_to_get, 'user_id': session['user_id']}):
                return redirect(url_for('notepad', note_name=note_to_get))
            else:
                return render_template('get_note.html', error='Note not found')
        elif button == 'create_note':
            now = datetime.now(timezone.utc)
            note_to_create = request.form.get('new_note_name')
            collection = get_collection()
            if collection.find_one({'name': note_to_create, 'user_id': session['user_id']}):
                return render_template('get_note.html', error='Note already exists')
            else:
                collection.insert_one({'name': note_to_create, 'content': 'Hey! This is your new note. Start writing here...',
                                      'created_at': now, 'updated_at': now, 'user_id': session['user_id']})
                return redirect(url_for('notepad', note_name=note_to_create))
        elif button == 'delete_note':
            note_to_delete = request.form.get('note_name')
            collection = get_collection()
            collection.delete_one(
                {'name': note_to_delete, 'user_id': session['user_id']})
            return redirect(url_for('select_note'))
        elif button == 'logout':
            session.clear()
            return redirect(url_for('login'))
    all_notes = list(get_collection().find(
        {'user_id': session['user_id']}).sort('updated_at', -1))
    return render_template('get_note.html', all_notes=all_notes)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users_collection = get_users_collection()
        if users_collection.find_one({'username': username}):
            return render_template('signup.html', error='Username already exists')
        else:
            users_collection.insert_one(
                {'username': username, 'password': password})
            return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = get_users_collection().find_one({'username': username})

        if user and check_password(user['password'], password):
            session['user_id'] = str(user['_id'])
            return redirect(url_for('select_note'))
        else:
            return render_template('login.html', error='Username or password is incorrect')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
