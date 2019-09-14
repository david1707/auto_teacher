A small 2-files script where the first generates random files with names and marks, and the second one calculates if it passes the school year

## Generate reports

To generate reports, run the generate_reports.py with the argument -g and the number of reports to generate. For example:

```python
python .\generate_reports.py -g 500
```

This will generate 500 reports with random names, and between 8 and 10 subjects with a mark between 3.5 and 10.

## Delete reports

To delete reports, run the generate_reports.py with the argument -d to delete them

```python
python .\generate_reports.py -d
```

This will remove every file ending with '_marks.txt'