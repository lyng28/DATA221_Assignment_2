import pandas as pd

file = pd.read_csv('student.csv')

# Filter the original file
filtered_file = file.loc[(file['studytime'] >= 3) & (file['internet'] == 1) & (file['absences'] <= 5), :]

# Save the filtered data into a new csv file
filtered_file.to_csv('high_engagement.csv', index=False)

high_engagement_students = len(filtered_file) # Number of high engagement students
average_grade = filtered_file['grade'].mean().round(2) # Calculate the average grade of all students using mean()

print(f'The number of students are: ', high_engagement_students)
print(f'The average grade is: ', average_grade)