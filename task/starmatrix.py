n=int(input("Enter the rows:"))
for row in range(n):
    for col in range(n):
       if col==0 or row==0 or col+row==2 or col+row==3 or col+row==4:
            print("*", end="")
       else:
            print("", end="")
    print("\n")