n=int(input("Enter the rows:"))
for row in range(n):
    for col in range(n):
       if row==0 or (col==0 and col==3) or col==0 or (row==0 and row==3) or col==1 and row==1 or col==1 and row==2 or col==2 and row==2:
     #   if row==0 or (col==0 and col==3) or row==1 and (col==1 or col==2) or row==2 and (col==1 or col==2 or col==3) or row==3 and(col==2):   
            print("*", end=" ")
       else:
            print(" ", end=" ")
    print("\n")

# for i in range(0,1):
#         print("* * * *\n* *\n* * *\n*")
        