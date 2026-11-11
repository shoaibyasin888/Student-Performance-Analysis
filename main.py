
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Student Performance Analysis")
print("Project Started Successfully!")


# Read the data of students from the CSV file and display the first five rows, dataset information, and shape of the dataset.
df = pd.read_csv("dataset/students.csv")
print("\n Display the first five students:")
print(df.head())

# Display dataset information
print("\n Dataset Information:")
print(df.info())

# Display dataset shape
print("\n Dataset shape:")
print(df.shape)

def assign_grade(marks):
    if marks >=90:
        return "A"
    elif marks >=80:
        return "B"
    elif marks >=70:
        return "C"
    else:
        return "F"


# def assign_grade(marks):

#     if marks >= 90:
#         return "A"

#     elif marks >= 80:
#         return "B"

#     elif marks >= 70:
#         return "C"

#     elif marks >= 60:
#         return "D"

#     else:
#         return "F"


# df["grade"] = df["average_marks"].apply(assign_grade)

# print("\nStudent Grades:")
# print(df[["student_id", "average_marks", "grade"]])



# # Sort students by average marks
# top_students = df.sort_values(
#     by="average_marks",
#     ascending=False
# )

# print("\nTop 5 Students:")
# print(
#     top_students[
#         ["student_id", "average_marks", "grade"]
#     ].head(5)
# )


# # Average attendance
# average_attendance = df["attendance"].mean()

# # Average daily study hours
# average_study_hours = df["study_hours"].mean()

# # Students with attendance below 75%
# low_attendance = df[df["attendance"] < 75]

# print("\nAttendance Analysis")

# print("Average Attendance:",
#       round(average_attendance, 2), "%")

# print("Average Study Hours:",
#       round(average_study_hours, 2))

# print("\nStudents with Attendance Below 75%:")
# print(low_attendance[["student_id", "attendance"]])



# # Create output directories if they do not exist
# os.makedirs("outputs/charts", exist_ok=True)
# os.makedirs("outputs/reports", exist_ok=True)

# print("\nOutput folders are ready!")



# plt.figure(figsize=(9, 5))

# sns.histplot(
#     df["average_marks"],
#     bins=8,
#     kde=True
# )

# plt.title("Student Performance Distribution")
# plt.xlabel("Average Marks")
# plt.ylabel("Number of Students")

# plt.savefig("outputs/charts/performance_distribution.png")

# plt.show()
# plt.close()



# top5 = df.nlargest(5, "average_marks")

# plt.figure(figsize=(9, 5))

# sns.barplot(
#     data=top5,
#     x="average_marks",
#     y="student_id"
# )

# plt.title("Top 5 Performing Students")
# plt.xlabel("Average Marks")
# plt.ylabel("Student ID")

# plt.savefig("outputs/charts/top_students.png")

# plt.show()
# plt.close()



# plt.figure(figsize=(9, 5))

# sns.scatterplot(
#     data=df,
#     x="study_hours",
#     y="average_marks",
#     hue="gender",
#     s=100
# )

# plt.title("Study Hours vs Average Marks")
# plt.xlabel("Daily Study Hours")
# plt.ylabel("Average Marks")

# plt.savefig("outputs/charts/study_hours_vs_marks.png")

# plt.show()
# plt.close()



# plt.figure(figsize=(9, 6))

# correlation = df[
#     [
#         "study_hours",
#         "attendance",
#         "assignments_completed",
#         "math_score",
#         "science_score",
#         "english_score",
#         "average_marks"
#     ]
# ].corr()

# sns.heatmap(
#     correlation,
#     annot=True,
#     cmap="coolwarm",
#     fmt=".2f"
# )

# plt.title("Student Performance Correlation")

# plt.savefig("outputs/charts/correlation_heatmap.png")

# plt.show()
# plt.close()



# # Save processed dataset
# df.to_csv(
#     "outputs/cleaned_students.csv",
#     index=False
# )

# # Generate report
# with open(
#     "outputs/reports/analysis_report.txt",
#     "w"
# ) as file:

#     file.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
#     file.write("=" * 40 + "\n\n")

#     file.write(f"Total Students: {len(df)}\n")

#     file.write(
#         f"Class Average: {class_average:.2f}\n"
#     )

#     file.write(
#         f"Highest Average: {highest_average:.2f}\n"
#     )

#     file.write(
#         f"Lowest Average: {lowest_average:.2f}\n"
#     )

#     file.write(
#         f"Average Attendance: {average_attendance:.2f}%\n"
#     )

#     file.write(
#         f"Average Study Hours: {average_study_hours:.2f}\n"
#     )

#     file.write("\nTOP 5 STUDENTS\n")

#     for _, student in top_students.head(5).iterrows():

#         file.write(
#             f"{student['student_id']}: "
#             f"{student['average_marks']:.2f}\n"
#         )

# print("\nAnalysis Report Generated Successfully!")
# print("Project Completed!")


