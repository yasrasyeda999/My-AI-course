def total_salary(basic_salary,hra,da):
    return basic_salary + hra +da
basic_salary = float(input('enter the basic salary in (PKR)  '))
hra = 0.2 * basic_salary
da = 0.15 * basic_salary
total_salary = basic_salary + hra + da
print(f'{total_salary}')    
print(f'{hra}')
print(f'{da}')


