import sqlite3
import os

def create_db():
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    sql = "CREATE TABLE user (" \
          "username TEXT, " \
          "passwort TEXT);"
    cur.execute(sql)
    con.commit()

    Benutzer = "admin"
    Passwort = "admin"
    insert = f"INSERT INTO anmeldung VALUES('{Benutzer}', '{Passwort}');"
    cur.execute(insert)
    con.close()

def NewAcc(name, passwort):
    connection = sqlite3.connect("mathe.db")
    cursor = connection.cursor()
    InsertNewAcc = f"INSERT INTO anmeldung VALUES('{name}', '{passwort}');"
    cursor.execute(InsertNewAcc)
    connection.commit()
    connection.close()

def Prüfanm(name, passwort):
    con = sqlite3.connect("mathe.db")
    cur= con.cursor()

    statement = f"""SELECT benutzername
                    FROM anmeldung
                    WHERE benutzername ='{name}' AND passwort= '{passwort}'"""
    cur.execute(statement)
    k = cur.fetchone()
    if not k:
        return False
    else:
        return True
def regristierungs_Prüfen(Benutzer):
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    sql = f"""SELECT benutzername 
          FROM anmeldung 
          WHERE benutzername = '{Benutzer}';"""

    PrüfRgst = cur.execute(sql).fetchone()
    if PrüfRgst:
        return False
    else:
        return True

def Ausgabe():
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    sql = "SELECT * FROM anmeldung"
    ausgabe = cur.execute(sql).fetchall()
    print(ausgabe)
    con.commit()
    con.close()

if os.path.exists("mathe.db"):
    print("Datenbank existiert bereits")
else:
    create_db()
