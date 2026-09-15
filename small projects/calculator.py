# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:43:29 2026

@author: evafa
"""

#display a menu with options: add, subtract, multiply, divide, and exit.
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    #prompt the user to select an operation
    choice = input("Select an option 1-5: ")
    
    #If the user chooses to exit
    if choice == "5":
        print("Goodbye!")
        break
    
    #validate menu choice
    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please select a valid option.")
        continue
    
    #prompt the user to enter two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    
    #perform the selected operation and display the result.
    if choice == "1":
        result = num1 + num2
        print(result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print(result)
        
    elif choice == "4":
        
        #division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            
        else:
            result = num1 / num2
            print(result)
 