num1 = input ("enter the first number:")
num2 =input ("enter the second number:")
opr = input ("enter your operator:")


if opr == '+':
    print("the sum of two numbers is:",int(num1)+int(num2))

elif opr == '-':
    print("the sub of two numbers is:",int(num1)-int(num2))

elif opr == '*':
    print("the product of two numbers is:",int(num1)*int(num2))

elif opr == '/':
    print("the division of two numbers is:",int(num1)/int(num2))

else:
    print ("invalid response!")