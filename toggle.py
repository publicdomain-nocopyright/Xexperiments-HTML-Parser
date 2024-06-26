# Toggle must be aware of its value in the context instead of being global variable. If a different function call, it should reset itself. It should be unique to each function.

def togglere():
    state = True
    while True:
        yield state
        state = not state

# Using the generator
toggle_gen = togglere()

# First call to get initial state
print(next(toggle_gen))  # Output: True

# Subsequent calls to toggle state
print(next(toggle_gen))  # Output: False
print(next(toggle_gen))  # Output: True

# toggle() - returns False or True depending if used before in the context.
# The toggle function works on a context level and does not need an argument to be passed to it.
# The toggle function have internal variable to save state of boolean. A count variable can be usedto debug the context.
# If toggle() is inside another function, it resets internal variable.
def toggle():
    # Initialize a variable to keep track of state
    state = False
    count = 0
    
    def inner():
        nonlocal state  # Use nonlocal to modify the state variable in the enclosing scope
        nonlocal count
        count = count +1
        state = not state  # Toggle the state (True becomes False, False becomes True)
        return count  # Return the toggled state
    
    return inner  # Return the inner function

# Example usage:
toggle_func = toggle()

print("----")
print(toggle_func())  # First call, returns True



def ter():
    print(toggle_func())  # Second call, returns False
    print(toggle_func())  # Third call, returns True
ter()
print(toggle_func())  # Third call, returns True



def sectoggle():
    # Initialize a variable to keep track of state

    countz
    countz = countz +1
    state = not state  # Toggle the state (True becomes False, False becomes True)
    return countz  # Return the toggled state

print(sectoggle())