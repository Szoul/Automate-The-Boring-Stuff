#! python 3.8.3
#Date_Detection.py: can detect DD/MM/YYYY format

'''
Project description:
    Write a regular expression that can detect dates in the DD/MM/YYYY format.
    Assume that the days range from 01 to 31, the months range from 01 to 12, 
    and the years range from 1000 to 2999. Note that if the day or month is a 
    single digit, it’ll have a leading zero.

    The regular expression doesn’t have to detect correct days for each month 
    or for leap years; it will accept nonexistent dates like 31/02/2020 or 
    31/04/2021. Then store these strings into variables named month, day, and 
    year, and write additional code that can detect if it is a valid date.
'''

#If Match found check if it is a viable date 
def is_valid_date (day,month,year):
    valid_dates = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}           #maximum days per month
    #check leap year
    if year%400 == 0:
        valid_dates[2] = 29
    elif year%100 == 0:
        pass
    elif year%4 == 0:
        valid_dates[2] = 29
    else:
        pass
    
    #vali-date
    if valid_dates[month] >= day:                                                                       #check if current day is possible in that particular month
        return True
    else:
        return False


def detect_and_validate_dates(text):

    #Regular Expression to detect a date format
    import re
    date_regex = re.compile (r"""
                            (0?[1-9]|[1-2][0-9]|3[0-1])         #day (01-31)
                            (/)                                 #seperation
                            (0?[1-9]|1[0-2])                    #month (01-12)
                            (/)                                 #seperation
                            ([1-2][0-9][0-9][0-9])              #year (1000-2999)
                            """, re.VERBOSE)
    
    mu = date_regex.findall(text)

    #store day,month, year in a seperate variable and check if it is viable
    list_of_valid_dates = []
    for current_date in mu:
        index = mu.index(current_date)
        day = int(mu[index][0])
        month = int(mu[index][2])
        year = int(mu[index][4])

        if is_valid_date(day,month,year) == True:
            valid_date = str(current_date[0]) + "/" + str(current_date[2]) + "/" + str(current_date[4])
            list_of_valid_dates.append(valid_date)
        else:
            pass
    
    return list_of_valid_dates

    

test_text = "He was born on the 29/02/1264, becoming a teacher on 31/2/1284 and even today (20/03/2999) he is being remembered as such."
print (detect_and_validate_dates(test_text))