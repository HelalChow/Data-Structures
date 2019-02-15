from ADT import ArrayStack


def postfix_helper(lst_exp):
    stack = ArrayStack.ArrayStack()
    operations = "+-*/"
    for i in lst_exp:
        if i not in operations:
            stack.push(i)
        else:
            second = int(stack.pop())
            first = int(stack.pop())
            if i == "+":
                stack.push(first + second)
            elif i == "-":
                stack.push(first - second)
            elif i == "*":
                stack.push(first * second)
            elif i == "/":
                stack.push(first / second)
    return stack.pop()


def postfix_calculator():
    seen_done = False
    variables_dict = {}
    operations = "+-*/"
    while seen_done == False:
        expression = input("--> ")
        if expression == "done()":
            seen_done = True
        elif len(expression) == 1 and expression[0].isdigit() == False:
            print(variables_dict[expression])
        else:
            lst_exp = expression.split(" ")
            if len(lst_exp) == 1 or lst_exp[1] != '=':
                for i in range(len(lst_exp)-1):
                    if lst_exp[i].isdigit() == False and lst_exp[i] not in operations:
                        lst_exp[i] = str(variables_dict[lst_exp[i]])
                print(postfix_helper(lst_exp))
            elif lst_exp[1] == '=':
                for i in range(2, len(lst_exp)):
                    if lst_exp[i].isdigit() == False and lst_exp[i] not in operations:
                        lst_exp[i] = str(variables_dict[lst_exp[i]])
                variables_dict[lst_exp[0]] = postfix_helper(lst_exp[2:])
                print(lst_exp[0])

postfix_calculator()
