import os

start_date = '20200501'
end_date = '20200505'

table_route = 'aggs_v2.creation_measures' + "$" + start_date
commend_template = 'bq rm -f '
# def main():

#  first stage we gonna delete partitions with for loop according to calender inputs.

print(commend_template + table_route)
os.system("pwd")

# /// second stage we upload new data from side "view" table 
