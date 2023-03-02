import sqlite3

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
    cursor.execute(insert)
    con.close()
creat_db()
