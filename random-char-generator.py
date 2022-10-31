import string
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase

    # choose from letters 123
    # letters = '123'
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str
