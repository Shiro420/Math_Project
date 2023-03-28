import sqlite3
import os

def create_db():
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    sql =  f"""CREATE TABLE anmeldung(
                benutzername TEXT,
                passwort TEXT
            );"""
    cur.execute(sql)
    con.commit()

    Benutzer = "A"
    Passwort = "A"
    insert = f"INSERT INTO anmeldung VALUES('{Benutzer}', '{Passwort}');"
    cur.execute(insert)
    con.close()

def NewAcc(Benutzer, Passwort):
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()
    InsertNewAcc = f"INSERT INTO anmeldung VALUES('{Benutzer}', '{Passwort}');"
    cur.execute(InsertNewAcc)
    con.commit()
    con.close()

def anmeldung(Benutzer, Passwort):
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    statement = f"""SELECT benutzername
                    FROM anmeldung
                    WHERE benutzername ='{Benutzer}' AND passwort= '{Passwort}'"""
    cur.execute(statement)
    k = cur.fetchone()
    if not k:
        return False
    else:
        return True
def regristierungs_prüfen(Benutzer):
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    sql = f"""SELECT benutzername 
          FROM anmeldung 
          WHERE benutzername = '{Benutzer}';"""

    regristierungs_Prüfen = cur.execute(sql).fetchone()
    if regristierungs_Prüfen:
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
