# instance class

from element import Element


class Definition(Element):

    def __init__(self, name, description, solution):
        super().__init__()


def main():
    d = Definition('test', 'test', 'test')
    print(d.id)
    print('Done. ')


if __name__ == '__main__':
    main()
