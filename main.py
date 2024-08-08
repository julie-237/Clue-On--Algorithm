"""Step 1:
Ask for the number of sleeping hours, store it
Ask for the number of working hours, store it 
Ask for the number of relaxing hours, store it 
Compute available hours = 24 - sleeping hours - working hours - relaxing hours - 3
print available hours


Step 2:
Ask for the number of sleeping hours, store it
Ask for the number of working hours, store it 
Ask for the number of week day relaxing hours, store it 
Ask for the number of week end relaxing hours, store it 
Compute week day available hours = 24 - sleeping hours - working hours - week day relaxing hours - 3
Compute week day available hours = 24 - sleeping hours - week end relaxing hours - 3
Compute the total available hours per week   = 5* available hours per week day + 2* available hours per week end


print available hours (week day, week end, total per week)"""

import time

sleeping_hours = int(input("howlong do you sleep? "))
working_hours = int(input("howlong do you work? "))
relaxing_hours_weekday = int(input("howlong do you relax on weekdays? "))
relaxing_hours_weekend = int(input("howlong do you relax on weekends? "))

available_study_hours_per_weekday = 24 - sleeping_hours - working_hours - relaxing_hours_weekday - 3
available_study_hours_per_weekend = 24 - sleeping_hours - relaxing_hours_weekday - 3
total_available_hours_per_week = 5*available_study_hours_per_weekday + 2*available_study_hours_per_weekend

print("and you have ", sleeping_hours, " hours to sleep per day")
time.sleep(2)
print("and you have ", working_hours, " hours to work per day")
time.sleep(2)
print("and you have ", relaxing_hours_weekday, " hours to relax per weekday")
time.sleep(2)

set_term = "so you have {} hours to study per {}"

print(set_term.format(available_study_hours_per_weekday, "weekday"))
time.sleep(2)
print(set_term.format(available_study_hours_per_weekend, "weekend"))
time.sleep(2)
print(set_term.format(total_available_hours_per_week, "week"))
time.sleep(2)

print(f"and you have {relaxing_hours_weekday} hours to relax per day")

