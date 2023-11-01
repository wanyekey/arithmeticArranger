#this is an arithmetic arranger practically
#this function can arrange a max of five arithmetics that only deal with addition and subtraction

'''
the output should be as follows:
  1200     300      40000       11
+   20   -   5    -  1900    + 999
 -----   -----     ------    -----
  1200     295      38100     1010

'''
arithmetic_list = ["1200 + 20", "300 - 5", "4000000 - 11900", "564 + 789", "1000000 - 2", "11 - 10"]
signs = []
longests = []

# def get_input():
#     n = input("How many operations do you want to carry out: ")
#     print("Enter the operations\n")
#     for item in range(int(n)):
#         op = input('')
#         arithmetic_list.append(op)


def get_oper_index(element):
    if '+' in element:
        oper_index = element.index('+')
        signs.append('+')
    elif '-' in element:
        oper_index = element.index('-')
        signs.append('-')
    else:
        print("Invalid operation!")
    return oper_index

def get_first_row_components(element):#returns a list of elements to be displayed in the first row
    components = [item[:get_oper_index(item)].strip() for item in arithmetic_list]
    return components

def get_second_row_components(element):#returns a list of elements to be displayed in the second row
    components = [item[get_oper_index(item) + 1:].strip() for item in arithmetic_list]
    return components

def get_spacing(): #returns number of whitespace required with reference to the first rows elements
    zipped_rows = zip(get_first_row_components(arithmetic_list), get_second_row_components(arithmetic_list))
    spaces = [len(i) - len(v) for i, v in zipped_rows]
    return spaces

for i, v in zip(get_first_row_components(arithmetic_list), get_second_row_components(arithmetic_list)):
    if len(i) >= len(v):
        longests.append(len(i))
    elif len(v) > len(i):
        longests.append(len(v))

def map_spaces():
    spa = [space for space in get_spacing()]
    new_list, new_result, completed = [], [], []
    i = 0
    for space in get_spacing():
        if space > 0:
            new_list.append(get_second_row_components(arithmetic_list)[i])
        elif space < 0:
            new_list.append(get_first_row_components(arithmetic_list)[i])
            space = space * -1
        else:
            new_list.append(get_first_row_components(arithmetic_list)[i])      
        new_result.append(space * " ")
        i += 1
    last = list(zip(new_result, new_list)) 

    for i, v in last:
        new_tuple = i + v
        completed.append(new_tuple)
    return completed


def replace_and_display_values(list1, list2, replacers_list):
    for item in replacers_list:
        if item.strip() in list1:
            list1[list1.index(item.strip())] = item
        elif item.strip() in list2:
            list2[list2.index(item.strip())] = item
    for x in list1:
        print(f"  {x}", end='\t')
    print()
    
    for y in list2:
        print(f"{signs[list2.index(y)]} {y}", end='\t')
    print()
    
    for k in longests:
        print(((k + 1)*'-') + '-', end='\t')
    return "\t"


def display_answers():
    answers = []
    for i, operation in enumerate(arithmetic_list):
        if "-" in operation:
            answer = int(get_first_row_components(arithmetic_list)[i]) - int(get_second_row_components(arithmetic_list)[i])
        elif "+" in operation:
            answer = int(get_first_row_components(arithmetic_list)[i]) + int(get_second_row_components(arithmetic_list)[i])
        answers.append(answer)
        
    for ans in answers:
        if len(str(ans)) == longests[answers.index(ans)]:
            print(f"  {ans}", end='\t')
        elif len(str(ans)) < longests[answers.index(ans)]:
            print(f"   {ans}", end='\t')
        else:
            print(f" {ans}", end='\t')

    return '\t' 

list_a = get_first_row_components(arithmetic_list)
list_b = get_second_row_components(arithmetic_list)
replacers = map_spaces()

print(replace_and_display_values(list_a, list_b, replacers))
print(display_answers())


        