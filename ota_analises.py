# %%
# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# Import data
students = pd.read_csv('student-mat.csv', delimiter=';')
# %%
# Print summary statistics for all columns
print(students.describe())
print(students.columns)
# %%
#Creating a new DF filtering the infos i want
students_new = students[['address', 'Mjob', 'Fjob', 'absences', 'G3']]
print(students_new)
 # %%
 
print(students_new.head())
print(students_new.describe())
 # %%
 # Calculate mean
math_grade_mean = students_new.G3.mean()
print(math_grade_mean)
 # %%
 # Calculate median
math_grade_median = students_new.G3.median()
print(math_grade_median)
 # %%
 # Calculate mode
math_grade_mode = students_new.G3.mode()[0]
print(math_grade_mode)
 # %%
 # Calculate range
math_grade_range = students_new.G3.max() - students_new.G3.min()
print(math_grade_range)
# %%
#Calculate de standart deviation
math_grade_deviation = students_new.G3.std()
print(math_grade_deviation)
# %%
#Calculate de MAD
math_grade_mad = np.mean(np.abs(students_new['G3'] - math_grade_mean))
print(math_grade_mad)
# %%
# Create a histogram of math grades
sns.histplot(x = 'G3', data = students_new)
plt.show()
plt.clf()
# %%
# Create a box plot of math grades
sns.boxplot(x = 'G3', data = students_new)
plt.show()
plt.clf()
# %%
# Calculate number of students with mothers in each job category
mothers_job = students_new.Mjob.value_counts()
print(mothers_job)
print(students_new.Mjob.value_counts(normalize=True))
# %%
# Create bar chart of Mjob
sns.countplot(x = 'Mjob', data = students_new)
plt.show()
plt.clf()
# %%
# Create pie chart of Mjob
students_new.Mjob.value_counts().plot.pie()
plt.show()
# %%