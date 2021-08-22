num = int (input("Enter Your Marks: "))
if 200 >= num >= 0:
    if num >= 100:
        print ("A")
    elif num >= 50:
        print("B")
    elif num >= 35:
        print("C")
    else:
        print("Fail")

else:
    print("Invalid Marks")
