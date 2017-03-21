average_hours = 6
semester_length = 17
number_of_workdays = 5
work_hours_weekly = 52
all_working_hours = work_hours_weekly * semester_length
print(all_working_hours)
Hours_spent_coding_in_a_semester = print("Hours spent coding in a semester: " + str(average_hours * semester_length * number_of_workdays))


average_work_hours_weekly = 52
print("Percentage of the coding hours in the semester: " + str((average_hours * semester_length * number_of_workdays) / all_working_hours) * 100)
