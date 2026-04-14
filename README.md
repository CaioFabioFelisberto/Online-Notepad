# 📒 Online Notepad (Full-Stack Python)

A dynamic web-based notepad application that allows users to Create, Read, Update, and Delete (CRUD) personal notes. This project features **Markdown** support for rich text editing and **NoSQL** database persistence using MongoDB.

## 🚀 Features

- **Note Management:** Easy note selection via dropdown menu, new note creation, and quick deletion.
- **Rich Text Editing:** Automatic Markdown-to-HTML rendering for professional-looking notes.
- **User Authentication:** Secure login and signup system using **password hashing** (Werkzeug).
- **Metadata Tracking:** Notes are automatically sorted by the most recent update.
- **Responsive UI:** Clean and intuitive interface built with Jinja2 templates and custom CSS.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Web Framework:** [Flask](https://flask.palletsprojects.com/)
- **Database:** [MongoDB](https://www.mongodb.com/) (via PyMongo)
- **Security:** Werkzeug Security (PBKDF2 Hashing)
- **Formatting:** Markdown library for Python
- **Frontend:** HTML5, CSS3, and Jinja2

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/online-notepad-python.git](https://github.com/your-username/online-notepad-python.git)
   cd online-notepad-python

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
3. **Install dependencies:**
   ```bash
   pip install flask pymongo python-dotenv markdown
4. **Environment Variables:**
   Create a .env file in the root directory and add your credentials:
   ```bash
   MONGO_URI=mongodb://localhost:27017/
   DB_NAME=notepad_db
   COLLECTION_NAME=notes
   SECRET_KEY=your_random_secret_key_here
5. **Run the application:**
   ```bash
   python app.py
