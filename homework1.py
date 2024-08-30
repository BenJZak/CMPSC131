#im not error checking right now lol

#Height explainer

height = input("Enter your height in inches: ")

print("You are", height, "inches tall!")

#celsius to fahrenheit converter

temp_celsius = input("Enter a temperature in Celsius: ")

fahrenheit = (9/5) * (float)(temp_celsius) + 32

print(temp_celsius, "degrees celsius is", fahrenheit, "degrees fahrenheit!")

#Compound interest calculator

annual_rate = input("Input your annual interest rate as a percentage: ")

annual_rate = float(annual_rate)/100 #to convert percent to decimal

P = 20000/((1+(annual_rate))**10)

P = round(P, 2) #round b/c you cant have .0000001 of a dollar

print("You will need to deposit", P, "dollars in order to achieve $20,000 in 10 years!")