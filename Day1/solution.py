with open('input.txt', 'r') as f:
    lines = f.readlines()

    thislist = []
    value = 0
    for line in lines:
        if line.strip() == "":
            print('The line is empty')
            thislist.append(value)
            value=0
        else:
            print('The line is NOT empty')
            value = value + int(line)

# challenge 1
    print(thislist)
    max_index = max(thislist)
    print(max_index)

    print("--------------------------------------------------")

    # Challenge 2
    thislist.sort()
    print(thislist)
    print((sum(thislist[-3:])))