con = raw_input("Enter A if you want to convert fahreheit to celsius \nEnter B to convert celsius to fahrenheit\nEnter:").upper()

if con == "A":
   fahrenheit = float(raw_input("Enter a temperature in celsius : "))
   fahrenheit = 9.0/5.0 * fahrenheit + 32
   print "Fahrenheit : " + str(fahrenheit)
   
elif con == "B":
   celsius = float(raw_input("Enter a temperature in fahrenheit : "))
   celsius = (celsius - 32) * 5.0/9.0
   print "Celsius : " + str(celsius)
   
else:
   print "You did not choose A or B"
