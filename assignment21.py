"""

Number 1 -

Question -
Add the current date to the text file today.txt as a string.

Answer -
from datetime import date
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now_str, file=output)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
Read the text file today.txt into the string today_string

Answer -
with open('today.txt', 'rt') as input:
    today_string = input.read()
    
today_string
'2021-05-04\n'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
Parse the date from today_string.

Answer -
from datetime import datetime
fmt = '%Y-%m-%d\n'
datetime.strptime(today_string, fmt)
datetime.datetime(2021, 5, 4, 0, 0)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4-

Question -
List the files in your current directory

Answer -
import os
os.listdir('.')
['.ipynb_checkpoints',
 'Assignment_10_Soln.ipynb',
 'Assignment_11_Soln.ipynb',
 'Assignment_12_Soln.ipynb',
 'Assignment_13_Soln.ipynb',
 'Assignment_14_Soln.ipynb',
 'Assignment_15_Soln.ipynb',
 'Assignment_16_Soln.ipynb',
 'Assignment_17_Soln.ipynb',
 'Assignment_18_Soln.ipynb',
 'Assignment_19_Soln.ipynb',
 'Assignment_1_Soln.ipynb',
 'Assignment_20_Soln.ipynb',
 'Assignment_21_Soln.ipynb',
 'Assignment_2_Soln.ipynb',
 'Assignment_3_Soln.ipynb',
 'Assignment_4_Soln.ipynb',
 'Assignment_5_Soln.ipynb',
 'Assignment_6_Soln.ipynb',
 'Assignment_7_Soln.ipynb',
 'Assignment_8_Soln.ipynb',
 'Assignment_9_Soln.ipynb',
 'books.csv',
 'books.db',
 'image.jpg',
 'new.zip',
 'newimg.jpg',
 'Soln.ipynb',
 'test.txt',
 'today.txt',
 'zoo.py',
 '__pycache__']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
Create a list of all of the files in your parent directory (minimum five files should be available).

Answer -
os.listdir('..')
['Assignment_1.docx',
 'Assignment_10.docx',
 'Assignment_11.docx',
 'Assignment_12.docx',
 'Assignment_13.docx',
 'Assignment_14.docx',
 'Assignment_15.docx',
 'Assignment_16.docx',
 'Assignment_17.docx',
 'Assignment_18.docx',
 'Assignment_19.docx',
 'Assignment_2.docx',
 'Assignment_20.docx',
 'Assignment_21.docx',
 'Assignment_22.docx',
 'Assignment_23.docx',
 'Assignment_24.docx',
 'Assignment_25.docx',
 'Assignment_3.docx',
 'Assignment_4.docx',
 'Assignment_5.docx',
 'Assignment_6.docx',
 'Assignment_7.docx',
 'Assignment_8.docx',
 'Assignment_9.docx',
 'Solutions']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.

Answer -
!python multi_process.py
wait 0.11258240976256462 seconds, time is 2021-05-04 14:26:13.559911
wait 0.5027238463295997 seconds, time is 2021-05-04 14:26:13.947904
wait 0.7974100623500293 seconds, time is 2021-05-04 14:26:14.239878
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
Create a date object of your day of birth.

Answer -
my_day = date(1996, 8, 10)
my_day
datetime.date(1996, 8, 10)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
What day of the week was your day of birth?

Answer -
With weekday(), Monday is 0 and Sunday is 6. With isoweekday(), Monday is 1 and

Sunday is 7. Therefore, this date is a Saturday.

my_day.weekday()
5
my_day.isoweekday()
6
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 9 -

Question -
When will you be (or when were you) 10,000 days old?

Answer -
from datetime import timedelta
ten_thousand = my_day + timedelta(days=10000)
ten_thousand
datetime.date(2023, 12, 27)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






"""