age = int(raw_input("What's your age?"))
celsius = (age - 32) / 1.8
celsiusround = round(celsius, 2)

print "Temperature:", age, "Fahrenheit = ", celsiusround, " Celsius"