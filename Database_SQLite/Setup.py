# %%
import sqlite3

# %%
con = sqlite3.connect('test.db',timeout=40)
cur = con.cursor()


# %%
try: 
        cur.execute('''CREATE TABLE product(
                product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
                )''')
        cur.execute('''CREATE TABLE warehouse(
                warehouse_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
                )''')
except Exception as e:
        print(e)
        try: 
                cur.execute('''ALTER TABLE product ADD(
                        name VARCHAR''')
                cur.execute('''ALTER TABLE warehouse ADD(        
                        warehouse_id INT PRIMARY KEY DESC)''')
        except Exception as e:
                print(e)
                try: 
                        cur.execute('''DROP TABLE product''')
                        cur.execute('''DROP TABLE warehouse''')
                except Exception as e:
                        print(e)
# %%
cur.execute('''ALTER TABLE product ADD COLUMN
                        name VARCHAR''')
cur.execute('''INSERT INTO {}({})VALUES({})'''.format("product","name","'CTS3'"))
cur.execute('''SELECT * FROM product''')

print(cur.fetchall())
cur.execute('''ALTER TABLE warehouse ADD COLUMN
                        name VARCHAR''')
# %%
con.commit()
con.close()
