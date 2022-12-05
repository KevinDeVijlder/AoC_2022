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
    total_part_one = 0
    total_part_two = 0
    for line in lines:
        # challenge 1
        input = line.split()
        figureOne = input[0]
        figureTwo = input[1]
        value_second_figure = calculateValueOfFigure(figureTwo)
        total_part_one += value_second_figure  
        scoreOfGame = determineWinner(figureOne, figureTwo)
        total_part_one += scoreOfGame

        # challenge 2
        new_figureTwo = determineType(figureOne, figureTwo)
        value_second_figure = calculateValueOfFigure(new_figureTwo)
        total_part_two += value_second_figure  
        scoreOfGame = determineWinner(figureOne, new_figureTwo)
        total_part_two += scoreOfGame

print("The result for AoC day 2 part 1 is: " + str(total_part_one))
print("The result for AoC day 2 part 2 is: " + str(total_part_two)) 
print(r"""     
     *
    ***
   *****
  *******
 *********
     * 
Merry Xmas!""")
