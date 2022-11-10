# Write a function ‘maskaddress’ that parses the list of email addresses from the previous
# assignment and prints each email address (regardless of the validity) but with each ‘.’ replaced by
# ‘(DOT)’ and each ‘@’ replaced by ‘(AT)’. Use regular expressions for this exercise.
#
# The output should look like:
# johan(DOT)vanbauwel(AT)thomasmore(DOT)be
# johan(DOT)van(DOT)bauwel(AT)thomasmore(DOT)be
# info(AT)telenet(DOT)BE
# duiven(DOT)bond(AT)com(DOT)com(DOT)com
# r123456(AT)Student(DOT)thomasmore(DOT)be
# !(AT)TEST(DOT)be
# info(AT)test(DOT)belgium
# info(AT)!(DOT)com
# infotest(DOT)com
# info(AT)test(DOT)be$
# ET(AT)phone(DOT)hom(DOT)3
# (AT)fundum(DOT)be
import re

testcases = ['johan.vanbauwel@thomasmore.be',
             'johan.van.bauwel@thomasmore.be', 'info@telenet.BE',
             'duiven.bond@com.com.com', 'r123456@Student.thomasmore.be',
             '!TEST.be', 'info@test.belgium', 'info@!.com', 'infotest.com',
             'info@test.be$', 'ET@phone.hom.3', '@fundum.be'
             ]


def maskaddress(s: str):
    return re.sub(r"[@.]", lambda mo: "(AT)" if mo.group(0) == "@" else "(DOT)", s)


for email in testcases:
    print(maskaddress(email))
