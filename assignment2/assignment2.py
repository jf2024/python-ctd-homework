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
#print(employee_id_column)

#task4 - find employee first name
def first_name(row_number):
    column = column_index('first_name')
    return employees['rows'][row_number][column]

#task5 - find employee, function in function
def employee_find(employee_id):

    def employee_match(row):
        #print(f"Checking row: {row}")
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees['rows']))

    return matches

#task6 - find employee with lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees['rows']))
    return matches