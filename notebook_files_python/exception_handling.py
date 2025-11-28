

# Exception Handling
# ------------------

# History of Exception Handling


# NOTE:
# -----
# --> After 1990's the applications that are developed are almost web based applications as 
#   well as client server application.
# --> So if any programming language is used to develop these
#   application , then it should support Exception Handling


# Types of Error in python :

# In any programming language there are 2 types of errors

# 1. Syntax Errors / compilation error
# 2. Runtime Errors / Exception


# Syntax Errors:
# -----------------
# -->The errors which occurs because of invalid syntax are called
#   syntax errors.
# -->In python Pythoncompiler is responsible for syntax error


# # Examples:cls
# print('Hello world')
# name = "mahesh"
# if name == "mahesh":
#     print("Hello world")

# print("start")

# 2.Runtime Errors /Exception

# -->While executing the program if something goes wrong because of end
# user input or programming logic or memory problems .... then we will lead to Runtime Errors.

# -->Unwanted/Unexpected event that occurs during Executiontime/Runtime
# which leads to abnormal termination is referred as RuntimeError/Exception
# -->Some of the Exceptions are ZeroDivisionError, TypeError, ValueError,
# FileNotFoundError, EOFError


# Termination of the program:
# ---------------------------
# 1.Abnormal Termination/Non-Graceful Termination
# 2.Normal Termination/Graceful termination


# 1.Abnormal Termination/Non-Graceful Termination :

# example:

# num1 = int(input("Please enter the numerator: "))
# num2 = int(input("Please enter the denominator: "))
# print('result = ',num1/num2)

# ZeroDivisionError
# ----------------------

# --> In the above example programmer has not handled the exception
# so PVM handled the exception

# --> Then the Exception Object after getting the reason it will
# abnormally terminates from the program by printing the Exception information on the console


# 2.Normal Termination/Graceful termination:

# Syntax to Handle exception in python:
# ------------------------------------
# try:
# ---- (Risky Code)
# ----
# except:
# ---- (Handling the exception code)
# ----


# Exception handling using single except block:
# ---------------------------------------------

# try:
#     num1 = int(input("Please enter the numerator: "))
#     num2 = int(input("Please enter the denominator: "))
#     print('result = ',num1/num2)
# except (ZeroDivisionError,ValueError):
#     print("inside ZeroDivisionError")


# Example


# try:
#     num1 = int(input("Please enter the numerator: "))
#     num2 = int(input("Please enter the denominator: "))
#     print('result = ',num1/num2)
# except (ZeroDivisionError, ValueError):
#     print("inside ZeroDivisionError")

# NOTE:
# -----
# --> In the above example a single except block is used so apart
# from the given exception if
# any other exception is occured then PVM has to handle the exception
# --> So inorder to overcome this disadvantage we have to make use of
# multiple except block


# Exception handling using Multiple except block:
# ---------------------------------------------

# example

# print("start")

# try:
#     num1 = int(input("Please enter the numerator: "))
#     num2 = int(input("Please enter the denominator: "))
#     print('result = ',num1/num2)
# except ZeroDivisionError:
#     print("inside ZeroDivisionError")
# except ValueError:
#     print("Inside Value Error")

# print("end" )

# NOTE:
# -----
# -->If there are multiple except blocks in the program then PVM will
# search for the Exception name from top to bottom untill the matched Exception is avilable


# Handling multiple Exceptions using Single except block:/Grouping Multiple
# Exceptions using single except block


# print('Entering the main () code')
# print('Connection is established')
# try:
#   num1=int(input('Enter the Numerator:\t'))
#   num2=int(input('Enter the Denominator:\t'))
#   result=num1/num2
#   print(result)
# except (ZeroDivisionError,ValueError,NameError) as e:
#   print('The cause of the exception : ',e)
#   print('Connection is terminated')


# Python's Exception Hierarchy:

# Base Exception

# --> SystemExit
# --> genaratorExit
# -->KeyboardInterrupt
# --> Exception
#   -->AttributeError
#   -->ArithematicError---->ZeroDivisionError
#   -->EOFError         |-->FloatingPointError
#   -->NameError        |-->OverflowError
#   -->LockupError---->IndexError , KeyError  
#   -->OSError-------->FilenotFoundError
#   -->TypeError   |-->InterruptedError
#   -->ValueError  |-->PermissionError
#                  |-->TimeoutError

# NOTE:
# -----
# --> Every Exception in Python is a class.
# --> All exception classes are child classes of BaseException.i.e
#   every exception class extends BaseException either directly or
#   indirectly.Hence BaseException acts as root for Python Exception Hierarchy.


# Handling the Exception using Exception class:

print('Entering the main () code')
print('Connection is established')
try:
  num1=int(input('Enter the Numerator:\t'))
  num2=int(input('Enter the Denominator:\t'))
  result=num1/num2
  print(result)
except Exception as e:
  print('The cause of the exception : ',e)
  print('Connection is terminated')
  print('Exiting from the main () code')


# Default Except Block:

# print('Entering the main () code')
# print('Connection is established')
# try:
#   num1=int(input('Enter the Numerator:\t'))
#   num2=int(input('Enter the Denominator:\t'))
#   result=num1/num2
#   print(result)
# except ZeroDivisionError:
#   print('Please enter the non-zero Denominator')
# except :             #default except block
#   print('Please provide the proper input')
#   print('Connection is terminated')
#   print('Exiting from the main () code')


# else block in Exception Handling:

# print('Entering the main () code')
# print('Connection is established')
# try:
#   num1=int(input('Enter the Numerator:\t'))
#   num2=int(input('Enter the Denominator:\t'))
#   result=num1/num2
#   print(result)

# except Exception as e:
#     # num2=float(input('Enter the Denominator:\t')) 
#     # result=num1/num2
#     # print(result)
#     print('The cause of the exception : ',e)
#     print('Connection is terminated')
# else:
#     print("im inside the else block")

# print('Exiting from the main () code')


# Standard way of writing Python Programs:
# ----------------------------------------

# try:
#   Risky code
# except:
#   Handling code for Exceptions
# else:
#   No exception code
# finally:
#   Cleanup code/resource termination code

# print('Entering the main () code')
print('Connection is established')
# try:
#   num1=int(input('Enter the Numerator:\t'))
#   num2=int(input('Enter the Denominator:\t'))
#   result=num1/num2
#   print(result)  
# except Exception as e:
#     print('The cause of the exception : ',e)
#     print('Connection is terminated')
# else: 
#     print("im inside the else block")
# finally:
#     print("im inside the finally block")
#     print('Exiting from the main () code')

# finally block in Exception handling
# -------------------------------------
# --> finally block is used to write the resource termination code
# --> In the above example if we don't use finally block then the
# connections will not be terminated


# raise keyword in python:
# ------------------------

# -->raise keyword is used to raise the exception at any given line
# of the program


# print('Entering the main () code')
# print('Connection is established')
# try:
#   num1=int(input('Enter the Numerator:\t'))
#   num2=int(input('Enter the Denominator:\t'))
#   result=num1/num2
#   print(result)
# except Exception as e:
#     raise Exception
#     print(result)
#     # print('The cause of the exception : ',e)
#     print('Connection is terminated')
# else:
#     print("im inside the else block")

# print('Exiting from the main () code')


# WAP to collect the input from the user(odd numbers) and convert it to
# even number , if the user tries to enter even number initially then raise
# a proper exception

# 1 + 1 --> 2

# class wrongnumber(Exception):
#     def __init__(self, msg):
#         self.msg = msg

# num = int(input("Enter the odd number: \t"))

# if num%2 == 0:
#     raise wrongnumber("stupid enter the odd number...!")

# print(f"The even number for given odd number is {num+1}")


# https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y

# https://www.youtube.com/watch?v=Iw2H3WT-c1s