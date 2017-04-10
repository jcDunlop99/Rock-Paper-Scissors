def playPaper():
    cpuroll = random.randint(1,3)
    if cpuroll == 1:
        print(">>>> Paper covers rock, You Win! <<<<")
    elif cpuroll == 2:
        print(">>>> You both have paper, Draw <<<<")
    elif cpuroll == 3:
        print(">>>> Scissors cut paper, You Lose <<<<")
    menu()
