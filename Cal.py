import math

while True:
	"This for the condition of looping to be true each time"
	print("Choose the Math operator you wish to use\n\n 0 - Addition\n 1- Subtraction\n 2 - Multiplication\n 3 - Division\n 4 - Modulo\n 5 - Raising to a power\n 6 - Square root\n 7 - Logarithm\n 8 - Sine\n 9 - Cosine\n 10 - Tangent\n")
	
	operation = input("Your option from the menu : ")
	
	#Addition
	if operation == "0":
		var1 = float(input("Enter the value of x :"))
		var2 = float(input("Enter the value of y :"))
		
		print("\n The result of addition is " + str(var1 + var2) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
		
	#Subtraction
	elif operation == "1":
		var1 = float(input("Enter the value of x :"))
		var2 = float(input("Enter the value of y :"))
		
		print("\n The result of Subtraction is " + str(var1 - var2) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Multiplication
	elif operation == "2":
		var1 = float(input("Enter the value of x :"))
		var2 = float(input("Enter the value of y :"))
		
		print("\n The result of Multiplication is " + str(var1 * var2) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Division
	elif operation == "3":
		var1 = float(input("Enter the value of x :"))
		var2 = float(input("Enter the value of y :"))
		
		print("\n The result of division is " + str(var1 / var2) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Modulo
	elif operation == "4":
		var1 = float(input("Enter the value of x :"))
		var2 = float(input("Enter the value of y :"))
		
		print("\n The result of Modulo is " + str(var1 % var2) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Raising to a power
	elif operation == "5":
		var1 = float(input("Enter the value of base :"))
		var2 = float(input("Enter the value of power :"))
		
		print("\n The result is " + str(math.pow(var1,var2)) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Square root		
	elif operation == "6":
		var1 = float(input("Enter the value for which square root is required :"))
		
		print("\n The result is " + str(math.sqrt(var1)) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
	#Logarithm
	elif operation == "7":
		var1 = float(input("Enter the value for which you want Logarithm to the base 2 :"))
		
		print("\n The result is " + str(math.log(var1 ,2)) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Sine
	elif operation == "8":
		var1 = float(input("Enter the value (In degrees) for calculating the Sine :"))
		
		print("\n The result is " + str(math.sin(math.radians(var1))) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Cosine
	elif operation == "9":
		var1 = float(input("Enter the value (In degrees) for calculating the Cosine :"))
		
		print("\n The result is " + str(math.cos(math.radians(var1))) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
			
	#Tangent
	elif operation == "10":
		var1 = float(input("Enter the value (In degrees) for calculating the Tangent :"))
		
		print("\n The result is " + str(math.tan(math.radians(var1))) + "\n")
		
		#Going back to main menu
		back = input("\n Go back to main menu? (y/n) : ")	
		if back == "y":
			continue
		else:
			break
		
	#Invalid option
	else:
		print("Please enter a valid option")
		continue
		
#End of program.
