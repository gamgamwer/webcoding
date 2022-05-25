import datetime as dt
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':
    base_date = dt.datetime(2022,4,1)

    for day in range(30):
        date=base_date + relativedelta(days=day)

        print(date)
