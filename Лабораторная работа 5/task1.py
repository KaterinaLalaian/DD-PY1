# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_ = [{"dec": value, "bin": bin(value), "oct": oct(value), "hex": hex(value)} for value in range(16)]
pprint(list_)
