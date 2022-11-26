def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x,y):
   return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True :
    # take input from the user ,to run infinte time until it breaks
    cho = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if cho in ('1', '2', '3', '4'):#in operator checks whether choice is present in the given data
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if cho == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif cho == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif cho == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif cho == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        dj = input("Let's do next calculation? (yes/no): ")
        if dj == "no":
          break
    
    else:
        print("Invalid Input")


