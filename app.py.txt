from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRESQL_ADDON_DB"),
            user=os.getenv("POSTGRESQL_ADDON_USER"),
            password=os.getenv("POSTGRESQL_ADDON_PASSWORD"),
            host=os.getenv("POSTGRESQL_ADDON_HOST"),
            port=os.getenv("POSTGRESQL_ADDON_PORT")
        )
        return "Connexion à PostgreSQL réussie !"
    except Exception as e:
        return f"Erreur : {e}"

if __name__ == "__main__":
    app.run()
