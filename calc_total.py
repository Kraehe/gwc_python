list = [3,4,5,4,6,7]    # defines a list

def calc_total(list):   # defines the function 'calc_total' and takes in the parameter 'list'
    total = 0           # initializes a 'total' variable
    for num in list:    # loops through each value of the list given in the parameter
        total += num    # adds each value to the 'total' variable
    return total        # returns the total variable
print(calc_total(list)) # prints what the calc_total returns when given the list
