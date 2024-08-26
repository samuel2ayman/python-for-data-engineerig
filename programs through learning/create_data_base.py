import sqlite3
new_db=sqlite3.connect("sam.db")
new_db.execute("create table if not exists users(id integer,name text,salary integer)")
db_cur=new_db.cursor()
my_list=["samuel","dave","nataly"]
for key , user in enumerate(my_list):
    db_cur.execute(f"insert into users(id,name,salary) values({key+1},'{user}',{key*1000})")
#to commit 
new_db.commit()
db_cur.execute("select * from users")
print(db_cur.fetchmany(7))