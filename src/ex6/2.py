# Write a function to count the occurrences of each word in a given sentence. Try to print each word
# with its corresponding frequency on a separate line.
# Example:
#   Input: 'Python is great, it is the best scripting language
#           in the world, and we love to learn it!'
#   Output:
#       {'Python': 1,
#       'and': 1,
#       'best': 1,
#       'great,': 1,
#       'in': 1,
#       'is': 2,
#       'it': 1,
#       'it!': 1,
#       'language': 1,
#       'learn': 1,
#       'love': 1,
#       'scripting': 1,
#       'the': 2,
#       'to': 1,
#       'we': 1,
#       'world,': 1}

def count(s: str):
    dc = {}

    for word in s.split():
        if dc.get(word) is None:
            dc[word] = 1
        else:
            dc[word] += 1

    return dc


dc_count = count("Python is great, it is the best scripting language in the world, and we love to learn it!")

print(", \n".join(str(dc_count).split(", ")))
