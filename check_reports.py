import os
import shutil
import sys


passed_reports_folder = 'students_passed'
failed_reports_folder = 'students_failed'

compression_type = 'zip'


def process_reports():
	generate_folders()

	filename_list = os.listdir(os.getcwd())
	for report in filename_list:
		if report.endswith('_marks.txt'):

			# Checks if the student has passed
			f = open(report, 'r')
			subjects_and_marks = f.readlines()[6:]
			total_failed_subjects = calculate_failed_subjects(
				subjects_and_marks)
			f.close()

			# Move to folder
			move_to_folder(report, total_failed_subjects)

	# Zip both folders
	shutil.make_archive(failed_reports_folder,
						compression_type, failed_reports_folder)
	shutil.make_archive(passed_reports_folder,
						compression_type, passed_reports_folder)


def clean_everything():
	# Clean txt and zip files
	filename_list = os.listdir(os.getcwd())
	for report in filename_list:
		if report.endswith('_marks.txt') or report.endswith('.zip'):
			os.remove(report)

	# Clean folders
	if os.path.exists(passed_reports_folder):
		shutil.rmtree(passed_reports_folder)

	if os.path.exists(failed_reports_folder):
		shutil.rmtree(failed_reports_folder)


def generate_folders():
	if not os.path.exists(passed_reports_folder):
		os.makedirs(passed_reports_folder)

	if not os.path.exists(failed_reports_folder):
		os.makedirs(failed_reports_folder)


def calculate_failed_subjects(subjects_and_marks):
	failed_subjects = 0

	for subject in subjects_and_marks:
		grade = float(subject.split(': ')[1].strip())
		if grade < 5:
			failed_subjects += 1

	return failed_subjects


def move_to_folder(old_filename, total_failed_subjects):
	if total_failed_subjects >= 2:
		new_filename = '_'.join(old_filename.split('_')[:3]) + '_failed.txt'
		os.rename(old_filename, os.path.join(
			failed_reports_folder, new_filename))

	else:
		new_filename = '_'.join(old_filename.split('_')[:3]) + '_passed.txt'
		os.rename(old_filename, os.path.join(
			passed_reports_folder, new_filename))


if __name__ == '__main__':
	try:
		action = sys.argv[1]
	except IndexError:
		pass

	action = sys.argv[1]
	if action == '-p':
		process_reports()
	elif action == '-d':
		clean_everything()
	else:
		print('Action not recognized.')
