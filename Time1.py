days = int(input('days: '))
hours = int(input('hours: '))
minutes = int(input('minutes: '))
seconds = int(input('seconds: '))
nice = True
if hours > 24:
    print('There are only 24 hours in a day!')
    if nice == True:
        nice = False
if minutes > 60:
    print('There are only 60 minutes in an hour!')
    if nice == True:
        nice = False
if seconds > 60:
    print('There are only 60 seconds in a minute!')
    if nice == True:
        nice = False
if hours > 24 or minutes > 60 or seconds > 60:
    print('Try again!')
if nice == True:
    print('seconds in the given time: ' + str(days*86400 + hours*3600 + minutes*60 + seconds))