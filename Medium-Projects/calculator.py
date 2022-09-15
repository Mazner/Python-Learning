# Here i'm experiencing building a calculator with everything i've learned
# so far (variables, conditionals, loops)

# My background in C programing, made me go into search for creating functions, so I could
# Make the code a little bit more clear.

def sum(sum_list):
    list_size = len(sum_list)
    total_sum = 0
    for i in range(0,list_size):
        total_sum += sum_list[i]
    print(f"The sum of the elements equals: {total_sum}")

def sub(sub_list):
    list_size = len(sub_list)
    total_sub = 0
    for i in range(0,list_size):
        total_sub -= sub_list[i]
    print(f"The subtraction of the elements equals: {total_sub}")
    
def multiplication(mult_list):
    list_size = len(mult_list)
    total_mult = 1
    for i in range(0,list_size):
        total_mult *= mult_list[i]
    print(f"The multiplication of the elements equals: {total_mult}")

def division(division_list):
    list_size = len(division_list)
    total_div = 0
    for i in range(0,list_size):
        if i == 0:
            total_div = division_list[i]
        else:
            total_div /= division_list[i]
    print(f"The division of the elements equals: {total_div}")
    
        

op = 0
while op != 'e':
    print("Operations:\n 1 - Sum\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division")
    op = input('Tell me, what operation you need me to do?\nAlso, you can press \'e\' at anytime to exit\n> ')
    if op == '1':
        sum_list = []
        sum_size = int(input("How many numbers will I sum?\n> "))
        i = 0
        while i < sum_size:
            n = int(input("> "))
            sum_list.append(n)
            i += 1
        sum(sum_list)
    
    if op == '2':
        sub_list = []
        sub_size = int(input("How many numbers will I subtract?\n> "))
        i = 0
        while i < sub_size:
            n = int(input("> "))
            sub_list.append(n)
            i += 1
        sub(sub_list)
    
    if op == '3':
        mult_list = []
        mult_size = int(input("How many numbers will I multiply?\n> "))
        i = 0
        while i < mult_size:
            n = int(input("> "))
            mult_list.append(n)
            i += 1
        multiplication(mult_list)

    if op == '4':
        div_list = []
        div_size = int(input("How many numbers will I divide?\n> "))
        i = 0
        while i < div_size:
            n = int(input("> "))
            if n == 0:
                print("Cannot divide by zero!!")
                i += 1
            else:
                div_list.append(n)
                i += 1
        division(div_list)

        
print("Exiting program...")



