import random
choice=input(str("DO you want to roll the dice? yes(y)/no(n)")).lower()
if choice=="y":
    a=random.randint(1,6)
    b=random.randint(1,6)
    print(f'(the dice number you got are {a} and {b})')
    
elif choice=="n":
    print("Thank you for playing:")
else:
    print("INVALID INSTRUCTIONS")


