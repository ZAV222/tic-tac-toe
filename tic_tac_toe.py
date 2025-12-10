a = ["_"]*9

def printer():
    cn = 0
    while cn < 9:
        if cn==3 or cn == 6:
            print()
        print(a[cn],end=" ")
        cn+=1
    print()


printer()

currentUser = "o"
slst = []
z = 1
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
while z <= 9:
    ask = int(input("Enter choice (0-8): "))
    if ask in slst:
        print("Cannot choose already chosen")
        continue
    
    slst.append(ask)
    a[ask] = currentUser

    printer()
    print()

    # check win
    
    for combo in wins:
        if a[combo[0]] == a[combo[1]] == a[combo[2]] != "_":
            print(a[combo[0]], "wins")
            exit()

    # switch player
    currentUser = "o" if currentUser == "x" else "x"
    z += 1

print("It's a tie!")
