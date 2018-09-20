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
rpt.soft.total_estab = 0
rpt.soft.total_empl = 0

#variables for maxes
all_max_wage_amt = 0
all_max_wage_id = 0
all_max_estab_amt = 0
all_max_estab_id = 0
all_max_empl_amt = 0
all_max_empl_id = 0

soft_max_wage_amt = 0
soft_max_wage_id = 0
soft_max_estab_amt = 0
soft_max_estab_id = 0
soft_max_empl_amt = 0
soft_max_empl_id = 0


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
singlefile_reader = csv.reader(fipsfile, delimiter=',')


singlefile_first_line = True

for row in singlefile_reader:
    #Dont count first line (column titles)
    if singlefile_first_line == True:
        singlefile_first_line = False
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
        if (int(row[10]) > all_max_wage_amt):
            all_max_wage_amt = int(row[10])
            all_max_wage_id = fips
        if (int(row[8]) > all_max_estab_amt):
            all_max_estab_amt = int(row[8])
            all_max_estab_id = fips
        if (int(row[9]) > all_max_empl_amt):
            all_max_empl_amt = int(row[9])
            all_max_empl_id = fips

    if row[2] == "5112" and row[1] == "5":
        # Get Stats Over soft
        rpt.soft.count += 1
        rpt.soft.total_pay += int(row[10])
        rpt.soft.total_estab += int(row[8])
        rpt.soft.total_empl += int(row[9])
        # Get maxes
        if (int(row[10]) > soft_max_wage_amt):
            soft_max_wage_amt = int(row[10])
            soft_max_wage_id = fips
        if (int(row[8]) > soft_max_estab_amt):
            soft_max_estab_amt = int(row[8])
            soft_max_estab_id = fips
        if (int(row[9]) > soft_max_empl_amt):
            soft_max_empl_amt = int(row[9])
            soft_max_empl_id = fips


area_titles_file = open(sys.argv[1] + "/area_titles.csv")

area_titles_reader = csv.reader(area_titles_file, delimiter=',')
area_titles_first_line = True
for row in area_titles_reader:
    #Exclude first row, (titles)
    if area_titles_first_line == True:
        area_titles_first_line = False
        continue
        #get maxes for all
    if row[0] == all_max_wage_id:
        all_max_wage_id = row[1]
    if row[0] == all_max_estab_id:
        all_max_estab_id = row[1]
    if row[0] == all_max_empl_id:
        all_max_empl_id = row[1]

        #get maxes for soft
    if row[0] == soft_max_wage_id:
        soft_max_wage_id = row[1]
    if row[0] == soft_max_estab_id:
        soft_max_estab_id = row[1]
    if row[0] == soft_max_empl_id:
        soft_max_empl_id = row[1]

# establish maxes in rpt
rpt.all.max_pay = (all_max_wage_id, all_max_wage_amt)
rpt.all.max_estab = (all_max_estab_id, all_max_estab_amt)
rpt.all.max_empl = (all_max_empl_id, all_max_empl_amt)

rpt.soft.max_pay = (soft_max_wage_id, soft_max_wage_amt)
rpt.soft.max_estab = (soft_max_estab_id, soft_max_estab_amt)
rpt.soft.max_empl = (soft_max_empl_id, soft_max_empl_amt)




# By the time you submit your work to me, this should be the *only* output your
# entire program produces.
print(rpt)