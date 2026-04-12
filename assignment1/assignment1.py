# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator
def calc(num1, num2, operation="multiply"):

    try: 
        match operation: 

            case "add":
                return num1 + num2 

            case "subtract":
                return num1 - num2

            case "multiply":
                return num1 * num2 

            case "divide":
                return num1 / num2

            case "modulo":
                return num1 % num2

            case "int_divide":
                return num1 // num2

            case "power":
                return num1 ** num2
            
    except ZeroDivisionError:
        return "You can't divide by 0!"
    
    except TypeError:
        return "You can't multiply those values!"


# task4: data type conversion
def data_type_conversion(value, name):
    
    try:
        match name:

            case "int":
                return int(value)
            
            case "float":
                return float(value)
            
            case "str":
                return str(value)
            
    except ValueError:
        return f"You can't convert {value} into a int."

# task5: grading system, using *args
def grade(*args):
    try: 
        avg = sum(args) / len(args)

        #help here: https://stackoverflow.com/questions/69710333/is-there-a-way-to-match-inequalities-in-python-%E2%89%A5-3-10
        match avg: 
            case _ if avg >= 90:
                return "A"
            
            case _ if 80 <= avg <= 89:
                return "B"
            
            case _ if 70 <= avg <= 79:
                return "C"
            
            case _ if 60 <= avg <= 69:
                return "D"
            
            case _: 
                return "F"     
    except:
        return "Invalid data was provided."

#task6 use a for loop with a range
def repeat(string, count):
    new_string = ""
    for _ in range(count):
        new_string += string

    return new_string

#task 7 student scores using **kwargs
def student_scores(pos, **kwargs):
    match pos: 

        case "best":
            high = 0
            name = ""
            for key, value in kwargs.items():
                if value > high:
                    high = value
                    name = key

            return name 
        
        case "mean":
            return sum(kwargs.values()) / len(kwargs)

#task8 titleize, with string and list operations
def titleize(string):
    split_string = string.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    new_string = []

    for i, word in enumerate(split_string):
        if i == 0 or i == len(split_string) - 1: 
            new_string.append(word.capitalize())

        elif word not in little_words:
            new_string.append(word.capitalize())

        else:
            new_string.append(word)

    return " ".join(new_string)

#task9 hangman, string operations
def hangman(secret, guess):
    secret_split = list(secret)

    for i in range(len(secret_split)):
        if secret_split[i] not in guess:
            secret_split[i] = "_"

    return "".join(secret_split)

#task10 pig latin
def pig_latin(s):
    s_list = s.split()
    answer = []

    for word in s_list:
        if word[0] in "aeiou":
            answer.append(word + "ay")

        else:
            i = 0
            while i < len(word):
                if word[i:i + 2] == "qu":
                    i += 2
                    break

                elif word[i] in "aeiou":
                    break

                else:
                    i += 1

            answer.append(word[i:] + word[:i] + "ay")

    return " ".join(answer)
    

    


    
