import sys
class UnknownBallError(Exception):
    pass
class CoordinateError(Exception):
    pass
try:    
    checklist = []
    gamemap = []
    currentscore = 0
    def gamemapgenerator():   
        try:
            with open("{}".format(sys.argv[1]), "r") as ballsinput:
                global gamemap
                gamemap = []
                try:
                    for lines in ballsinput.readlines():
                        row = lines.split()
                        gamemap.append(row)
                    assert len(gamemap) != 0
                except IndexError:
                    print("An error (m)ight be here?")
                except AssertionError:
                    raise AssertionError
            ballsinput.close()
        except AssertionError:
            raise AssertionError
        except:
            print("Something went terribly wrong HERE!")
            raise IndexError
    def gamemapprinter():
        global gamemap
        a = 0
        print("--------------------------------------------------")
        print("   ", end="")
        for i in range(len(gamemap[0])):
            print(i, end=" ")
        print()
        for rows in gamemap:
            print("{}) ".format(a), end="")
            a = a+1
            for balls in rows:
                print(balls, end=" ")
            print("")
        print("\nSCORE: {}.".format(currentscore))
    def gameendcheck():
        try:
            global rowlength, gameenddict, columnlength, checklist
            rowlength, columnlength, checklist, gameenddict = len(gamemap[0]), len(gamemap), [], dict()
            for checkend in range(len(gamemap)):
                for checkend2 in range(len(gamemap[checkend])):
                    yaxisball, xaxisball, ball, neighbour = checkend, checkend2, gamemap[checkend][checkend2], 0
                    if ball != "B" and ball != "G" and ball != "W" and ball != "Y" and ball != "R" and ball != "P" and ball != "O" and ball != "D" and ball != "F" and ball != "X" and ball != " ":
                        raise UnknownBallError
                    if yaxisball+1 != columnlength:   
                        if  ball == gamemap[yaxisball+1][xaxisball] and ball != " ":
                            neighbour = neighbour+1
                    if yaxisball-1 >= 0:
                        if ball == gamemap[yaxisball-1][xaxisball] and ball != " ":
                            neighbour = neighbour+1 
                    if xaxisball+1 != rowlength:
                        if ball == gamemap[yaxisball][xaxisball+1] and ball != " ":
                            neighbour = neighbour+1   
                    if xaxisball-1 >= 0:
                        if ball == gamemap[yaxisball][xaxisball-1] and ball != " ":
                            neighbour = neighbour+1
                    if ball == "B":
                        ballweight = 9
                    elif ball == "G":
                        ballweight = 8
                    elif ball == "W":
                        ballweight = 7
                    elif ball == "Y":
                        ballweight = 6
                    elif ball == "R":
                        ballweight = 5
                    elif ball == "P":
                        ballweight = 4
                    elif ball == "O":
                        ballweight = 3
                    elif ball == "D":
                        ballweight = 2
                    elif ball == "F":
                        ballweight = 1
                    elif ball == "X":
                        ballweight = 0
                    elif ball == " ":
                        ballweight = 0
                    gameenddict[(xaxisball, yaxisball)] = [ball, neighbour, ballweight]
        except UnknownBallError:
            raise UnknownBallError
        except IndexError:
            print("Can I ask a question?")
        except:
            print("Or error might be here?")           
        try:
            for balls in gameenddict:
                if gameenddict[balls][1] >= 1 and gameenddict[balls][0] != " " or gameenddict[balls][0] == "X":
                    checklist.append(1)
                else:
                    checklist.append(0)
        except:
            print("Bro, what have you done? Just dont touch anything!")
    def vertical_check():
        empty_line = 0
        deletedlines = []
        for horizontal in range(len(gamemap[0])):
            fullempty = []
            for vertical in range(len(gamemap)):
                if gamemap[vertical][horizontal] == " ":
                    fullempty.append(1)
            if fullempty.count(1) == len(gamemap) and len(fullempty) != 0:
                deletedlines.append(horizontal)
        if len(deletedlines) > 0:
            for deleted in reversed(deletedlines):
                for a in gamemap:
                    a.pop(deleted)      
                continue  
        for horizontal in range(len(gamemap[0])):
            for vertical in range(len(gamemap)-1, -1, -1):
                while vertical != 0 and gamemap[vertical][horizontal] == " ":
                    emptylist = []
                    for check in range(vertical+1):
                        if gamemap[check][horizontal] == " ":
                            emptylist.append(1)
                        else:
                            emptylist.append(0)
                    if 0 not in emptylist:
                        break
                    for changing in range(vertical,0,-1):
                        gamemap[changing][horizontal] = gamemap[changing-1][horizontal]
                    
                    gamemap[0][horizontal] = " "
        for i in range(len(gamemap)-1, -1, -1):
            if len(gamemap[i]) == gamemap[i].count(" "):
                gamemap.pop(i)
    def neighbourdelete():    
        global yaxis, xaxis, gameenddict, columnlength, rowlength, returncount
        if returncount == 0:    
            if yaxis-1 >= 0 and (gameenddict[(xaxis, yaxis-1)][0] == " " or gameenddict[(xaxis, yaxis-1)][0] == theball) and gameenddict[(xaxis, yaxis-1)][1] != 0:
                                gameenddict[(xaxis, yaxis-1)][1] = gameenddict[(xaxis, yaxis-1)][1]-1
            if yaxis+1 < columnlength and (gameenddict[(xaxis, yaxis+1)][0] == " " or gameenddict[(xaxis, yaxis+1)][0] == theball) and gameenddict[(xaxis, yaxis+1)][1] != 0:
                                gameenddict[(xaxis, yaxis+1)][1] = gameenddict[(xaxis, yaxis+1)][1]-1
            if xaxis-1 >= 0 and (gameenddict[(xaxis-1, yaxis)][0] == " " or gameenddict[(xaxis-1, yaxis)][0] == theball) and gameenddict[(xaxis-1, yaxis)][1] != 0:
                                gameenddict[(xaxis-1, yaxis)][1] = gameenddict[(xaxis-1, yaxis)][1]-1
            if xaxis+1 < rowlength and (gameenddict[(xaxis+1, yaxis)][0] == " " or gameenddict[(xaxis+1, yaxis)][0] == theball) and gameenddict[(xaxis+1, yaxis)][1] != 0:
                                gameenddict[(xaxis+1, yaxis)][1] = gameenddict[(xaxis+1, yaxis)][1]-1
    gamemapgenerator()
    gameendcheck()
    while True:
        returncount, fork = 0, False
        if len(gamemap) == 0:
            print("--------------------------------------------------")
            print("\nSCORE: {}.".format(currentscore))
            break
        gamemapprinter()
        gameendcheck()
        if 1 not in checklist:
            break
        userchoice = input("Choose a ball by choosing a row and a column with a space between them.\n")
        coordinates = userchoice.split()
        try:    
            if len(coordinates) != 2:
                raise CoordinateError
            yaxis, xaxis = int(coordinates[0]), int(coordinates[1])
        except ValueError:
            print("--------------------------------------------------\n", "Dude, you gotta choose with numbers...")
            continue
        except CoordinateError:
            print("--------------------------------------------------\n","Now, I will teach you how to enter 2 numbers!")
            continue
        coordinates2 = (xaxis, yaxis)
        allcoordinates = [] 
        forkcoord = []
        bomblist = []
        try:
            theball = gamemap[yaxis][xaxis]
            if xaxis < 0 or yaxis < 0:
                raise IndexError
        except IndexError:
            print("--------------------------------------------------\n","Bro, you got a little high, you know.")
            continue
        if theball == " ":
            print("--------------------------------------------------\n","Bro, can you not to choose an (e)mptiness?")
            continue
        if theball == "X":
            bomblist.append((xaxis, yaxis))
            for bombs in bomblist:
                for horizontal in range(len(gamemap[0])):
                    if gamemap[bombs[1]][horizontal] == "X" and (horizontal,bombs[1]) not in bomblist:
                        bomblist.append((horizontal, bombs[1]))
                for vertical in range(len(gamemap)):
                    if gamemap[vertical][bombs[0]] == "X" and (bombs[0],vertical) not in bomblist:
                        bomblist.append((bombs[0], vertical))
            for bombs in bomblist:
                for horizontal in range(len(gamemap[0])):
                    if gameenddict[(horizontal, bombs[1])][0] != " ":
                        currentscore = currentscore+gameenddict[(horizontal, bombs[1])][2]
                    gamemap[bombs[1]][horizontal] = " "
                    gameenddict[(horizontal, bombs[1])][0] = " "
                    
                for vertical in range(len(gamemap)):
                    if  gameenddict[(bombs[0], vertical)][0] != " ":
                        currentscore = currentscore+gameenddict[(bombs[0], vertical)][2]
                    gamemap[vertical][bombs[0]] = " "
                    gameenddict[(bombs[0], vertical)][0] = " "  
            vertical_check()
            continue
        if gameenddict[(int(xaxis), int(yaxis))][1] > 0:
            try: 
                while True:
                    if gamemap[yaxis][xaxis] != " " and gameenddict[(xaxis, yaxis)][0] != " ":   
                        gamemap[yaxis][xaxis],  gameenddict[(xaxis, yaxis)][0] = " ", " "
                        currentscore = currentscore+gameenddict[(xaxis, yaxis)][2]
                    allcoordinates.append((xaxis, yaxis))
                    if gameenddict[(xaxis, yaxis)][1] > 1:
                        fork = True
                        forkcoord.append(allcoordinates)
                        allcoordinates = []
                    neighbourdelete()
                    if gameenddict[(xaxis, yaxis)][1] > 0: 
                        returncount = 0
                        if yaxis-1 >= 0: 
                            if gamemap[yaxis-1][xaxis] == theball and gamemap[yaxis-1][xaxis] != " ":
                                yaxis = yaxis-1
                                continue    
                        if yaxis+1 != columnlength:
                            if gamemap[yaxis+1][xaxis] == theball and gamemap[yaxis+1][xaxis] != " ":
                                yaxis = yaxis+1
                                continue
                        if xaxis-1 >= 0:
                            if gamemap[yaxis][xaxis-1] == theball and gamemap[yaxis][xaxis-1] != " ":

                                xaxis = xaxis-1
                                continue
                        if xaxis+1 != rowlength:
                            if gamemap[yaxis][xaxis+1] == theball and gamemap[yaxis][xaxis+1] != " ":
                                xaxis = xaxis+1
                                continue
                    else:
                        if fork == False:   
                            returncoordinate = len(allcoordinates)-1
                        else:
                            if len(forkcoord)>0:
                                returncoordinate = len(forkcoord[-1])-1
                        while gameenddict[(xaxis, yaxis)][1] == 0:
                            if fork == True and len(forkcoord) == 0:
                                xaxis, yaxis = coordinates2[0], coordinates2[1]
                                break
                            if returncoordinate >= 0:
                                if fork == False:
                                    xaxis = allcoordinates[returncoordinate-1][0]
                                    yaxis = allcoordinates[returncoordinate-1][1]
                                    returncoordinate = returncoordinate-1
                                elif fork == True:
                                    if len(forkcoord)>0:
                                        xaxis = forkcoord[-1][-1][0]
                                        yaxis = forkcoord[-1][-1][1] 
                            if fork != False:
                                if len(forkcoord) > 0:
                                    forkcoord[-1].pop(-1)
                            if len(forkcoord) > 0:   
                                if len(forkcoord[-1]) == 0:
                                    forkcoord.pop(-1)
                            if xaxis == coordinates2[0] and yaxis == coordinates2[1]:
                                break
                        if xaxis == coordinates2[0] and yaxis == coordinates2[1] and gameenddict[(xaxis, yaxis)][1] == 0:
                            break
                        allcoordinates = []
                        returncount = returncount+1 
                gameendcheck()   
            except IndexError:
                print("Hey! Can you look here?")
            vertical_check()
        else:
            continue
    print("Game Over!")
except UnknownBallError:
    print("--------------------------------------------------")
    print("You might be mistaken in input brother. Sorry.")
    print("--------------------------------------------------")
except AssertionError:
    print("--------------------------------------------------")
    print("You didn't give me any input!")
    print("--------------------------------------------------")
except IndexError:
    print("--------------------------------------------------")
    print("The input file couldn't found!!!")
    print("--------------------------------------------------")
