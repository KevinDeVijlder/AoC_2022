def calculateValueOfFigure(figure):
    figurevalue=0
    if(figure == "A" or figure == "X"):
        figurevalue = 1
    elif(figure == "B" or figure == "Y"):
        figurevalue = 2
    else:
        figurevalue = 3
    return figurevalue

def determineWinner(figureOne, figureTwo):
    score=0
    if( (figureOne == "A" and figureTwo == "X" ) or (figureOne == "B" and figureTwo == "Y") or (figureOne=="C" and figureTwo=="Z") ):
        score = 3
    elif( (figureOne == "A" and figureTwo == "Z" ) or (figureOne == "B" and figureTwo == "X") or (figureOne=="C" and figureTwo=="Y") ):
        score = 0
    else:
        score = 6
    return score

def determineType(figureOne, figureTwo):
    newfigure = ""
    #Lose
    if(figureTwo == "X"):
        if(figureOne == "A"):
            newfigure="Z"
        if(figureOne == "B"):
            newfigure ="X"
        if(figureOne == "C"):
            newfigure = "Y"
    #Draw
    elif(figureTwo == "Y"):
        if(figureOne == "A"):
            newfigure="X"
        if(figureOne == "B"):
            newfigure ="Y"
        if(figureOne == "C"):
            newfigure = "Z"
    else:
        if(figureOne == "A"):
            newfigure="Y"
        if(figureOne == "B"):
            newfigure ="Z"
        if(figureOne == "C"):
            newfigure = "X"
    return newfigure

with open('input.txt', 'r') as f:
    lines = f.readlines()

    thislist = []
    value = 0
    for line in lines:
        input = line.split()
        figureOne = input[0]
        figureTwo = input[1]
        new_figureTwo = determineType(figureOne, figureTwo)
        value_second_figure = calculateValueOfFigure(new_figureTwo)
        value += value_second_figure  
        scoreOfGame = determineWinner(figureOne, new_figureTwo)
        print(scoreOfGame)
        value += scoreOfGame
    print(value)

