#!/usr/local/bin/python3
import pandas as pd
import sys

number_of_args = len(sys.argv)
if number_of_args != 2:
    print('Error: One argument required (csv filename)')
    sys.exit()

df = pd.read_csv(sys.argv[1])
column = df['Severity']

def get_numbers(severity_level):
    global df
    global column
    non_resolved = df.query('Severity=="'+severity_level+'"')['Resolved']
    repeated = df.query('Severity=="'+severity_level+'"')['Repeated']
    print('*** ' + severity_level +  ' ***')

    try:
        print('Total number of ' + severity_level + ' level incidents:',column.value_counts()[severity_level])
    except KeyError:
        print('Total number of ' + severity_level + ' level incidents: 0 (please double check to be sure)')

    try:
        print('Non-resolved ' + severity_level + ' level incidents:',non_resolved.value_counts()['No'])
    except KeyError:
        print('Non-resolved ' + severity_level + ' level incidents: 0 (please double check to be sure)')  
    
    try:
        print('Repeated ' + severity_level + ' level incidents:',repeated.value_counts()['Yes'])
    except KeyError:
        print('Repeated ' + severity_level + ' level incidents: 0 (please double check to be sure)')
    print('\n')

severities = ['Information', 'Warning', 'Average', 'High', 'Disaster']
for severity in severities:
    get_numbers(severity)

total_incidents = len(df.axes[0]) - 1
resolved = df['Resolved'].value_counts()['Yes']
repeated = df['Repeated'].value_counts()['Yes']
print('\n')
print('Total number of incidents:', total_incidents)
print('Percentage of resolved incidents:', str((resolved/total_incidents)*100)+'%')
print('Percentage of repeated incidents:', str((repeated/total_incidents)*100)+'%')