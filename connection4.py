from funcandvariable import *
while True:
    countA=0
    countB=0
    for i in matrix:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
        for j in range(4):
            if i[j]=="A":
                countA+=1
            elif i[j]=="B":
                countB+=1
    if countA+countB==16:
        print("The game is a draw")
        break
    gamer = gamers[index]
    val=-5
    while not(0<=val and val<4):
        try:
            val=int(input("Choose numbers between 1 and 4:"))-1
            if not(0<=val and val<4):
                print("Wrong value.!")
        except:
            print("Wrong value.!")
    control=-1
    for i in matrix:
        if i[val]=="A" or i[val]=="B":
            matrix[control][val]=gamer
            break
        elif i[val]==matrix[3][val]:
            matrix[3][val]=gamer
            break
        control+=1
    if winner(matrix,gamer):
        for i in matrix:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
        if gamer=="A":
            print("Gamer 1 is won the game.")
            break
        else:
            print("Gamer 2 is won the game")
            break
    if index==1:
        index=0
    else:
        index=1

