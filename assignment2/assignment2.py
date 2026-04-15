# task2 csv file
import csv

def read_employees():
    dic = {}
    rows = []

    dic.setdefault('rows', []) #https://www.geeksforgeeks.org/python/appending-to-list-in-python-dictionary/

    try: 
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)

            fields = next(reader)
            dic['fields'] = fields #column headers

            for row in reader:
                rows.append(row)
                dic['rows'].append(row)

            return dic
        
    except Exception as e:
        print(f"Error is: {e}")


employees = read_employees()
#print(employees) #will comment this out for final submission

#task 3 - column index
def column_index(string):
    return employees['fields'].index(string)

employee_id_column = column_index("employee_id")
#print(employee_id_column) #will comment this out for final submission

#task4 - find employee first name
def first_name(row_number):
    column = column_index('first_name')
    return employees['rows'][row_number][column]

#task5 - find employee, function in function
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees['rows']))

    return matches

#task6 - find employee with lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees['rows']))
    return matches

#task7 - sort rows by last_name using lambda
def sort_by_last_name():
    last_name = column_index('last_name')
    employees['rows'].sort(key=lambda row: row[last_name])
    return employees['rows']

#print(sort_by_last_name()) #will comment this out for final submission


#task8 - dict for an employee
def employee_dict(row):
    employ_dic = {}

    combined_info = tuple(zip(employees['fields'],row))[1:] #https://www.w3schools.com/python/ref_func_zip.asp
    for key, value in combined_info:
        employ_dic[key] = value
    
    return employ_dic

#print(employee_dict(employees["rows"][0])) #['1', 'Cindy', 'Wade', '+222 656-486-3727'] is the row example


#task9 - dict of dicts, all employees
def all_employees_dict():
    dic = {}

    for row in employees['rows']:
        dic[row[column_index('employee_id')]] = employee_dict(row)
    return dic

#print(all_employees_dict()) #checking if it looks right, #will comment this out for final submission

#task10 - os module 
import os
def get_this_value():
    return os.environ.get('THISVALUE')

#task11 - creating my own module
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("messiIsTheGoat")
#print(custom_module.secret) #output is messiIsTheGoat, #will comment this out for final submission

#task12 - reading minutes1 and minutes2 
def read_minutes():

    def read_file(f):
        general_dict = {}
        general_rows = []
        general_dict.setdefault('rows', [])

        with open(f, 'r') as file: 
            reader = csv.reader(file)
            fields = next(reader)

            general_dict['fields'] = fields
            for row in reader:
                general_rows.append(row)
                general_dict['rows'].append(tuple(row))

        return general_dict

    minutes1_dict = read_file('../csv/minutes1.csv')
    minutes2_dict = read_file('../csv/minutes2.csv')

    return minutes1_dict, minutes2_dict


minutes1, minutes2 = read_minutes()
# print(minutes1)
# print('----')
# print(minutes2)


#task13 - create minutes_swset
def create_minutes_set():
    min1_sets = set(minutes1['rows'])
    min2_sets = set(minutes2['rows'])

    combined_sets = min1_sets.union(min2_sets)

    return combined_sets 

minutes_set = create_minutes_set()

#task14 - conversion to datetime



#task15 - sorted list 
#check user comment about this task in the "discussion" channel on slack