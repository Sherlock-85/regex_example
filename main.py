import re

message = ' For the best Python party in town call me at 415-867-5309 tomorrow, or at 415-555-9890!'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # d represents digit
match = phoneNumRegex.search(message)  # searches the message for matches
print(match.group())

print(phoneNumRegex.findall(message))

