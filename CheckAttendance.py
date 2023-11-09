'''
Author: Hubert Waleńczak

Description:
This simple script compares students logged with a mobile app against a student group and outputs a file with the date that students were logged on. It relies on two essential CSV files: 'Students.csv,' which contains student names and a column with unique student numbers ('student_number'), and 'data.csv,' which stores data extracted from PowerBI.

Requirements:
- pandas
- 'Students.csv' file with students' information
- 'data.csv' file with data extracted from PowerBI

Operational Notes:
Ensure that both 'Students.csv' and 'data.csv' are present and correctly.

Example Usage:
python script_name.py
'''
import os
import pandas as pd

Attendance = pd.read_csv('data.csv')
Students = pd.read_csv('Students.csv')
Date = Attendance.iloc[0,0].split()
Present = Students.merge(Attendance, on='student_number', how='inner')
del Present['date']


if not os.path.exists('Attendance'):
    os.makedirs('Attendance')

Present.to_csv('Attendance/'+Date[0]+'.csv', sep=',', index=False)
