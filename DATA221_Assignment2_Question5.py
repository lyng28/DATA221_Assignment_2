import pandas as pd

file = pd.read_csv('student.csv')

# Call a function and apply it to create a new column
def grade_band(grade):
    if grade <= 9:
        return 'Low'
    elif 10 < grade < 14:
        return 'Medium'
    else:
        return 'High'
file['grade_band'] = file['grade'].apply(grade_band)

# Create grouped summary
filtered_low_grade = file[file['grade_band'] == 'Low']
filtered_medium_grade = file[file['grade_band'] == 'Medium']
filtered_high_grade = file[file['grade_band'] == 'High']

# Generate summary table by create a list
summary_rows = [{'grade_band': 'Low',
                 'Number of students': len(filtered_low_grade),
                 'Average absences': filtered_low_grade['absences'].mean().round(2),
                 'Percentage of students with internet access': filtered_low_grade['internet'].mean().round(2) *100},
                 {'grade_band': 'Medium',
                  'Number of students': len(filtered_medium_grade),
                  'Average absences': filtered_medium_grade['absences'].mean().round(2),
                  'Percentage of students with internet access': filtered_medium_grade['internet'].mean().round(2) * 100},
                 {'grade_band': 'High',
                 'Number of students': len(filtered_high_grade),
                 'Average absences': filtered_high_grade['absences'].mean().round(2),
                 'Percentage of students with internet access': filtered_high_grade['internet'].mean().round(2) *100}
]

summary_table = pd.DataFrame(summary_rows)

summary_table.to_csv('student_bands.csv', index= False)
print(summary_table)







