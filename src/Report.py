# You do not need to modify this file.
# In fact, it's best if you leave this completely unchanged.

class EmploymentDataSet():
    def __init__(self):
        self.count                   = 0

        self.total_pay               = 1
        self.max_pay                 = ("Junk2", 2)

        self.total_estab             = 3
        self.max_estab               = ("Junk4", 4)

        self.total_empl              = 5
        self.max_empl                = ("Junk6", 6)

class Report():
    def __init__(self):
        self.all  = EmploymentDataSet()
        self.soft = EmploymentDataSet()


    def __str__(self):
        return f"""
[============]
[Final Report]
[============]

Statistics over all industries in 2017:
=========================================================
Count of FIPS areas in report        {self.all.count:,}

Gross annual wages                   ${self.all.total_pay:,}
Area with maximum annual wages       {self.all.max_pay[0]}
Maximum reported wage                ${self.all.max_pay[1]:,}

Gross number of establishments       {self.all.total_estab:,}
Area with maximum establishments     {self.all.max_estab[0]}
Maximum reported # establishments    {self.all.max_estab[1]:,}

Gross annual employment level        {self.all.total_empl:,}
Area with maximum employment         {self.all.max_empl[0]}
Maximum reported employment level    {self.all.max_empl[1]:,}


Statistics over the software publishing industry in 2017:
=========================================================
Count of FIPS areas in report        {self.soft.count:,}

Gross annual wages                   ${self.soft.total_pay:,}
Area with maximum annual wages       {self.soft.max_pay[0]}
Maximum reported wage                ${self.soft.max_pay[1]:,}

Gross number of establishments       {self.soft.total_estab:,}
Area with maximum establishments     {self.soft.max_estab[0]}
Maximum reported # establishments    {self.soft.max_estab[1]:,}

Gross annual employment level        {self.soft.total_empl:,}
Area with maximum employment         {self.soft.max_empl[0]}
Maximum reported employment level    {self.soft.max_empl[1]:,}
"""
