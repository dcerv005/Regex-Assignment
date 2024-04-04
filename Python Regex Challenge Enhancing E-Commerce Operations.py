#Question 4
#Task 1
import re
'''
descriptions = ["Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

def tag_product(descriptions):
    electronics_pattern = r"\b(smartphone|television|headphones)"
    apparel_pattern = r"\b(t-shirt|pants|shoes)"
    home_kitchen_pattern = r"\b(knife|stove|chair)"
    product_descriptions= {}
    for description in descriptions:
        if re.search(electronics_pattern, description, re.IGNORECASE):
            product_descriptions["Electronics"]= [description]
        if re.search(apparel_pattern, description, re.IGNORECASE):
            product_descriptions["Apparel"]= [description]
        if re.search(home_kitchen_pattern, description, re.IGNORECASE):
            product_descriptions["Home & Kitchen"]= [description]
    return product_descriptions

print(tag_product(descriptions))

#Task 2
'''
price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
# Standardize all prices to 'USD XX.XX' format
# Your code here

pattern1 = r"\$(\d{2})\.(\d{2})"
pattern2 = r"(\d{2})\.(\d{2})\sUSD"
pattern3= r"(\d{1})\.(\d{2})\$"
new_pattern = r"USD \1.\2"
patterns= [pattern1, pattern2, pattern3]

for pattern in patterns:
    price_data= re.sub(pattern, new_pattern, price_data)

print(price_data) 
