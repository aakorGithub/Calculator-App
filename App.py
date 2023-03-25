# This is my Python App Calculator!

from tkinter import*
import math

root =Tk()
blank_space =  " "
root.title (50 * blank_space + "Vs code Calculator")
root.resizable(width =FALSE, height = False)
root.geometry("438x573+460+40")

coverFrame = Frame (root, bd =20, pady=2, relief = RIDGE)
coverFrame.grid()

root.mainloop()

from ast import Add
from asyncio.subprocess import SubprocessStreamProtocol
from audioop import add

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide


print ("Select an operation to perform:")
print ("1. Add")
print ("2. Sunbtract")
print ("3. Multiply")
print ("4. Divide")

operation = input ()

if operation == "1":

    num1 = input ("Enter first number:")
    num2 = input ("Enter second numbet: ")
    print ("The sum is  " + str(int(num1) + int (num2)))

elif operation == "2":
   
    num1 = input ("Enter first number:")
    num2 = input ("Enter second numbet: ")
    print ("The difference is  " + str(int(num1) - int (num2)))

elif operation == "3":

    num1 = input ("Enter first number:")
    num2 = input ("Enter second numbet: ")
    print("The product is  " + str(int(num1) * int (num2)))
   
elif operation == "4":
    num1 = input("Enter first number:  ")
    num2 = input("Enter second numbet:   ")
    print ("The result is  " + str(int(num1) / int (num2)))
else:
     print("Invalid Entry")   