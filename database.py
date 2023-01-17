import sqlite3


def create_db():
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    # Tabelle user erstellen
    sql = "CREATE TABLE user (" \
          "username TEXT, " \
          "passwort TEXT);"
    cur.execute(sql)
    con.commit()
    con.close()