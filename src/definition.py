# instance class

from element import Element


class Definition(Element):

    def __init__(self, parent, id=None, name=None, description=None):
        '''
        name:
        id:
        description:
        solution:    
        parent:      
        '''
        super().__init__(parent, id)
        self.name = name
        self.desription = description


def main():
    d = Definition('test', 'test', 'test')
    print(d.id)
    print('Done.')


if __name__ == '__main__':
    main()
