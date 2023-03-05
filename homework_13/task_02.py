import re


def is_date(string):
    return re.fullmatch(r'(\d{1,2})-(\d{1,2})-(\d{4})', string) is not None


if __name__ == '__main__':
    assert is_date('23-12-2020')
    assert is_date('29-05-2009')

