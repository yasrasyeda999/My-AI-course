def calculate_BMI(weight,height):
    return weight/(height ** 2)
weight = float(input('enter the weight  '))
height = float(input('enter the height '))
calculate_BMI = weight/(height**2)
print(f'The BMI is {calculate_BMI} ') 