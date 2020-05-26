import os
from datetime import timedelta, date

start_date = date(2020, 4, 26)
end_date = date(2020, 4, 27)
table_route = 'aggs_v2.units_answers$' 
commend_template = 'bq rm -f '

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
         yield start_date + timedelta(n)

def main():

#first stage we gonna delete partitions with for loop according to calender inputs.

    for single_date in daterange(start_date, end_date):
        tmp = commend_template + "'" + table_route + single_date.strftime("%Y%m%d") + "'"
        # print(tmp)
        os.system(tmp)

#second stage we upload new data from side "view" table 


if __name__ == "__main__":
    main()

