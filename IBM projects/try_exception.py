def safe_divide(numerator ,denominator):
    try:
        result=numerator/denominator
        return result
    except ZeroDivisionError:
        print("Error: you cannot divide with zero")
        return None
    
numerator=int(input("enter numerator"))
denominator=int(input("enter denomirator"))
print(safe_divide(numerator ,denominator))
    
    