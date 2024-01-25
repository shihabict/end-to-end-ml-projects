from ensure import ensure_annotations


def get_dict_prod(x: int, y: int) -> int:
    return x * y


@ensure_annotations
def get_proper_dict_prod(x: int, y: int) -> int:
    return x * y


if __name__ == '__main__':
    x = 2
    y = 4
    x1 = 2
    y2 = '4'
    print(get_dict_prod(x=x, y=y2))
    print(get_proper_dict_prod(x=x, y=y2))
