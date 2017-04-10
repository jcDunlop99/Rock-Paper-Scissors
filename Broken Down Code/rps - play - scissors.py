def playScissors():
    cpuroll = random.randint(1,3)
    if cpuroll == 1:
        print(">>>> Rock smashes scissors, You Lose <<<<")
    elif cpuroll == 2:
        print(">>>> Scissors cut paper, You Win! <<<<")
    elif cpuroll == 3:
        print(">>>> You both have scissors, Draw <<<<")
    menu()
