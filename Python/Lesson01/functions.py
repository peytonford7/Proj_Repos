def hello_world():
    print("Hello world!")

hello_world()

def sum(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum(2, 3)
print(total)

