In Python, input and output operations are fundamental for program interaction. 
Input:
The input() function is used to obtain data from the user via the console. 
Python

name = input("Enter your name: ")
print("Hello,", name)
The input() function pauses program execution and waits for the user to type something and press Enter.
The optional argument within the parentheses is a prompt string displayed to the user.
The data entered by the user is returned as a string. If numerical input is required, it must be explicitly converted using functions like int() or float(). 
Output:
The print() function is used to display data to the console. 
Python

age = 30
print("Your age is:", age)
print("This is a multi-line", "output.")
The print() function takes one or more arguments, which can be variables, literals, or expressions.
Arguments are typically separated by a space by default when printed.
The print() function automatically converts non-string arguments to their string representation before displaying them.
Output can be formatted using f-strings (formatted string literals) or the str.format() method for more control over presentation.
Example of Input and Output with Type Conversion:
Python

num_str = input("Enter a number: ")
num_int = int(num_str)  # Convert string input to an integer
print("You entered:", num_int)
print("Data type of num_int:", type(num_int))
