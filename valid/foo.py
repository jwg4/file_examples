from sys import argv


def add_foo_to_string(s):
    """
    Return the same string but with 'foo' at the end.
    """
    return s + "foo"


if __name__ == "__main__":
    for arg in argv:
        print(add_foo_to_string(arg))
