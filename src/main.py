#!/usr/bin/env python3

from Report import Report
rpt = Report()

## TODO: Add your code here
import sys
import csv
import operator

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

#lists for distict values
distinct_wage_values = []
distinct_estab_values = []
distinct_empl_values = []

#lists for unique values
unique_wage_values = []
unique_estab_values = []
unique_empl_values = []

#lists for distict values
soft_distinct_wage_values = []
soft_distinct_estab_values = []
soft_distinct_empl_values = []

#lists for unique values
soft_unique_wage_values = []
soft_unique_estab_values = []
soft_unique_empl_values = []

#all of the things in one list
all_wage_list = []
all_estab_list = []
all_empl_list = []

soft_wage_list = []
soft_estab_list = []
soft_empl_list = []


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

        #Putting all values into list, paired up with their fips codes
        all_wage_list.append((fips, int(row[10])))
        all_estab_list.append((fips, int(row[8])))
        all_empl_list.append((fips, int(row[9])))




        #Get Stats Over All
        rpt.all.count += 1
        rpt.all.total_pay += int(row[10])

        # getting the amount of distinct values of annual wadges
        if row[10] in distinct_wage_values and row[10] in unique_wage_values:
            # Remove not unique values
            unique_wage_values.remove(row[10])

        elif row[10] not in distinct_wage_values:
            # Add distinct values
            distinct_wage_values.append(row[10])
            unique_wage_values.append(row[10])

        rpt.all.total_estab += int(row[8])

        # getting the amount of distinct values
        if row[8] in distinct_estab_values and row[8] in unique_estab_values:
            # Remove not unique values
            unique_estab_values.remove(row[8])
        elif row[8] not in distinct_estab_values:
            # Add distinct values
            distinct_estab_values.append(row[8])
            unique_estab_values.append(row[8])

        rpt.all.total_empl += int(row[9])

        # getting the amount of distinct values
        if row[9] in distinct_empl_values and row[9] in unique_empl_values:
            # Remove not unique values
            unique_empl_values.remove(row[9])
        elif row[9] not in distinct_empl_values:
            # Add distinct values
            distinct_empl_values.append(row[9])
            unique_empl_values.append(row[9])
        
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

        # getting the amount of distinct values of annual wadges
        if row[10] in soft_distinct_wage_values and row[10] in soft_unique_wage_values:
            # Remove not unique values
            soft_unique_wage_values.remove(row[10])
        elif row[10] not in soft_distinct_wage_values:
            # Add distinct values
            soft_distinct_wage_values.append(row[10])
            soft_unique_wage_values.append(row[10])

        rpt.soft.total_estab += int(row[8])

        # getting the amount of distinct values of annual estab
        if row[8] in soft_distinct_estab_values and row[8] in soft_unique_estab_values:
            # Remove not unique values
            soft_unique_estab_values.remove(row[8])
        elif row[8] not in soft_distinct_estab_values:
            # Add distinct values
            soft_distinct_estab_values.append(row[8])
            soft_unique_estab_values.append(row[8])

        rpt.soft.total_empl += int(row[9])

        # getting the amount of distinct values of annual emp
        if row[9] in soft_distinct_empl_values and row[9] in soft_unique_empl_values:
            # Remove not unique values
            soft_unique_empl_values.remove(row[9])
        elif row[9] not in soft_distinct_empl_values:
            # Add distinct values
            soft_distinct_empl_values.append(row[9])
            soft_unique_empl_values.append(row[9])
        
        
        
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



area_titles = {}
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

    # Read area codes into dict
    area_titles[row[0]] = row[1]


for i in range(len(all_wage_list)):
    all_wage_list[i] = (area_titles[all_wage_list[i][0]],  all_wage_list[i][1])
    
for i in range(len(all_empl_list)):
    all_empl_list[i] = (area_titles[all_empl_list[i][0]],  all_empl_list[i][1])
    
for i in range(len(all_estab_list)):
    all_estab_list[i] = (area_titles[all_estab_list[i][0]],  all_estab_list[i][1])


#Get the top 5 and establish
all_wage_list.sort(key=operator.itemgetter(1), reverse=True)
all_wage_top5 = [all_wage_list[0], all_wage_list[1], all_wage_list[2], all_wage_list[3], all_wage_list[4]]
rpt.all.top_annual_wages = all_wage_top5

all_estab_list.sort(key=operator.itemgetter(1), reverse=True)
all_estab_top5 = [all_estab_list[0], all_estab_list[1], all_estab_list[2], all_estab_list[3], all_estab_list[4]]
rpt.all.top_annual_estab = all_estab_top5

all_empl_list.sort(key=operator.itemgetter(1), reverse=True)
all_empl_top5 = [all_empl_list[0], all_empl_list[1], all_empl_list[2], all_empl_list[3], all_empl_list[4]]
rpt.all.top_annual_avg_emplvl = all_empl_top5





# establish maxes in rpt
rpt.all.max_pay = (all_max_wage_id, all_max_wage_amt)
rpt.all.max_estab = (all_max_estab_id, all_max_estab_amt)
rpt.all.max_empl = (all_max_empl_id, all_max_empl_amt)

rpt.soft.max_pay = (soft_max_wage_id, soft_max_wage_amt)
rpt.soft.max_estab = (soft_max_estab_id, soft_max_estab_amt)
rpt.soft.max_empl = (soft_max_empl_id, soft_max_empl_amt)

#establish distinct values
rpt.all.distinct_pay = len(distinct_wage_values)
rpt.all.distinct_estab = len(distinct_estab_values)
rpt.all.distinct_empl = len(distinct_empl_values)


#establish unique values
rpt.all.unique_pay = len(unique_wage_values)
rpt.all.unique_estab = len(unique_estab_values)
rpt.all.unique_empl = len(unique_empl_values)

#Per capita average wage
rpt.all.per_capita_avg_wage = rpt.all.total_pay/rpt.all.total_empl




#establish distinct values  SOFT
rpt.soft.distinct_pay = len(soft_distinct_wage_values)
rpt.soft.distinct_estab = len(soft_distinct_estab_values)
rpt.soft.distinct_empl = len(soft_distinct_empl_values)


#establish unique values SOFT
rpt.soft.unique_pay = len(soft_unique_wage_values)
rpt.soft.unique_estab = len(soft_unique_estab_values)
rpt.soft.unique_empl = len(soft_unique_empl_values)

#Per capita average wage SOFT
rpt.soft.per_capita_avg_wage = rpt.soft.total_pay/rpt.soft.total_empl









# By the time you submit your work to me, this should be the *only* output your
# entire program produces.
print(rpt)