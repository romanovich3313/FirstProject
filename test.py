

while True:
        # operand = float(input('Введите первое число: '))
        # operator = input('Введите операцию: ')
        # operand2 = float(input('Введите второе число: '))
        # ravno = input('>>>: ')
        try:
            operand = float(input('Введите первое число: '))
            operator = input('Введите операцию: ')
            operand2 = float(input('Введите второе число: '))
            ravno = input('>>>: ')
            
            if operator == '+':
                c = operand + operand2
                print(c) if ravno == "="  else print('Знак = не найден')           

                continue
                         
            elif operator == '-':
                c = operand - operand2
                print(c)
                continue
            elif operator == '*':
                c = operand * operand2
                print(c)
                continue
            elif operator == '/':
                c = operand / operand2
                print(c)
                continue
            else:
                print (f"{operator} Оператор не определен")

        except NameError:
              print(f"{operand} Первое число неверное ")
        except TypeError:
              print(f"{operator} Вы не ввели символ operator ")
        
        except ValueError:
              print(f"{operand2} Второе число неверное ")
        
        finally:
            print("Попробуй еще раз ")        