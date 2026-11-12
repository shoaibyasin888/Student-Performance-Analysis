
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Student Performance Analysis")
print("Project Started Successfully!")


# Read the data of students from the CSV file
df = pd.read_csv("dataset/students.csv")

print("\nDisplay the first five students:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)


# Calculate average marks for each student
df["average_marks"] = df[
    ["math_score", "science_score", "english_score"]
].mean(axis=1)

print("\nAverage Marks:")
print(df[["student_id", "average_marks"]])


# Assign grades to students
def assign_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"


df["grade"] = df["average_marks"].apply(assign_grade)

print("\nStudent Grades:")
print(df[["student_id", "average_marks", "grade"]])


# Class Performance Statistics
class_average = df["average_marks"].mean()
highest_average = df["average_marks"].max()
lowest_average = df["average_marks"].min()


# ==========================================
# SUBJECT-WISE PERFORMANCE ANALYSIS
# ==========================================

print("\n===== SUBJECT-WISE ANALYSIS =====")

subject_columns = [
    "math_score",
    "science_score",
    "english_score"
]

# Calculate average marks of each subject
subject_averages = df[subject_columns].mean()

print("\nAverage Marks in Each Subject:")
print(subject_averages)

# Find best and weakest performing subjects
best_subject = subject_averages.idxmax()
weakest_subject = subject_averages.idxmin()

print("\nBest Performing Subject:", best_subject)
print("Subject Needing Improvement:", weakest_subject)


# Count students in each grade
grade_counts = df["grade"].value_counts().sort_index()

print("\n===== GRADE DISTRIBUTION =====")
print(grade_counts)


# Calculate pass percentage
pass_percentage = (
    (df["average_marks"] >= 60).sum() / len(df)
) * 100

print("\nClass Pass Percentage:", round(pass_percentage, 2), "%")


# Sort students by average marks
top_students = df.sort_values(
    by="average_marks",
    ascending=False
)

print("\nTop 5 Students:")
print(
    top_students[
        ["student_id", "average_marks", "grade"]
    ].head(5)
)


# Average attendance
average_attendance = df["attendance"].mean()

# Average daily study hours
average_study_hours = df["study_hours"].mean()

# Students with attendance below 75%
low_attendance = df[df["attendance"] < 75]

print("\nAttendance Analysis")

print("Average Attendance:",
      round(average_attendance, 2), "%")

print("Average Study Hours:",
      round(average_study_hours, 2))

print("\nStudents with Attendance Below 75%:")
print(low_attendance[["student_id", "attendance"]])


# Create output directories if they do not exist
os.makedirs("outputs/charts", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)

print("\nOutput folders are ready!")


# ==========================================
# CHART 1: PERFORMANCE DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 5))

sns.histplot(
    df["average_marks"],
    bins=8,
    kde=True
)

plt.title("Student Performance Distribution")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")

plt.savefig("outputs/charts/performance_distribution.png")

plt.show()
plt.close()


# ==========================================
# CHART 2: TOP 5 STUDENTS
# ==========================================

top5 = df.nlargest(5, "average_marks")

plt.figure(figsize=(9, 5))

sns.barplot(
    data=top5,
    x="average_marks",
    y="student_id"
)

plt.title("Top 5 Performing Students")
plt.xlabel("Average Marks")
plt.ylabel("Student ID")

plt.savefig("outputs/charts/top_students.png")

plt.show()
plt.close()


# ==========================================
# CHART 3: STUDY HOURS VS MARKS
# ==========================================

plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="study_hours",
    y="average_marks",
    hue="gender",
    s=100
)

plt.title("Study Hours vs Average Marks")
plt.xlabel("Daily Study Hours")
plt.ylabel("Average Marks")

plt.savefig("outputs/charts/study_hours_vs_marks.png")

plt.show()
plt.close()


# ==========================================
# CHART 4: CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(9, 6))

correlation = df[
    [
        "study_hours",
        "attendance",
        "assignments_completed",
        "math_score",
        "science_score",
        "english_score",
        "average_marks"
    ]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Student Performance Correlation")

plt.savefig("outputs/charts/correlation_heatmap.png")

plt.show()
plt.close()


# ==========================================
# CHART 5: SUBJECT-WISE AVERAGE
# ==========================================

plt.figure(figsize=(9, 5))

sns.barplot(
    x=subject_averages.index,
    y=subject_averages.values
)

plt.title("Subject-Wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.savefig("outputs/charts/subject_average.png")

plt.show()
plt.close()


# ==========================================
# CHART 6: GRADE DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 5))

sns.barplot(
    x=grade_counts.index,
    y=grade_counts.values
)

plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")

plt.savefig("outputs/charts/grade_distribution.png")

plt.show()
plt.close()


# ==========================================
# SAVE PROCESSED DATASET
# ==========================================

df.to_csv(
    "outputs/cleaned_students.csv",
    index=False
)


# ==========================================
# GENERATE FINAL ANALYSIS REPORT
# ==========================================

with open(
    "outputs/reports/analysis_report.txt",
    "w"
) as file:

    file.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Students: {len(df)}\n")

    file.write(
        f"Class Average: {class_average:.2f}\n"
    )

    file.write(
        f"Highest Average: {highest_average:.2f}\n"
    )

    file.write(
        f"Lowest Average: {lowest_average:.2f}\n"
    )

    file.write(
        f"Average Attendance: {average_attendance:.2f}%\n"
    )

    file.write(
        f"Average Study Hours: {average_study_hours:.2f}\n"
    )

    file.write(
        f"Class Pass Percentage: {pass_percentage:.2f}%\n"
    )


    # Subject-wise Average Marks
    file.write("\nSUBJECT-WISE AVERAGE MARKS\n")
    file.write("-" * 35 + "\n")

    file.write(
        f"Math Average: {subject_averages['math_score']:.2f}\n"
    )

    file.write(
        f"Science Average: {subject_averages['science_score']:.2f}\n"
    )

    file.write(
        f"English Average: {subject_averages['english_score']:.2f}\n"
    )

    file.write(
        f"Best Performing Subject: {best_subject}\n"
    )

    file.write(
        f"Weakest Performing Subject: {weakest_subject}\n"
    )


    # Grade Distribution
    file.write("\nGRADE DISTRIBUTION\n")
    file.write("-" * 35 + "\n")

    for grade, count in grade_counts.items():

        file.write(
            f"Grade {grade}: {count} Students\n"
        )


    # Top 5 Students
    file.write("\nTOP 5 STUDENTS\n")
    file.write("-" * 35 + "\n")

    for _, student in top_students.head(5).iterrows():

        file.write(
            f"{student['student_id']}: "
            f"{student['average_marks']:.2f} "
            f"({student['grade']})\n"
        )


    # Low Attendance Students
    file.write("\nSTUDENTS WITH LOW ATTENDANCE\n")
    file.write("-" * 35 + "\n")

    for _, student in low_attendance.iterrows():

        file.write(
            f"{student['student_id']}: "
            f"{student['attendance']}%\n"
        )


print("\nAnalysis Report Generated Successfully!")
print("Project Completed!")
