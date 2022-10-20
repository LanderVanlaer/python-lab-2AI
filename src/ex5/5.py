# Write a program to remove all duplicates from a dictionary. Use the following dictionary as test
# data and print your result.
#
# students = {'id1':
#  {'name':'Tom',
#  'gender':'M',
#  'courses':'dsp, math, python'
#  },
# 'id2':
#  {'name': 'Alice',
#  'gender': 'F',
#  'courses': 'operating systems, math, python'
#  },
# 'id3':
#  {'name': 'Tom',
#  'gender': 'M',
#  'courses': 'dsp, math, python'
#  },
# 'id4':
#  {'name': 'Bob',
#  'gender': 'M',
#  'courses': 'math, python'
#  },
# }
#
# Output:
#   {
#       'id1': {'name': 'Tom', 'gender': 'M', 'courses': 'dsp, math, python'},
#       'id2': {'name': 'Alice', 'gender': 'F', 'courses': 'operating systems, math, python'},
#       'id4': {'name': 'Bob', 'gender': 'M', 'courses': 'math, python'}
#   }

students = {
    'id1': {
        'name': 'Tom',
        'gender': 'M',
        'courses': 'dsp, math, python'
    },
    'id2': {
        'name': 'Alice',
        'gender': 'F',
        'courses': 'operating systems, math, python'
    },
    'id3': {
        'name': 'Tom',
        'gender': 'M',
        'courses': 'dsp, math, python'
    },
    'id4': {
        'name': 'Bob',
        'gender': 'M',
        'courses': 'math, python'
    },
}

for i, k in enumerate(students.copy()):
    for k2, v2 in list(students.items())[i + 1::]:
        if students[k] == v2:
            del students[k2]

print(students)
