# write a program to calculate the diff betwn two dates
from datetime import datetime

date1 = datetime(2026, 9, 1)
date2 = datetime(2026, 9, 27)

difference = date2 - date1

print("Difference between dates:", difference.days, "days")