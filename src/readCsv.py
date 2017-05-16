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

def enrollmentNoEngagement(enrollments, uniqueEngagementStudent):
    enrollmentNoEngagement = list()
    for enr in enrollments:
        student = enr['account_key']
        if student not in uniqueEngagementStudent \
            and enr['join_date'] != enr['cancel_date']:
            enrollmentNoEngagement.append(enr)
    return enrollmentNoEngagement




enrollments         = read_csv('../data/enrollments.csv')
daily_engagement    = read_csv('../data/daily_engagement.csv')
project_submissions = read_csv('../data/project_submissions.csv')


uniqueEnrollmentStudents = uniqueEnrollmentStudent(enrollments)
uniqueEngagementStudent  = uniqueEngagementStudent(daily_engagement)
uniqueSubmissionStudent  = uniqueSubmissionStudent(project_submissions)
enrollmentNoEngagement = enrollmentNoEngagement(enrollments, uniqueEngagementStudent)

print(len(enrollments))
