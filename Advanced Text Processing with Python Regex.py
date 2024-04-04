#Question 3
#Task 1

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
occupation = re.search(r'Occupation: (\w+)', text)
print(occupation.group(1))

#Task 2
urls = ["https://example.com", "www.example.com", "http://test.com"]
# Validate each URL in the list
# Your code here
valid_emails = []
invalid_emails = []
for url in urls:
    if re.match(r'^(http://|https://)', url):
        valid_emails.append(url)
    else:
        invalid_emails.append(url)

print(f"The valid emails are: {valid_emails}\nThe invalid emails are: {invalid_emails}")