# Create a simple calculator application which does read the parameters from the prompt
# and prints the result to the prompt.

# It should support the following operations:
# +, -, *, /, % and it should support two operands.

# The format of the expressions must be: {operation} {operand} {operand}.
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit


userinput = str(input("Please type in the expression: "))
userinput = userinput.split(" ")

result = 0
def calculator(userinput):

    if userinput[0] == '+':
         result = int(userinput[1]) + int(userinput[2])
         print(result)
    elif userinput[0] == '-':
        result = int(userinput[1]) - int(userinput[2])
        print(result)
    elif userinput[0] == '*':
        result = int(userinput[1]) * int(userinput[2])
        print(result)
    elif userinput[0] == '/':
        result = float(userinput[1]) / float(userinput[2])
        print(result)
    elif userinput[0] == '%':
        result = float(userinput[1]) % float(userinput[2])
        print(result)

calculator(userinput)
