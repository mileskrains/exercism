import datetime

def meetup_day(gyear, gmonth, gdow, gdesc):
    weekdays = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()

    gmonth_firstdow = datetime.datetime(gyear, gmonth, 1).weekday()
    gdow_firstdate = (weekdays.index(gdow) - gmonth_firstdow + 7) % 7
    gdow_dates = list(range(1,32)[gdow_firstdate::7])
    try:
        datetime.datetime(gyear, gmonth, gdow_dates[-1])
    except ValueError:
        del gdow_dates[-1]

    date_from_desc = dict(zip('1st 2nd 3rd 4th 5th'.split(), gdow_dates))
    date_from_desc['last'] = gdow_dates[-1]
    date_from_desc['teenth'] = [d for d in gdow_dates if 12<d<20][0]

    return datetime.date(gyear, gmonth, date_from_desc[gdesc])
