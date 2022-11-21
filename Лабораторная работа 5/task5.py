import random
import string


def get_random_password() -> str:
    str_ = string.ascii_lowercase + string.ascii_uppercase + string.digits
    list_ = random.sample(str_, 8)
    return "".join(list_)


print(get_random_password())
