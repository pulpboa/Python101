n = int(input("Write a number: "))
for w in range (1 , n +1):
    print ("Table of" , w , '\n')
    for e in range (1 ,11):
        print(w  ,"*" , e  ,'=' ,w *e )
    print("______________" , '\n')    