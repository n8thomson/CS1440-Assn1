#!/usr/bin/env python3

from Report import Report
rpt = Report()

## TODO: Add your code here
import sys
import csv

#reset
rpt.all.count = 0
rpt.all.total_pay = 0
rpt.all.total_estab = 0
rpt.all.total_empl = 0
rpt.soft.count = 0
rpt.soft.total_pay = 0
rpt.soft.total_empl = 0

#variables for maxes
all_max_annual_wage_amt = 0
all_max_annual_wage_id = 0





singlefile = None
areatitles = None


try:
    try:
        singlefile = sys.argv[1] + '/2017.annual.singlefile.csv'
        v = open(singlefile)
    except:
        print("ERROR: No data directory given. Please specify a directory containing a file called '2017_annual_singlefile.csv'")
    try:
        areatitles = sys.argv[1] + '/area_titles.csv'
    except:
        print("ERROR: No data directory given. Please specify a directory containing a file called 'area_titles.csv'")
except:
    sys.exit(0)



file = sys.argv[1] + "/2017.annual.singlefile.csv"

fipsfile = open(file)
area_titles_reader = csv.reader(fipsfile, delimiter=',')


first_line = True

for row in area_titles_reader:
    #Dont count first line (column titles)
    if first_line == True:
        first_line = False
        continue
    fips = row[0]
    # Dont count fips with 000, C, or US
    if fips[2:] == "000" or fips[0:1] == "C" or fips[0:2] == "US":
        continue
    if row[1] == "0" and row[2] == "10":
        #Get Stats Over All
        rpt.all.count += 1
        rpt.all.total_pay += int(row[10])
        rpt.all.total_estab += int(row[8])
        rpt.all.total_empl += int(row[9])
        #Get highest wage
        if (int(row[10]) > all_max_annual_wage_amt):






















# By the time you submit your work to me, this should be the *only* output your
# entire program produces.
print(rpt)