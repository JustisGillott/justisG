import math
equations = []
def menu():
    a = int(input("Enter number for a: "))
    b = int(input("Enter number for b: "))
    c = int(input("Enter number for c: "))

f = b**2-4*a*c

if f < 0:
    print("This equation has no roots.")
    
elif f == 0:
    x = (-b + math.sqrt (f)) /2*a
    print("This equation has one root.")

else:
    xa = (-b + math.sqrt( (b**2) - (4* (a*c)))) /(2*a)
    xb = (-b - math.sqrt( (b**2) - (4* (a*c)))) /(2*a)
    print("This equation has two roots.")
    print(xa,xb)
    
    answer = input("Any more? ")
    if answer = 'N':
        notDone = False
        
