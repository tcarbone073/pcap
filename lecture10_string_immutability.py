"""
Strings are immutable.
"""

# This will fail
my_var= 'abcdefg'
my_var[0] = 'j'

# This is how to mutate strings
my_var = 'j' + my_var[1:]
