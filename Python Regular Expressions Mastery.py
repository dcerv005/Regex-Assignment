#Question 1
#Task 1
import re


text = '<span class="hljs-string">"Contact emails are: john.doe@example.com and jane.doe@example.com."</span>'
emails = re.findall(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', text, re.IGNORECASE)
print(emails)


#Task 2

log_data = '<span class="hljs-string">"12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."</span>'
#data = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\1-\2', log_data)
new_data = re.sub(r'@\w+', r"'[ANONYMOUS USER]'", re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\1-\2', log_data))
print(new_data)