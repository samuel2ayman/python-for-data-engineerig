tries=5
password="samuel"
writen_pass=input("write password ")
while writen_pass!=password :
    tries-=1
    print(f"wrong password you have {tries} tries left")
    writen_pass=input("write password ")
    if tries == 0:
        break
else:
    print("correct password")

print("loop is done")    