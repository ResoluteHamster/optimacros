import gmpy2


def calculate_factorial(value: int) -> str:
    result = gmpy2.factorial(int(value)).__format__('E')
    return result


if __name__ == '__main__':
    res = calculate_factorial(1000000)
    print(res, type(res))