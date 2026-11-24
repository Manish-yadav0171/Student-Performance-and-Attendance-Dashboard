import pandas as pd

# Reading marks CSV file
marks_df = pd.read_csv("../Data/students_marks.csv")

# Reading attendance CSV file
attendance_df = pd.read_csv("../Data/students_attendance.csv")

# Display marks data
print("STUDENT MARKS DATA")
print(marks_df)

print("\nSTUDENT ATTENDANCE DATA")
print(attendance_df)