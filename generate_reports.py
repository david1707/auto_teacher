import os
import sys
import random
from datetime import date, timedelta

import names


subjects = ['English', "French", "Science", "Music", "Art", "Biology",
            "Drama", "History", "PE", "Pyshics", "Geography", "Algebra"]


def generate_reports(num):
    assert type(num) == int, 'Please, introduce a number to generate reports.'

    for i, student_number in enumerate(range(num)):
        # Generate values
        max_number_characters = len(str(num))
        student_name = names.get_full_name()
        student_name_to_file = student_name.lower().replace(' ', '_')
        filename = f'{str(i+1).zfill(max_number_characters)}_{student_name_to_file}_marks.txt'

        with open(filename, 'w') as f:

            # Randomize and pick between 8 and 10 subjects
            random.shuffle(subjects)
            subjects_number = random.randint(8, 10)
            student_subjects = subjects[:subjects_number]
            report_generation_date = date.today() - timedelta(days=random.randint(0, 7))

            # Generate a dictionary and then a string with the student subjects and their grade
            subjects_and_marks = generate_subjects_and_marks(student_subjects)
            student_marks_report = generate_marks_report(subjects_and_marks)

            # Create a .txt report
            report_text = f'Student name: {student_name}\n\n' + \
                f'Report generated on {report_generation_date}\n\n' + \
                'Student final marks:\n\n' + \
                f'{student_marks_report}'

            f.write(report_text)


def delete_reports():
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.txt'):
            os.remove(filename)


def generate_subjects_and_marks(student_subjects):
    return {subject: round(random.uniform(4, 10), 1)
            for subject in student_subjects}


def generate_marks_report(subjects_and_marks):
    text = ''
    for key, value in subjects_and_marks.items():
        text += f'\t{key}: {value}\n'

    return text


if __name__ == '__main__':
    try:
        action = sys.argv[1]
        value = int(sys.argv[2])
    except IndexError:
        pass

    if action == '-d':
        delete_reports()
    elif action == '-g':
        generate_reports(value)
    else:
        print('Action not recognized.')