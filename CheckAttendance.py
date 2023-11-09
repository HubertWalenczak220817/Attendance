'''
Author: Hubert Waleńczak
Simple script that compares students logged with app and student group.
Outputs a file with the date that students were logged on.
Requirenments:
- pandas
- CSV file named 'Students.csv' with students names and column with student numbers named 'student_number'
- CSV file named 'data.csv' with data extracted from powerBI
'''

import pandas as pd
Attendance = pd.read_csv('data.csv')
Students = pd.read_csv('Students.csv')
Date = Attendance.iloc[0,0].split()
Present = Students.merge(Attendance, on='student_number', how='inner')
del Present['date']
Present.to_csv('Attendance'+Date[0]+'.csv', sep=',', index=False)
