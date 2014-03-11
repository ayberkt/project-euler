first_element = 1
other_element = 1
temp = 0
count = 2 # Initialized with first two elements.
while True:
    count += 1
    temp = other_element
    other_element = first_element + other_element
    first_element = temp

    if len(str(other_element)) >= 1000:
        print count
        break