import pandas as pd

enrollments         = pd.read_csv('../data/enrollments.csv')

students = enrollments['account_key'].unique();
for student in students:
    print(student)

daily_engagement    = pd.read_csv('../data/daily_engagement.csv')

print( len(daily_engagement['acct'].unique()) )

project_submissions = pd.read_csv('../data/project_submissions.csv')
