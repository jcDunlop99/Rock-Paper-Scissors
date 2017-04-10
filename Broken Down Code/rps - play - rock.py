def playRock():
    cpuroll = random.randint(1,3)
    if cpuroll == 1:
        print(">>>> You both have rock, Draw <<<<")
    elif cpuroll == 2:
        print(">>>> Paper covers rock, You Lose <<<<")
    elif cpuroll == 3:
        print(">>>> Rock smashes scissors, You win <<<<")
    menu()
