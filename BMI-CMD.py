print("***********************")
print("   ENTER INFORMATION   ")
print("***********************")
gender = input("What is your gender Male or Female : ").lower()
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))
weight = float(input("Enter your weight : "))
print()

def find_bmi():
    """Find BMi"""
    print("**********************")
    print("This is BMI Calculater")
    print("**********************")
    heights = height
    heights = heights/100
        #input heights as centimeter
    weights = weight
        #input as kilogram
    bmi = (weights / (heights * heights))
    print('Your BMI is %.2f' % bmi)

    if bmi > 0 and bmi <= 18.5:
        print('Your weights status is Underweights')

    elif bmi > 18.5 and bmi <= 23:
        print('Your weights status is Normal weights')

    elif bmi > 23 and bmi <= 24.9:
        print('Your weights status is Overweights')

    elif bmi > 24.9 and bmi <= 30:
        print('Your weights status is Obese')

    else:
        print('There is an error with you input')
        print('Please check you have entered whole numbers\n'
              'and decimals where asked.')

def find_tdee():
    print("***********************")
    print("This is TDEE Calculater")
    print("***********************")
    genders = gender
    ages = age
    weights = weight
    heights = height
    bmr = 0
    """BMR CALCULATED"""
    if "Male" in genders:
        bmr = 66 + (13.7 * weights) + (5 * heights) - (6.8 * ages)
    elif "Female" in genders:
        bmr = 665 + (9.6 * weights) + (1.8 * heights) - (4.7 * ages)

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


def find_ree():
    """REE (Resting Energy Expenditure)"""
    print("**********************")
    print("This is REE Calculater")
    print("**********************")
    genders = gender
    ages = age
    weights = weight
    heights = height
    ree = 0
    genders_1 = genders.title()

    if "Male" in genders_1:
        ree = (10 * weights) + (6.25 * heights) - (5 * ages) + 5
        print("%s %.2f Kilocalorie"%(genders_1, ree))

    elif "Female" in genders_1:
        ree = (10 * weights) + (6.25 * heights) - (5 * ages) - 161
        print("%s %.2f kilocalorie"%(genders_1, ree))

if gender == "male" or gender == "floatemale":
    print("*********************")
    print("    MENU FUNCTION    ")
    print("*********************")
    print("Number #1 = BMI Calculater\nNumber #2 = TDEE Calculater\nNumber #3 = REE Calculater\nNumber #0 = Exit")
    number = int(input("Please select number : "))
    if number == 1:
         find_bmi()
    elif number == 2:
        find_tdee()
    elif number == 3:
        find_ree()
    elif number == 0:
        print("Exit...")
        print("Good Bye~")
    else:
        print()
        print("Error : Please enter number 1 - 3")
        print()
else:
    print()
    print("Error : Please enter Male or Female.")
    print()
