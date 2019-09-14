import os
import random

import names


subjects = ['English', "French", "Science", "Music", "Art", "Biology",
            "Drama", "History", "PE", "Pyshics", "Geography", "Algebra"]


def generate_reports(num):
    assert type(num) == int, 'Please, introduce a number to generate reports.'

    for student_number in range(num):
        student_name = names.get_full_name()
        filename = student_name.lower().replace(' ', '_') + '_marks.txt'

        with open(filename, 'w') as f:
            random.shuffle(subjects)
            subjects_number = random.randint(8, 10)
            student_subjects = subjects[:subjects_number]

            subjects_and_marks = generate_subjects_and_marks(student_subjects)
            student_marks_report = generate_marks_report(subjects_and_marks)

            f.write(student_marks_report)


def delete_reports():
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.txt'):
            os.remove(filename)


def generate_subjects_and_marks(student_subjects):
    return {subject: round(random.uniform(0, 10), 1)
            for subject in student_subjects}


def generate_marks_report(subjects_and_marks):
    text = ''
    for key, value in subjects_and_marks.items():
        text += f'\t{key}: {value}\n'

    return text


if __name__ == '__main__':
    generate_reports(2)
    # delete_reports()
