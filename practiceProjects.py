def comma_code(items):
    # Handle the empty list case
    if not items:
        return ''
    
    # If there's only one item, return it without changes
    if len(items) == 1:
        return items[0]
    
    # Join all items with a comma and space, except the last item
    result = ', '.join(items[:-1])
    
    # Add 'and' before the last item
    result += ', and ' + items[-1]
    
    return result

# Test the function with the provided example
spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))  # Output: 'apples, bananas, tofu, and cats'

# Test the function with an empty list
print(comma_code([]))  # Output: ''
