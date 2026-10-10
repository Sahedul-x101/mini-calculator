print("Mini Calculator")
name = input("Please enter your name: ")

# main loop
while(True):
    result = 0
    a = float(input("Enter First number: "))
    print("Chose a opration between: +,-,*,/,//,%,**")
    oper = input("Enter a operator: ")
    b = float(input("Enter Secound number: "))

    # addition
    if(oper == '+'):
        result = a+b
    # subtraction
    elif(oper == '-'):
        result = a-b
    # multiplication
    elif(oper == '*'):
        result = a*b
    # division
    elif(oper == '/'):
        result = a/b
    # Foor Division
    elif(oper == '//'):
        result = a//b
    # Modulus
    elif(oper == '%'):
        result = a%b
    # power
    elif(oper == '**'):
        result = a**b

    print(f"{name} your result: ",result)
    
