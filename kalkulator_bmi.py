weight = float(input("What is you current weight? :"))
height = float(input("What is your height? :"))


def count(weight,height):

    BMI = weight/(height ** 2)

    if BMI < 18.5:
            print("You are underweight")
    elif BMI > 19 and BMI < 24.9:
        print("You'r weight in correnct!")
    elif BMI > 25 and BMI < 29.9:
        print("You are overweight")
    elif BMI > 30:
        print("You'r obes")
    else:
        print("weight out of range!")
       
    print("You'r BMI score is:",round(BMI,2))

    
count(weight,height)



