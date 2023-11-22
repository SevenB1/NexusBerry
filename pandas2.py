import pandas as pd
import numpy as np
#Two collections are in pandas module.
#i) Series, --- Its a single dimension data collection, it represents one column data
#ii) DataFrame, --- Its two dimesnional data collection, it represents rows and columns
#Series represents one column in the DataFrame

grades_series = pd.Series([87,77,66,55,97,59])
print(type(grades_series))
print(grades_series)

grades_series = pd.Series([87,77,66,55,97,59],index=['Mathematics','Physics','Chemistry','English','History','French'])
print(grades_series)

calories = {"day1":430,"day2":300,"day3":380}
calories_series = pd.Series(calories)
print(calories_series)

print(f'Grades Average:{grades_series.mean():.2f}')
print(f'Grades Min:{grades_series.min()}')
print(f'Grades Max:{grades_series.max()}')
print(f'Grades Count:{grades_series.count()}')
print(f'Grades std:{grades_series.std():.2f}')
print(f'Grades Median:{grades_series.median()}')
#
print("Grades Statistics\n",grades_series.describe())


#create a Series of 100 random integers in between 1 and 1000
rand_series = pd.Series(np.random.randint(1,1000,100))
print(rand_series)

#DataFrame, rows, and columns
calories_df = pd.DataFrame(calories_series)
print(type(calories_df))
print(calories_df)

grades_dict = {'Ahmad':[76,87,98],'Zubair':[99,56,77],'Qasim':[55,66,88]}
grades_df = pd.DataFrame(grades_dict,index=['Mathematics','Physics','Chemistry'])
print(grades_df)

print("Marks of Ahmad\n",grades_df['Ahmad'])
print("Marks of Mathematics")
print(grades_df.loc['Mathematics'])

print("Marks of Physics")
print(grades_df.loc['Physics'])

print("Marks of Chemistry")
print(grades_df.loc['Chemistry'])

print(grades_df.loc['Mathematics':'Chemistry'])

print("Marks of Mathematics")
print(grades_df.iloc[0])

print("Marks of Physics")
print(grades_df.iloc[1])

print("Marks of Chemistry")
print(grades_df.iloc[2])

print(grades_df.iloc[0:2])

#print the grades in the dataframe which are >=70
print(grades_df >= 70)
print(grades_df[grades_df >= 70])

grades_dict = {'Mathematics':[76,87,98],'Physics':[99,56,77],'Chemistry':[55,66,88]}
grades_df = pd.DataFrame(grades_dict,index=['Ahmad','Zubair','Qasim'])
print(grades_df)

# print(grades_df[grades_df['Mathematics'] >= 80][['Mathematics']])

# #print the student whose marks in physics is greater than 90 and in chemistry greater than 50

# print(grades_df[(grades_df['Physics'] > 90) & (grades_df['Chemistry'] > 50)][['Physics','Chemistry']])

#reproduce the above results through dataframe loc attribute
print(grades_df.loc[grades_df['Physics'] >=80,['Physics']])

# #Marks in Mathematics <= 80 and chemistry <=80 display only Mathematics and chemistry

# print(grades_df[(grades_df['Mathematics'] >= 80) | (grades_df['Chemistry'] >= 80)][['Mathematics', 'Chemistry']])

