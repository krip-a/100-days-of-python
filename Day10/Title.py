# convert all strings to title case 

def format_na(f_name, l_name):
    """Take a first and last name and format it to
    return the title case version of the name"""
    # this is how documentation is written as docstring

    name = f_name.title() + " " + l_name.title()
    return name

print(format_na("aliCe", "BoB")) 

# print (format_na(input("What is your name?"), input("What is your last name? ")))

my_fav_func = format_na     # storing the function