print("""      Exam grade calculator
  Test out the system to see how well you did!""")
print('It can be used by anyone to know their scores')
print('We may start Now')
print()

user_name = input('What is your name? ')
print('Welcome to the test', user_name, 'we are happy to see you')
year_of_test = int(input('What was the year of the test? '))
name_of_institution = input('Name of your institution:')
print(name_of_institution, 'That is a great institution, you went to')
name_of_exam = input('Name of exam: ')
print('We are about to find about the score of your', name_of_exam, 'you did in', year_of_test)
units_or_subjects = int(input('How many units or subjects did you take? '))
print('You took', units_or_subjects, 'units or subjects')
print()
total_score = int(input('What was the total score of the exam? '))
input_your_score = int(input('What was your score? '))
if input_your_score == 90 and input_your_score > 90:
  print(user_name,'You got A+ in', name_of_exam, 'exam you did in', year_of_test)
elif input_your_score == 80 and input_your_score <= 89:
   print(user_name,'You got A in', name_of_exam, 'exam you did in', year_of_test)
elif input_your_score == 70 and input_your_score <= 79:
   print(user_name,'You got B in', name_of_exam, 'exam you did in', year_of_test)
elif input_your_score == 60 and input_your_score <= 69:
   print(user_name,'You got C in', name_of_exam, 'exam you did in', year_of_test)
elif input_your_score == 50 and input_your_score <= 59:
   print(user_name,'You got D in', name_of_exam, 'exam you did in', year_of_test)
elif input_your_score == 40 and input_your_score <= 49:
   print(user_name,'You got U in', name_of_exam, 'exam you did in', year_of_test)
else:
  print('You had a bad experieance with the exams')
print()
percentage_score = round(float(input_your_score / total_score) * 100, 2)
print(user_name, 'You got', percentage_score,'% ','in', name_of_exam, 'exam you did in', year_of_test)

print('Congrajulations on your exams and the success ahead of you')