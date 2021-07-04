import sqlite3

#On cree une connection a la bd et on cree la table si besoin
def init():
  # Create db if not exist
  con = sqlite3.connect('hl.db')
  cur = con.cursor()

  # Profile table
  cur.execute("""CREATE TABLE IF NOT EXISTS profile
    (id integer primary key, name text)
    """)
  con.commit()

