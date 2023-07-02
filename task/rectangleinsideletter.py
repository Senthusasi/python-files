row=int(input("enter the no of rows:"))
col=5
for i in range(row):   
        for j in range(col):

            if i==0 or i==(row-1) or j==0 or j==(col-1): 
                print("*", end=" ")
            elif i==1 or i==row or j==1 or j==col :
                print(" ", end=" ")
            elif i==3 or i==row or j==3 or j==col:
                 print(" ", end=" ")
            else:
                print("s",end=" ")
                 
        print()