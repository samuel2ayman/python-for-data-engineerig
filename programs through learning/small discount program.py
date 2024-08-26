members=["samuel","micheal","tefa","nataly","fendi"]
name=input("enter your name ").strip().capitalize()
if name in members :
  print(f"hello {name}")
  print("your discount is 50%")
else:
    print(f"Hello {name}")
    print("your discount is 20%")
    cond=input("do you want more discount Y/N ").strip().capitalize()
    if cond=="Y":
        members.append(name)
        print("your discount is 50%")
    else :
        print("your discount is 20%")
print(members)