from flask import Flask
import os
import pymysql

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = pymysql.connect(
            host=os.environ['MYSQL_ADDON_HOST'],
            port=int(os.environ['MYSQL_ADDON_PORT']),
            user=os.environ['MYSQL_ADDON_USER'],
            password=os.environ['MYSQL_ADDON_PASSWORD'],
            database=os.environ['MYSQL_ADDON_DB']
        )
        return "✅ Connexion MySQL réussie"
    except Exception as e:
        return f"❌ Erreur MySQL : {e}"

if __name__ == "__main__":
    app.run()
