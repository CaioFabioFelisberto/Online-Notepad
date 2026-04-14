📒 Online Notepad (Full-Stack Python)
A dynamic web-based notepad application that allows users to Create, Read, Update, and Delete (CRUD) personal notes, featuring Markdown support and NoSQL database persistence.

🚀 Features
Note Management: Dropdown selection, new note creation, and deletion.

Rich Text: Automatic Markdown to HTML rendering.

User Sessions: Secure login system with password hashing.

Database: Integrated with MongoDB for scalable storage.

Responsive UI: Clean design focused on user experience (UX).

🛠️ Tech Stack
Language: Python 3.x

Web Framework: Flask

Database: MongoDB (via PyMongo)

Security: Werkzeug Security (Password Hashing)

Frontend: Jinja2 Templates, HTML5, CSS3

⚙️ Getting Started
Clone the repository:

Bash
git clone https://github.com/your-username/your-repository.git
Setup virtual environment and install dependencies:

Bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install flask pymongo python-dotenv markdown
Configure Environment Variables:
Create a .env file in the root directory:

Snippet de código
MONGO_URI=mongodb://localhost:27017/
DB_NAME=your_db_name
COLLECTION_NAME=your_notes_collection
SECRET_KEY=your_secure_secret_key
Run the application:

Bash
python app.py
