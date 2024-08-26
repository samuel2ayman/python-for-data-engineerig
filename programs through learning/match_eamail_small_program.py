import re
emails_list=[]
customer_email=input("Enter your email : ")
matched=re.search(r"([A-Za-z-0-9]+@(gmail|outlook|microsoft)\.(com|org))",customer_email)
print(matched)
if matched!=[]:
    emails_list.append(matched)
    print("the email is matched")
else:
    print("the email is not matched")
    
# for emails in emails_list:
#     print(f"this is the matched email: {emails}") #used for find all
    