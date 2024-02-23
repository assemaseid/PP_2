import datetime

#ex 1
print("Current date: ", datetime.datetime.now())
print("Subtracted date: ", datetime.datetime.now() - datetime.timedelta(days=5))

#ex 2

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
print("Yesterday:", yesterday.strftime("%x"))
today = datetime.datetime.now()
print("Today:", today.strftime("%x"))
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
print("Tomorrow:", tomorrow.strftime("%x"))

#ex 3
#datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") also we can use
print(datetime.datetime.now().isoformat(sep=" ",timespec= "seconds"))

#ex 4
def date_difference_in_seconds(date_str1, date_str2, date_format='%Y-%m-%d %H:%M:%S'):
    date1 = datetime.datetime.strptime(date_str1, date_format)
    date2 = datetime.datetime.strptime(date_str2, date_format)
    time_difference = abs((date1 - date2).total_seconds())
    return time_difference

date_str1 = '2022-01-01 12:00:00'
date_str2 = '2022-02-01 18:30:00'

difference_in_seconds = date_difference_in_seconds(date_str1, date_str2)
print(f'The difference between the two dates is {difference_in_seconds} seconds.')
