import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def uniqueEnrollmentStudent(enrollments):
    enrollment_students = set()
    for enr in enrollments:
        enrollment_students.add(enr['account_key'])
    return enrollment_students;

def uniqueEngagementStudent(daily_engagement):
    engagement_students = set()
    for daily in daily_engagement:
        engagement_students.add(daily['acct'])
    return engagement_students

def uniqueSubmissionStudent(project_submissions):
    submission = set()
    for sub in project_submissions:
        submission.add(sub['account_key'])
    return submission


enrollments = read_csv('../data/enrollments.csv')
daily_engagement = read_csv('../data/daily_engagement.csv')
project_submissions = read_csv('../data/project_submissions.csv')

enrollment_num_rows = len(enrollments)
enrollment_num_unique_students = len( uniqueEnrollmentStudent(enrollments) )

engagement_num_rows = len(daily_engagement)
engagement_num_unique_students = len( uniqueEngagementStudent(daily_engagement) );

submission_num_rows = len(project_submissions)
submission_num_unique_students = len( uniqueSubmissionStudent(project_submissions) )

print(enrollment_num_unique_students)
print(engagement_num_unique_students)
print(submission_num_unique_students)
