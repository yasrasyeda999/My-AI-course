total_questions = float(input('enter the total number of questions '))
correct_questions = float(input('enter the correct number of questions '))
print(f'The total number of questions are {total_questions}')
print(f'The correct number of questions are {correct_questions}')
percentage = correct_questions/total_questions * 100
print(f'The percentage of correct questions is {percentage}')