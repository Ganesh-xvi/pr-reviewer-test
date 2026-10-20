import hashlib
import json
import subprocess


def get_user(db, user_id):
    return db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchall()


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)


def load_session(data):
    return json.loads(data)


def list_folder(folder):
    return subprocess.run(["ls", folder], capture_output=True, check=True)
