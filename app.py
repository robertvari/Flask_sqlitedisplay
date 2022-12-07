from flask import Flask, render_template
import sqlite3, os

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(__file__)
DATABASE = os.path.join(PROJECT_ROOT, "db.sqlite3")

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM GEPEK_SQLITE').fetchall()
    conn.close()

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)