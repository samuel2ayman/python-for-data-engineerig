ofile=None
tries=5
while tries > 0 :
    try:
        print("enter the file absolute path to open")
        print("for example : E:\pro\python")
        the_file=input("the path :").strip()
        ofile=open(the_file,"r")
        print(ofile.read())
        break
    except:
        print("this is wrong path try again")
        tries-=1
        print(f"you have {tries} tries")
    finally:
        if ofile is not None:
            ofile.close()
            print("the file is closed")
else:
    print("all tries is done")