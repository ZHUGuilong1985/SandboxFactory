# instance class

from element import Element


class Definition(Element):

    def __init__(self, parent, name, description, solution):
        '''
        name:
        id:
        description:
        solution:    
        parent:      
        '''
        super().__init__(parent)
        pass


def main():
    d = Definition('test', 'test', 'test')
    print(d.id)
    print('Done.')


if __name__ == '__main__':
    main()
