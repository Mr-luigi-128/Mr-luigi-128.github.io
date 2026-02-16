import time
import random
DTheme = "---------------------------------------"
points = 100
bet = 0 
cont = True
dif = -1
validatePoints = 103
y=0
n=0
Tc=0 
v1 = 0
v2 = 1 
v3 = 9999999
mult=0.5

start = input("start (anything except NO to start)")
if start == "NO":
    print("Bruh")
    exit()
    
sets = input("would you like to veiw settings (input 7 if you would)")
if sets == "7":
    delay = int(input("what would you like to set the delay between questions to be? (please enter a number 0.1 - 10)"))
    time.sleep(1)
    print("There isnt atually a limit for this. negative numbers will crash this, but theres no limit for posotive numbers")
    time.sleep(5)
    print("I just would not reccomend setting it any higher or it will feel like it takes years to progress")
    DashTheme = str(input("Enter the style separator you would like (leave empty for none)"))
    DTheme = DashTheme

while dif != "1" and dif != "2" and dif != "3" and dif != "4" and dif != "5" and dif !="0" and dif !="true gambler":
    dif = input("""choose the difficuty
    1 - Easy
    2 - Normal
    3 - Hard
    4 - Very Hard
    """)

if dif == "1":
    high = 5
    mult = 1.5
    print("range: 1-5")
elif dif == "2":
    high = 10
    mult = 1.75
    print("range: 1-10")
elif dif == "3":
    high = 25
    mult = 2
    print("range: 1-25")
elif dif == "4":
    high = 50
    mult = 3
    print("range: 1-50")
elif dif =="0":
    print("range: 1-1")
    mult = 1.1
    high = 1
elif dif =="true gambler":
    print("range: 1-777")
    print("true gambler mode activated")
    high = 777
    mult = 0.5
else:
    high = 36936353765363785387344573489346837373787968979786278638732623873872389
    print("range: 1-yes")
    mult = 999
    print("evil suffering mode activated")

RANDOMTIPSRAH = [
    "01 - 'yes, i aknowledge the typos. no, i am not fixing them'",
    "02 - this code is held together by hopes, dreams and a bowl of scrambled egg. pls dont break it :(",
    "03 - what do i put here?",
    "04 - 1 higher than the hardest gamemode shown for a 'bad time'",
    "05 - noob",
    "06 - these have like a 1% spawn chance",
    "07 - would be really funny if you made the difficulty 777 - someone",
    "08 - 0. im not finna say more",
    "09 - 'are you winning son?'",
    "10 - there is a small chance an event will happen that could give you some free points"
]

yesMessages = [
    "You got it right",
    "You didnt get it wrong",
    "You win",
    "You are correct",
    "You arent incorrect",
    ":)",
    "yes",
    "get in!",
    "might of got it right or wrong idk not too sure"
]

noMessages = [
    "You got it Wrong",
    "You didnt get it right",
    "You win'nt",
    "You are'nt correct",
    "nuh uh",
    ":(",
    "no",
    "GET OUT!",
    "might of got it right or wrong idk not too sure"
]

print("")
while cont:
    print(DTheme)
    print("hey, you have", points, "points")
    validatePoints = 0

    # -------------------------------
    # FIXED BET VALIDATION SECTION
    # -------------------------------
    while validatePoints == 0:
        bet = int(input("enter points to bet (decimals will crash this :3) "))

        if bet <= 0:
            print("you cant bet 0 or negative points bruh")
        elif bet > points:
            print("You dont have that many points brah")
        else:
            validatePoints = 1
    # -------------------------------

    print("")
    guess = int(input("enter guess"))
    print("")
    g = random.randint(1,high)
    print(g)

    if guess == g:
        print(random.choice(yesMessages))
        points = points + (bet * mult)
        print(points)
        tc = points
        tc = tc + points
        y=y+1
    else:
        print(random.choice(noMessages))
        points = points - (bet)
        print(points)
        n=n+1

    a  = random.randint(0,100)
    if a == 32:
        print(random.choice(RANDOMTIPSRAH))

    Qtime = random.randint(0,50)
    if Qtime == 48:
        print("SUPRISE EVENT!")
        rwd = random.randint(10,55) * 1.5
        print("Reward for correctness- ", rwd)
        v1 = random.randint(-10,555)
        v2 = random.randint(-100,50)
        v3 = v1 + v2
        print("ADD THESE 2 NUMBERS!!!!!!")
        print(v1)
        print(v2)
        qtimans = int(input("enterino your guesserino"))
        print(v3)
        if qtimans == v3:
            print("Correct:3")
            points = points + rwd
        elif qtimans != v3:
            print("INCORRECT(we gotta lose some points)")
            points = points - rwd

    if points <= 0:
        print("You lose")
        print("__________________________________")
        time.sleep(0.5)
        print("you got a whole",y,"right!")
        if y == 0:
            print("wow, uh, 0...")
        elif y > 0 and y < 5:
            print("ok...")
        elif y > 5 and y < 20:
            print("nice")
        elif y > 20 and y < 40:
            print("DAYUM")
        elif y == 64:
            print(":)")
        time.sleep(1)
        print("")
        print("you failed total of",n,"time(s)!")
        time.sleep(1)
        print("dam...")
        print("")
        time.sleep(1)
        print("you made a total of",Tc)
        print("__________________________________")
        exit()
