import os
from datetime import timedelta, date

start_date = date(2020, 5, 1)
end_date = date(2020, 5, 5)
table_route = 'aggs_v2.creation_measures$' 
commend_template = 'bq rm -f '

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
         yield start_date + timedelta(n)

def main():

#first stage we gonna delete partitions with for loop according to calender inputs.

    for single_date in daterange(start_date, end_date):
        print(commend_template + table_route + single_date.strftime("%Y%m%d"))
        # os.system("pwd")

#second stage we upload new data from side "view" table 



if __name__ == "__main__":
    main()

