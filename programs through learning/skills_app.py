# program by amuel ayman
#date 14/7/2024
import sqlite3
#connection to database
db=sqlite3.connect("sam.db")
#set the cursor
cursor=db.cursor()
#create table
db.execute("create table if not exists skills(skill,progress,id)")
#function to commit and close
def commit_and_close():
    db.commit()
    db.close()
    print("the database is closed")
status="e"
messsage="""
What do you want to do 
"a" Add New skill
"s" Show all skils
"d" delete A skill
"u" update A skill
"q" Quit the App
Choose an option:
"""
user_input=input(messsage).strip().lower()
# global user_input
# while status=="c":
#   user_input=input(messsage).strip().lower()
#   status=input("enter c to continue and e to exit")

#define functions
#function to add new skill
def Add_New() :
    skill=input("enter your skill : ").strip().capitalize()
    id=input("enter your id : ").strip()
    cursor.execute(f"select name from skills where id='{id}' and skill='{skill}'")
    result=cursor.fetchone()
    if result!=None:
        print("this skill exists")
        decission=input("do you want to update the skill? Y/N").strip()
        if decission=="Y":
             progress=input("enter the new progress progress : ").strip()
             cursor.execute(f"update skills set progress='{progress}' where skill='{skill}' and id='{id}'")
        else:
            commit_and_close()
    else:   
        progress=input("enter your progress : ").strip()
        cursor.execute(f"insert into skills(skill,progress,id) values('{skill}','{progress}','{id}')")
    print("skill added")
    commit_and_close()
#function to show all skills
def Show_all():
    id=input("enter your id : ").strip()
    cursor.execute(f"select * from skills where id='{id}'")
    result=cursor.fetchall()
    if len(result)>0:
       print(f"showing all skills for user with id : {id}")
    else:
       print("this user have no skills")
    for row in result:
      print(f"your skill is >= {row[0]}")
      print(f"your progress is >= {row[1]}")
    commit_and_close()
#function to delete a skill
def delete_skill():
    skill=input("enter skill to delete : ").strip().capitalize()
    id=input("enter your id : ").strip()
    cursor.execute(f"delete from skills where skill='{skill}' and id='{id}'")
    print("skill deleted")
    commit_and_close()
#function to update a skill
def update_skill():
    skill=input("enter your skill to update : ").strip().capitalize()
    progress=input("enter the new progress progress : ").strip()
    id=input("enter your id")
    cursor.execute(f"update skills set progress='{progress}' where skill='{skill}' and id='{id}'")
    print("skill updated")
    commit_and_close()
#function to quit the app
def quit_app():
    print("app quited")
    commit_and_close()
#every choose lead to function
if user_input=="a":
    Add_New()
elif user_input=="s":
    Show_all()
elif user_input=="d":
    delete_skill()
elif user_input=="u":
    update_skill()
elif user_input=="q":
    quit_app()
else:
    print("not acceptable input")


    