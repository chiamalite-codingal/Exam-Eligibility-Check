medical = int(input("Do you have medical issues? 1.Yes 2.No"))
attend = int(input("Enter attendance:"))
if medical==1:
    print("Allowed for exam")
else:
    if attend>=75:
        print("Allowed for exam")
    else:
        print("Not allowed for exam")