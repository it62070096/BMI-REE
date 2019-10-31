def find_bmi():
    """Find BMi"""
    height = float(input("Enter your height : "))
    height = height/100
        #input height as centimeter
    weight = float(input("Enter your weight : "))
        #input as kilogram
    bmi = (weight / (height * height))
    print('Your BMI is %.2f' % bmi)

find_bmi():