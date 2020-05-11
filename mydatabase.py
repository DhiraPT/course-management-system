import _sqlite3

con = _sqlite3.connect('database.db')
cur = con.cursor()

cur.execute("""CREATE TABLE students (
            id text,
            name text,
            phone integer,
            grade integer,
            type text,
            fee text
           )""")

con.commit()
con.close()