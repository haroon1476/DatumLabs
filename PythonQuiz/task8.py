
def checkIfValidString(inputString):
    stack = []

    status = True
    for letter in inputString:
        if(letter == '{' or letter == '[' or letter == '('):
        # pushing in stack in that case
            stack.append(letter)

        if(letter == ')'):
            char = stack.pop()
            if(char !=  '('):
                status = False
                break

        if(letter == ']'):
            char = stack.pop()
            if(char !=  '['):
                status = False
                break


        if(letter == '}'):
            char = stack.pop()
            if(char !=  '{'):
                status = False
                break

    return status


print(checkIfValidString("{[()]}"))
print(checkIfValidString("([)")) 