# Data Base
import sqlite3

con = sqlite3.connect("condominios.db")
cursor = con.cursor()

cursor.execute("""
        INSERT INTO sindicos VALUES 
            (2, 'Bruna Falavina Bach', 55463554872, 479853546)
    """)

con.commit()

con.close()
