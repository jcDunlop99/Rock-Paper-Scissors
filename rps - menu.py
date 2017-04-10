def menu():
    print("<Welcome to my Rock, Paper, Scissors Game>")
    print("The objective is simple, play the classic decision making game")
    print(">>>> Input 1 to start playing <<<<")
    print(">>>> Input 2 to veiw credits <<<<")
    print(">>>> Input 3 to exit window <<<<")
    sel = int(input("Selection >> "))
    if sel == 1:
        print("Playing game")
        play()
    elif sel == 2:
        print("Credits")
        credits()
    elif sel == 3:
        print("Exiting Program")
        quit()
    else:
        sefl = str(sel)
        print(sefl , "is not an accepted input form, returning to top menu.")
        time.sleep(3)
        menu()
