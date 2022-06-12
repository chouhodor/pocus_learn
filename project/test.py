import re

def get_integer(i):
    i = int(re.search(r'\d+', i).group())
    return i

print(get_integer('assfasf.asfasfa5'))

