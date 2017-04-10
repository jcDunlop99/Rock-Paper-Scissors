#Joshua C. Dunlop
#RPS Program
#start - 20170329
#finish - 20170407
#patch1 - 20170410
import random, time

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

def play():
    print("<Please Select Your Tool>")
    print(">>>> Input 1 to select rock <<<<")
    print(">>>> Input 2 to select paper <<<<")
    print(">>>> Input 3 to select scissors <<<<")
    sel = int(input("Selection >> "))
    if sel == 1:
        print("Your tool of choice: Rock")
        time.sleep(1)
        playRock()
    elif sel == 2:
        print("Your tool of choice: Paper")
        time.sleep(1)
        playPaper()
    elif sel == 3:
        print("Your tool of choice: Scissors")
        time.sleep(1)
        playScissors()
    elif sel == 4:
        playSecret()
    else:
        sefl = str(sel)
        print(sefl , "is not an accepted input form, returning to selection.")
        time.sleep(3)
        play()

def credits():
    print("                    /")
    print("               ,.. /")
    print("             ,'   ';")
    print("  ,,.__    _,' /';  .")
    print(" :','  ~~~~    '. '~")
    print(":' (   )         )::,")
    print("'. '. .=----=..-~  .;'")
    print(" '  ;'  ::   ':.  '")
    print("   (:   ':    ;)")
    print('''    \\    '"  ./''')
    print('''     '"      '"''')
    print("Written by Joshua Dunlop")
    time.sleep(10)
    menu()

def playRock():
    roll = cpuRoll()
    if roll == 1:
        print(">>>> You both have rock, Draw <<<<")
    elif roll == 2:
        print(">>>> Paper covers rock, You Lose <<<<")
    elif roll == 3:
        print(">>>> Rock smashes scissors, You win <<<<")
    time.sleep(3)
    menu()

def playPaper():
    roll = cpuRoll()
    if roll == 1:
        print(">>>> Paper covers rock, You Win! <<<<")
    elif roll == 2:
        print(">>>> You both have paper, Draw <<<<")
    elif roll == 3:
        print(">>>> Scissors cut paper, You Lose <<<<")
    time.sleep(3)
    menu()

def playScissors():
    roll = cpuRoll()
    if roll == 1:
        print(">>>> Rock smashes scissors, You Lose <<<<")
    elif roll == 2:
        print(">>>> Scissors cut paper, You Win! <<<<")
    elif roll == 3:
        print(">>>> You both have scissors, Draw <<<<")
    time.sleep(3)
    menu()

def playSecret():
    print(">>>> Dynamite beats everything, You Cheated!! <<<<")
    time.sleep(3)
    menu()

def cpuRoll():
    for i in range(15):
        roll = random.randint(1,3)
    return roll

menu()
