def determine(line, buffersize):
      amount_of_characters = 0
      for element in range(0, len(line) - buffersize):
            input = line[element: element + buffersize]
            bufferset = set(input)
            if(len(bufferset) == buffersize):
                amount_of_characters += buffersize
                break
            else:
                amount_of_characters += 1
      return amount_of_characters

with open('input.txt', 'r') as f:
    lines = f.readlines()

    solution_one = 0
    solution_two = 0

    for line in lines:
        # challenge 1
        solution_one = determine(line, 4)    
        
        # Challenge 2
        solution_two = determine(line, 14)   

print("The result for AoC day 6 part 1 is: " + str(solution_one))
print("The result for AoC day 6 part 2 is: " + str(solution_two)) 
print(r"""     
     *
    ***
   *****
  *******
 *********
     * 
Merry Xmas!""")