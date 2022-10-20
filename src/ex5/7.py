# Define a function “merge” which can return a dictionary which is constructed from 2 lists (these are
# passed as arguments). Hint: use the zip() function!
# Example:
#       cities = ['Antwerpen', 'Lier', 'Mechelen', 'Brussel']
#       postalCodes = [2000, 2500, 2800, 1000]
#       print(merge(cities, postalCodes))
#       Output: {'Antwerpen': 2000, 'Lier': 2500, 'Mechelen': 2800, 'Brussel': 1000}

def merge(c, p):
    return dict(zip(c, p))


cities = ['Antwerpen', 'Lier', 'Mechelen', 'Brussel']
postalCodes = [2000, 2500, 2800, 1000]
print(merge(cities, postalCodes))
