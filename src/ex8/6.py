# Write a program that:
# - writes the data structure below to a JSON file ‘students.json’
# - reads the JSON file ‘students.json’ into a data structure ‘mydata’
#
# data = {
#       'name': 'Alice',
#       'age': 20,
#       'courses': [
#      {
#           'name': 'Python',
#           'SP': 6
#      },
#      {
#           'name': 'DSP',
#           'SP': 6
#       }
#   ]
# }
#
# Next, create a function ‘addscore’ with the following arguments:
# - student_name
# - course
# - score
# - mydata
# The function ‘addscore’ has to add a score for a certain course taken by a certain student in the
# ‘mydata’ structure. Call the function using the arguments provided in the example below. Make
# sure you add the score for the right student, for the right course. Print the ‘mydata’ structure
# afterwards.
#
# Example:
#   addscore('Alice', 'Python', 20, mydata)
# Output:
#   {'name': 'Alice', 'age': 20, 'courses': [{'name': 'Python', 'SP': 6, 'score': 20}, {'name': 'DSP', 'SP': 6}]}

import json

data = {
    'name': 'Alice',
    'age': 20,
    'courses': [{
        'name': 'Python',
        'SP': 6
    }, {
        'name': 'DSP',
        'SP': 6
    }]
}


def read():
    with open('students.json', 'r') as f:
        return json.load(f)


def write(d):
    with open("students.json", 'w') as f:
        json.dump(d, f)


def addscore(student_name: str, course: str, score: int, d):
    if d["name"] == student_name:
        for i, c in enumerate(d["courses"]):
            if c["name"] == course:
                c["score"] = score
                return


write(data)

mydata = read()
addscore('Alice', 'Python', 20, mydata)
print(mydata)
