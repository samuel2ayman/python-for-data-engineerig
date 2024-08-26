class members:
    def __init__(self,first,last,gender,age,age_in_days):
        self.first_name=first
        self.last_name=last
        self.gender=gender
        self.age=age
        self.age_in_days=age_in_days
        
    def title(self):
        if self.gender=="male" or self.gender=="MALE" :
           print(f"Hello Mr {self.first_name}")   
        elif self.gender=="female"or self.gender=="FEMALE":
            print(f"Hello Mrs {self.first_name}") 
        else:
            print(f"Hello {self.first_name}") 
    def all_info(self):
        print(f"your full name is {self.first_name} {self.last_name}")
        print(f"your age is :{self.age} ")
        print(f"you lived for :{self.age_in_days}")


i=2
while i>0:
    if i==2:
        print(f"1st member")
    else :
        print(f"2nd member")
    first_name=input("enter your first name :")
    last_name=input("enter your last name :")
    age=int(input("enter your age:"))
    gender=input("enter your genger : ")
    age_in_days=age*365
    print("#################################")
    member_one=members(first_name,last_name,gender,age,age_in_days)
    member_one.title()
    member_one.all_info()
    print("#################################")
    i-=1
else:
    print("storage is full")