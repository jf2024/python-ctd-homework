#task1 

#create dataframe from dictionary
import pandas as pd

first_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(first_data)
#print(task1_data_frame)
print("----------")

#add new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
#print(task1_with_salary)
print("----------")

#modify existing columnt
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
#print(task1_older)
print("----------")

#save as csv
task1_older.to_csv('employees.csv', index=False)
csv_file = pd.read_csv("employees.csv")
#print(csv_file.head())
print("----------")

#task2 

#read data from csv file
task2_employees = pd.read_csv("employees.csv")
#print(task2_employees.head())
print("----------")

#read from json file
json_employees = pd.read_json("additional_employees.json")
#print(json_employees)
print("----------")

#combine json and csv files
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
#print(more_employees)
print("----------")

#task3 - data inspection
#use head() method
first_three = more_employees.head(3)
#print(first_three)
print("----------")

#use tail() method
last_two = more_employees.tail(2)
#print(last_two)
print("----------")

#shape
employee_shape = more_employees.shape
#print(employee_shape)
print("----------")

#info
more_employees.info()

#task4 - data cleaning
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)
clean_data = dirty_data.copy()
print('---------')

#remove duplicates
#got some help here; https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
clean_data.drop_duplicates(inplace=True)
#print(clean_data)

#convert age to numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
#clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].median())

#convert salary to numeric
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].replace("unknown", 'NaN')
clean_data['Salary'] = clean_data['Salary'].replace("n/a", 'NaN')

#fill in missing numeric values
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

# convert to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed', errors='coerce')

# strip whitespace and standarize names
clean_data['Department'] = clean_data['Department'].str.strip()
clean_data['Department'] = clean_data['Department'].str.upper()

clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Name'] = clean_data['Name'].str.upper()

print(clean_data)
