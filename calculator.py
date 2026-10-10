print("Mini Calculator")
name = input("Please enter your name: ")

# main loop
while(True):
    result = 0
    a = float(input("Enter First number: "))
    print("Chose a opration between: +,-,*,/,//,%,**")
    oper = input("Enter a operator: ")
    b = float(input("Enter Secound number: "))

    if(oper == '+'):
        result = a+b
    elif(oper == '-'):
        result = a-b
    elif(oper == '*'):
        result = a*b
    elif(oper == '/'):
        result = a/b
    elif(oper == '//'):
        result = a//b
    elif(oper == '%'):
        result = a%b
    elif(oper == '**'):
        result = a**b

    print(f"{name} your result: ",result)
    
