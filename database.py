import sqlite3

def datenbankertellen():
    con =sqlite3.connect("Datenbank.db")
    cur = con.cursor()


    Tabelle = f"""CREATE TABLE anmeldung(
                    benutzername TEXT,
                    passwort TEXT
                );"""
    cur.execute(Tabelle)
    con.commit() 
