import hashlib
import pickle
import subprocess


def get_user(db, user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return db.execute(query).fetchall()


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def load_session(data):
    return pickle.loads(data)


def list_folder(folder):
    return subprocess.run("ls " + folder, shell=True, capture_output=True)


API_KEY = "sk_live_51H8abcDEF123xyz"
