import pandas as pd

# Reading CSV files
marks_df = pd.read_csv("../Data/students_marks.csv")
attendance_df = pd.read_csv("../Data/students_attendance.csv")


# ==============================
# DATA INSPECTION
# ==============================

# Display first 5 rows
print("\n--- MARKS DATA: FIRST 5 ROWS ---")
print(marks_df.head())

print("\n--- ATTENDANCE DATA: FIRST 5 ROWS ---")
print(attendance_df.head())


# Display dataset dimensions
print("\n--- DATASET SHAPE ---")
print("Marks dataset:", marks_df.shape)
print("Attendance dataset:", attendance_df.shape)


# Display column information
print("\n--- MARKS DATA INFORMATION ---")
marks_df.info()

print("\n--- ATTENDANCE DATA INFORMATION ---")
attendance_df.info()


# Check missing values
print("\n--- MISSING VALUES ---")
print("Marks dataset:")
print(marks_df.isnull().sum())

print("\nAttendance dataset:")
print(attendance_df.isnull().sum())


# Check duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Marks duplicates:", marks_df.duplicated().sum())
print("Attendance duplicates:", attendance_df.duplicated().sum())