import names


def generate_reports(num):
    assert type(num) == int, 'Please, introduce a number to generate reports.'

    for student_number in range(num):

        student_name = names.get_full_name()
        filename = student_name.lower().replace(' ', '_') + '_marks.txt'
        print(filename)
        # with open(filename, 'w') as f:


if __name__ == '__main__':
    generate_reports(10)
