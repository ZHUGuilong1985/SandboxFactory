from element import Element


class Definition(Element):

    def __init__(self, parent, sbid=None, name=None, description=None):
        '''
        name:
        sbid:
        description:
        solution:    
        parent:      
        '''
        super().__init__(parent, sbid)
        self.name = name
        self.desription = description


def main():
    d = Definition('test', 'test', 'test')
    print(d.sbid)
    print('Done.')


if __name__ == '__main__':
    main()
