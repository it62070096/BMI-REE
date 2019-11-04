def find_bmi():
    """Find BMi"""
    height = float(input("Enter your height : "))
    height = height/100
        #input height as centimeter
    weight = float(input("Enter your weight : "))
        #input as kilogram
    bmi = (weight / (height * height))
    print('Your BMI is %.2f' % bmi)

def tdee():
	print("")
	print("This is TDEE Calculater.")
	print("")
	gender = input("What is your gender Male or Female ")
	age = int(input("How old are you "))
	weight = float(input("Your weight is "))
	hight = float(input("Your hight is "))
	bmr = 0
	"""BMR CALCULATED"""
	if gender == "Male":
		bmr = 66 + (13.7 * weight) + (5 * hight) - (6.8 * age)
	elif gender == "Female":
		bmr = 665 + (9.6 * weight) + (1.8 * hight) - (4.7 * age)

find_bmi():