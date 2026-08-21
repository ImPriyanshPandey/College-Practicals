from flask import Flask
import mysql.connector, os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'db'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'rootpass'),
            database=os.getenv('DB_NAME', 'testdb')
        )
        return "<h1>Connected to MySQL!</h1>"
    except Exception as e:
        return f"<h1>App Running - DB error: {e}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
