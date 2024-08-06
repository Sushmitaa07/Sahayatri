#p
for row in range(6):
    for column in range(5):
        if (column == 0) and (row==1 or row==2 or row==3):
            print("*", end="  ")
        elif(column == 1) and (row==0 or row==4):
            print("*", end="  ")
        elif(column == 2) and (row==0 or row==3 or row==4):
            print("*", end="  ")
        elif(column == 3) and (row==0 or row==4):
            print("*", end="  ")
        elif(column == 4) and (row==1 or row==2 or row==3 or row==5):
            print("*", end="  ")
        else:
            print(end=" ")
    print()

#P
for row in range(7):
    for column in range(5):
        if (column == 0) and (row==1 or row==2 or row==3 or row==4 or row==5 or row==6):
            print("*", end=" ")
        elif(column == 1) and (row==0 or row==3):
            print("*", end=" ")
        elif(column == 2) and (row==0 or row==3 ):
            print("*", end=" ")
        elif(column == 3) and (row==0 or row==3):
            print("*", end=" ")
        elif(column == 4) and (row==1 or row==2 ):
            print("*", end=" ")
        else:
            print(end="  ")
    print()

#R
for row in range(7):
    for column in range(5):
        if (column == 0) and (row==1 or row==2 or row==3 or row==4 or row==5 or row==6):
            print("*", end=" ")
        elif(column == 1) and (row==0 or row==3):
            print("*", end=" ")
        elif(column == 2) and (row==0 or row==3 or row==4 ):
            print("*", end=" ")
        elif(column == 3) and (row==0 or row==3 or row==5):
            print("*", end=" ")
        elif(column == 4) and (row==1 or row==2 or row==6):
            print("*", end=" ")
        else:
            print(end="  ")
    print()


#A
for row in range(7):
    for coloum in range(5):
        if (coloum == 0) and (row ==1 or row ==2 or row ==3 or row==4 or row ==5):
            print ("*",end=" ")
        elif (coloum == 1) and (row ==1 or row ==3 ):
            print ("*",end=" ")
        elif (coloum == 2) and (row ==1 or row ==3 ):
            print ("*",end=" ")
        elif (coloum == 3) and (row ==1 or row ==3 ):
            print ("*",end=" ")
        elif (coloum == 4) and (row ==1 or row ==2 or row ==3 or row ==4 or row ==5 ):
            print ("*",end=" ")
        else:
            print(end="  ")
    print()

    #K
    for row in range(7):
         for column in range(4):
              if (column == 0) and (row==1 or row==2 or row==3 or row==4 or row==5 or row==6):
                  print("*", end=" ")
              elif(column == 1) and (row==2 or row==4):
                  print("*", end=" ")
              elif(column == 2) and (row==1 or row==5 ):
                   print("*", end=" ")
              elif(column == 3) and (row==0 or row==6):
                    print("*", end=" ")
              else:
                  print(end="  ")
    print()

    #R
    for row in range(7):
      for column in range(5):
        if (column == 0) and (row==1 or row==2 or row==3 or row==4 or row==5 or row==6):
            print("*", end=" ")
        elif(column == 1) and (row==0 or row==3):
            print("*", end=" ")
        elif(column == 2) and (row==0 or row==3 or row==4 ):
            print("*", end=" ")
        elif(column == 3) and (row==0 or row==3 or row==5):
            print("*", end=" ")
        elif(column == 4) and (row==1 or row==2 or row==6):
            print("*", end=" ")
        else:
            print(end="  ")
    print() 


