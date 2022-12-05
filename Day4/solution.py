with open('input.txt', 'r') as f:
    lines = f.readlines()

    total_overlaps = 0
    total_partial_overlaps = 0
    
    for line in lines:
        #strip line
        clean_line = line.strip()

        #first split on ,
        two_sets = clean_line.split(",")

        #make each set variable
        elf_one = two_sets[0]
        elf_two = two_sets[1]

        #split again to get 4 indivual numbers to compare
        elf_one_split = elf_one.split("-")
        elf_one_first_val = int(elf_one_split[0])
        elf_one_second_val = int(elf_one_split[1])

        elf_two_split = elf_two.split("-")
        elf_two_first_val = int(elf_two_split[0])
        elf_two_second_val = int(elf_two_split[1])

        #compare numbers to see if any overlaps

        if ((elf_one_first_val >= elf_two_first_val and elf_one_second_val <= elf_two_second_val) 
          or(elf_two_first_val >= elf_one_first_val and elf_two_second_val <= elf_one_second_val)) :
            total_overlaps += 1

        # part two , partials
        if ((elf_one_first_val >= elf_two_first_val and elf_one_second_val <= elf_two_second_val) 
          or(elf_two_first_val >= elf_one_first_val and elf_two_second_val <= elf_one_second_val)
          or(elf_two_first_val <= elf_one_second_val and elf_two_second_val >= elf_one_first_val)
          or(elf_two_first_val <= elf_one_second_val and elf_two_second_val >= elf_one_first_val)):
            total_partial_overlaps += 1
        
    print("The result for AoC day 4 part 1 is: " + str(total_overlaps))
    print("The result for AoC day 4 part 2 is: " + str(total_partial_overlaps))
 