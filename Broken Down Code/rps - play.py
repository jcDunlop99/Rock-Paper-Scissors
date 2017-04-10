def play():
    print("<Please Select Your Tool>")
    print(">>>> Input 1 to choose rock <<<<")
    print(">>>> Input 2 to choose paper <<<<")
    print(">>>> Input 3 to choose scissors <<<<")
    sel = int(input("Selection >> "))
    if sel == 1:
        print("sel == 1")
        playRock()
    elif sel == 2:
        print("sel == 2")
        playPaper()
    elif sel == 3:
        print("sel == 3")
        playScissors()
    else:
        sefl = str(sel)
        print(sefl , "is not an accepted input form, returning to selection.")
        time.sleep(3)
        play()
