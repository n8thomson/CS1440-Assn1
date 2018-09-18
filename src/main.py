#!/usr/bin/env python3

from Report import Report
rpt = Report()

## TODO: Add your code here
import sys
import csv



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
line_count = 0
for row in area_titles_reader:
    print(row[0])









# By the time you submit your work to me, this should be the *only* output your
# entire program produces.
