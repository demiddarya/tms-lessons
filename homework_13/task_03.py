import re


def is_float_number(string):
    return re.fullmatch(r'^[0-9]*[.,][0-9]+$', string) is not None


if __name__ == '__main__':
    assert is_float_number('4.5')
    assert is_float_number('20,45')
    assert is_float_number('1.0')