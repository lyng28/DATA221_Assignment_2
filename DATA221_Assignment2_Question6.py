import pandas as pd

file = pd.read_csv('crime.csv')

# Call a function and create a new column by applying rule
def risk(violent_crime):
    if violent_crime >= 0.50:
        return 'HighCrime'
    else:
        return 'LowCrime'
file['risk'] = file['ViolentCrimesPerPop'].apply(risk)

# Filter by crime group
high_crime = file[file['risk'] == 'HighCrime']
low_crime = file[file['risk'] == 'LowCrime']

print(f'The average Unemployment rate for High Crime group is: ', high_crime['PctUnemployed'].mean().round(2))
print(f'The average Unemployment rate for Low Crime group is: ', low_crime['PctUnemployed'].mean().round(2))


