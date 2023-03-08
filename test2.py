result = None
operand = None
operator = None
wait_for_number = True

result = float()
while True:
    operand = input("input number: ")
    if operand in ('+','-','*','/','='):
        print(f"{operand} is not a number. Try again")
        continue
    else:
        operand = float(operand)
        while True:
            operator = input()
            if operator not in ('+','-','*','/','='):
                print(f"{operator} is not a operator. Try again")
                continue
            else:
                break
    if operator == '+':
        result = float(operand) + float(operand)
    elif operator == '-':
        result = float(operand) - float(operand)
    elif operator == '*':
        result = float(operand) * float(operand)
    elif operator == '/':
        

        try:
            result = float(operand) / float(operand)              
        except ZeroDivisionError:
            print("dilenia na 0 ")
    elif operator == '=':
          print(f"Result: {result}")
          break