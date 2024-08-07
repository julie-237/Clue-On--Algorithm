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

sleeping_hours = int(input("howlong do you sleep? "))
working_hours = int(input("howlong do you work? "))
relaxing_hours = int(input("howlong do you relax? "))
available_study_hours_per_day = 24 - sleeping_hours - working_hours - relaxing_hours - 3
print("so you have ", available_study_hours_per_day, " hours to study per day")

print("and you have ", sleeping_hours, " hours to sleep per day")
print("and you have ", working_hours, " hours to work per day")
print("and you have ", relaxing_hours, " hours to relax per day")

print(f"and you have {relaxing_hours} hours to relax per day")

message_template = "and you have {} hours to {} per day"
print(message_template.format(sleeping_hours, "sleep"))
print(message_template.format(working_hours, "work"))
print(message_template.format(relaxing_hours, "relax"))

print(sleeping_hours, available_study_hours_per_day)
