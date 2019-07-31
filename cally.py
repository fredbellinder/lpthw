import csv
from datetime import datetime
from datetime import timedelta
from sys import argv

"""
This little script adapts the shape of the Chas Academy Calendar export from notion into a Google calendar friendly import.
usage: 
$ python3 cally.py your_notion_csv_file.csv your_google_formatted_csv_file.csv 
The your_google_formatted_csv_file.csv gets created if it doesn't already exist.
If all went according to plan you can now import your_google_formatted_csv_file.csv into google calendar, 
this probably only works on desktop browser interfaces.

Notion.so: please grow up and add a calendar subscription link to your app! Said with love.. 💚
"""

script, input_file_path, output_file_path = argv

# open the input file and set the encoding to support emojis and other symbols
file = False
try:
    file = open(input_file_path, newline="", encoding='utf-8-sig')
except Exception as e:
    print(e)
    print("Try entering a valid path to a csv file from Chas Academys Notion calendar")

while not file:
    try:
        path = input("> ")
        file = open(path, newline="", encoding='utf-8-sig')

    except EOFError:
        print("Exited on user prompt")
    except:
        print(
            "Try entering a valid path to a csv file from Chas Academys Notion calendar, or CTRL-D to exitpip")


# set the opened file to an iterator in the eyes of the csv module
reader = csv.reader(file)

# to skip the first line with the non-compatible header we go one iteration into the iterable that is reader.
next(reader)

# this will contain the adapted lines from the input csv.
total = []

# we loop over what is left in the iterable
for row in reader:
    # depending on the exactness of the given start/end dates/times we set the values to either input or their defaults
    # rows without a date specified are skipped, thay have no use in a calendar.
    allDay: bool = False
    if len(row[1]):
        # if only this part of the if-statement runs, the format looks like this: "Sep 11, 2018 10:00"
        startDate: datetime = datetime.strptime(row[1][0:12], '%b %d, %Y')
        startTime: datetime = datetime.strptime("00:00", '%H:%M')
        endTime: datetime = datetime.strptime("23:59", '%H:%M')
        endDate: datetime = startDate
        if len(row[1]) == 18:
            startTime: datetime = datetime.strptime(row[1][13:], '%H:%M')
            # the end time will be default 2 hours after startTime if only a startTime has beed provided
            endTime: datetime = startTime + timedelta(hours=2)
        elif len(row[1]) == 24:
            # The format looks like this: "Sep 11, 2018 10:00-12:00"
            startTime = datetime.strptime(row[1][13:-6], '%H:%M')
            # an end time has been provided and is set
            endTime = datetime.strptime(row[1][-5:], '%H:%M')
        elif len(row[1]) == 27:
            # The format looks like this: "Dec 17, 2018 → Jan 04, 2019"
            endTime = datetime.strptime(
                row[1][15:], '%b %d, %Y') + timedelta(hours=24)
            endDate = datetime.strptime(
                row[1][-12:], '%b %d, %Y')
            allDay = True
        # if no input has been provided for startTime or endTime the "All Day Event" is set to true
        if not allDay:
            allDay = startTime == datetime.strptime(
                "00:00", '%H:%M') and endTime == datetime.strptime("23:59", '%H:%M')

        # if it's an alldayevent we remove start and endtime, otherwise these will be displayed in Google cal.
        if allDay:
            startTime, endTime = [None, None]

        # The template for the row is set
        template = [
            row[0],
            datetime.strftime(startDate, '%d/%m/%Y'),
            datetime.strftime(startTime, '%H:%M') if startTime else None,
            datetime.strftime(endDate, '%d/%m/%Y'),
            datetime.strftime(endTime, '%H:%M') if endTime else None,
            allDay,
            str(row[2] + row[3]).strip(),
            "",
            False
        ]
        # we append our filled out template to the total list that csv.writer will be writing from
        total.append(template)


with open(output_file_path, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
    # we set the headers that we need for an import to google calendar
    wr.writerow(
        ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"])
    # we write each and every of the filled out templates stored in the total list.
    for row in total:
        wr.writerow(row)
