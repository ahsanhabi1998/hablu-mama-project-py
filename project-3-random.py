while True:
    import random
    all_ran = random.randrange (1,200)
    # print( all_ran)
    userInpit = int (input("Gues the bumber : "))
    if userInpit > all_ran:
        print( all_ran)
        print("the is to high ")
    elif all_ran > userInpit:
        print( all_ran)
        print("the number is too low")
    else :
        print( "yeas , you matched the number")
    