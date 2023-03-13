import pandas as pd
from datetime import datetime


def get_date(old_date):
    possible_formats = ["%d %b %Y", "%d-%m-%Y", "%Y%m%d", "%Y/%m/%d", "%Y-%m-%d", "%Y-%m-%dT%H:%M"]
    for f in possible_formats:
        try:
            new_date = datetime.strptime(old_date, f)
        except:
            pass
    return new_date

# Convert the following series of date-strings to a time series.
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
print("Input Series:\t", ser)

ser = ser.apply(get_date)
print("Output Series:\t", ser)

