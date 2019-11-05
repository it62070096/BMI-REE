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

	print("Press 1 if you don't have any workout")
	print("Press 2 if you have a workout 1-3 times per week")
	print("Press 3 if you have a workout 3-5 times per week")
	print("Press 4 if you have a workout 6-7 times per week")
	print("Press 5 if you workout so hard everday")
	tdee = 0
	answer = input()
	if answer == "1":
		tdee = 1.2 * bmr
	elif answer == "2":
		tdee = 1.375 * bmr
	elif answer == "3":
		tdee = 1.55 * bmr
	elif answer == "4":
		tdee = 1.725 * bmr
	elif answer == "5":
		tdee = 1.9 * bmr
	else:
		print("Please answer the right choice 1,2,3,4 or 5")
		tdee()
	print("Your TDEE is %.2f" %tdee)
	
find_bmi():