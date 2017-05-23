import pandas as pd

if False:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })

    def add_one(x):
        return x + 1

    print df.applymap(add_one)

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 60:
        return 'D'
    else:
        return 'F'

def convert_grades(grades):
    return grades.applymap(convert_grade)

#print convert_grades(grades_df)

if False:
    def convert_grades_curve(exam_grades):
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        return pd.qcut(exam_grades,
                       [0, 0.1, 0.2, 0.5, 0.8, 1],
                       labels=['F', 'D', 'C', 'B', 'A'])

    print convert_grades_curve(grades_df['exam1'])

    print grades_df.apply(convert_grades_curve)

def stdColuna(coluna):
    return ( coluna - coluna.mean()) / coluna.std()

def stdGrades(df):
    return df.apply(stdColuna)

print stdGrades(grades_df)