#  *args function - receives a variable number of arguments and prints them one by one

# def sample_function(*args):
#     for i in args:
#         print(i)
#
# sample_function(1,2,3,4,5, "Shashi")

#  **kwargs function - receives a variable number of keyword arguments and prints then one by one

# def sample_function(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# sample_function(name="Shashi", exp="10 years", age=32)

def sample(name, experience, location):
    print(name, experience, location)

d={"name":"Shashi", "experience":"10 years", "location":"India"}
sample(**d)

