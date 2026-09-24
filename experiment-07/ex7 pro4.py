text = "HelloWorld"

uppercase = list(map(str.upper, text))

lowercase = list(map(str.lower, text))

unique = list(set(lowercase))
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Without duplicates:", unique)
