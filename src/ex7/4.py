# Write a function ‘checkaddress’ that parses the list of email addresses below and prints only the
# valid mail addresses (only the first 5 in the list are “valid” and should be allowed to pass by your
# regex). Use regular expressions for this exercise.
#
# testcases = ['johan.vanbauwel@thomasmore.be', \
#    johan.van.bauwel@thomasmore.be', 'info@telenet.BE', \
#   'duiven.bond@com.com.com', 'r123456@Student.thomasmore.be', \
#   '!TEST.be', 'info@test.belgium', 'info@!.com', 'infotest.com', \
#   'info@test.be$', 'ET@phone.hom.3', '@fundum.be']
import re

testcases = ['johan.vanbauwel@thomasmore.be',
             'johan.van.bauwel@thomasmore.be', 'info@telenet.BE',
             'duiven.bond@com.com.com', 'r123456@Student.thomasmore.be',
             '!TEST.be', 'info@test.belgium', 'info@!.com', 'infotest.com',
             'info@test.be$', 'ET@phone.hom.3', '@fundum.be'
             ]


def checkaddress(email: str):
    return re.match(r"^[a-z0-9.]+@[a-z]+(\.[a-z]+)*\.[a-z]{2,3}$", email, flags=re.IGNORECASE) is not None


for email in testcases:
    if checkaddress(email):
        print(email)
