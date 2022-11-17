# Given the file Training_01.txt, which is a text file of image paths of a dataset used in training a
# neural network, create a program that keeps track of how many images of each image category
# there are (such as ‘abbey’, see file content) and – of course – also keeps track of how many image
# categories are present.
# The results have to be written as a dictionary to a JSON file ‘categories.json’. Print the total
# amount of categories to the console.
# You are obliged to use a regular expression to filter the image categories from the paths in
# each line.

import json
import re

categories = {}

with open("Training_01.txt", "r") as f, open("categories.json", 'w') as fout:
    for line in f:
        cat = re.search(r"/\w/(\w+(?:/\w+)?)/\w+\.\w+", line).group(1)

        if categories.get(cat) is None:
            categories[cat] = 0

        categories[cat] += 1

    json.dump(categories, fout)
