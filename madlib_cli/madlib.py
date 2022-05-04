def read_template(x):
    try:
        file  = open(x)
        contents = file.read()
        return contents
    except FileNotFoundError:
        raise FileNotFoundError
        print("file not found")

def parse_template(actual_stripped, actual_parts):
    actual_stripped = ("It was a {} and {} {}."), 
    actual_parts = filter(lambda x: x.startswith(("{")))
    print (actual_parts)
    return actual_stripped, actual_parts


def merge(x, y):
   return x.format(*y)
'''

actual_stripped

actual_parts


'''


