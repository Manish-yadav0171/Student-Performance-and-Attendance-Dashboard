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
# ==============================
# DATA CLEANING AND MERGING
# ==============================

# Check duplicate Student IDs
print("\n--- DUPLICATE STUDENT IDs ---")
print("Marks IDs:", marks_df["Student_ID"].duplicated().sum())
print("Attendance IDs:", attendance_df["Student_ID"].duplicated().sum())


# Merge both datasets using Student_ID
merged_df = pd.merge(
    marks_df,
    attendance_df,
    on="Student_ID",
    how="inner",
    suffixes=("_Marks", "_Attendance")
)

print("\n--- MERGED DATA ---")
print(merged_df.head())


# Calculate total marks
subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]

merged_df["Total_Marks"] = merged_df[subjects].sum(axis=1)


# Calculate average marks
merged_df["Average_Marks"] = merged_df[subjects].mean(axis=1)


# Calculate attendance percentage
merged_df["Attendance_Percentage"] = (
    merged_df["Classes_Attended"] / merged_df["Total_Classes"]
) * 100


# Display final dataset
print("\n--- FINAL DATASET ---")
print(merged_df.head())


# Display dataset dimensions
print("\nFinal dataset shape:", merged_df.shape)