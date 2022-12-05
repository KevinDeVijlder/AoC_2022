with open('input.txt', 'r') as f:
    lines = f.readlines()

    thislist = []
    value = 0
    for line in lines:
        if line.strip() == "":
            thislist.append(value)
            value=0
        else:
            value = value + int(line)

    # challenge 1
    max_index = max(thislist)

    # Challenge 2
    thislist.sort()
    top_three = (sum(thislist[-3:]))

print("The result for AoC day 1 part 1 is: " + str(max_index))
print("The result for AoC day 1 part 2 is: " + str(top_three)) 
print(r"""     
     *
    ***
   *****
  *******
 *********
     * 
Merry Xmas!""")