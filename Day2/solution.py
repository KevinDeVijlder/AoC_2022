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



with open('input.txt', 'r') as f:
    lines = f.readlines()

    thislist = []
    value = 0
    for line in lines:
        input = line.split()
        figureOne = input[0]
        figureTwo = input[1]
        value_second_figure = calculateValueOfFigure(figureTwo)
        value += value_second_figure  
        scoreOfGame = determineWinner(figureOne, figureTwo)
        print(scoreOfGame)
        value += scoreOfGame
    print(value)

