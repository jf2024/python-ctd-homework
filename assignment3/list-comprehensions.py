#task3

import csv

with open('../csv/employees.csv', 'r') as file:
    rows = []
    reader = csv.reader(file)

    fields = next(reader) #to skip the headers and start with the first row of an employee
    for row in reader:
        rows.append(row)

#print(rows)

first_last_names_list = [row[1] + " " + row[2] for row in rows]
print(first_last_names_list)
print(len(first_last_names_list))

print('------------------------')

contain_e = [name for name in first_last_names_list if 'e' in name]
print(contain_e)
print(len(contain_e))
        