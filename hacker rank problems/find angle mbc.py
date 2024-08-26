import math as m
ab=int(input())
bc=int(input())
ac=m.sqrt(pow(ab,2)+pow(bc,2))
print(f"{round(m.degrees(m.asin(ab/ac)))}{chr(176)}")
