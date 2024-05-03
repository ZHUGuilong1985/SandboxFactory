
class Crud:
    '''
    CRUD class

    '''
    @staticmethod
    def translate_command(self, command):
        # translate command

        pass

    def __init__(self):
        pass

    def command_input(self):
        command = input("Enter command: ")
        command_dict = self.parse_command(command)
        if command_dict['command'] == "create":
            self.create()
        elif command_dict['command'] == "read":
            self.read()
        elif command_dict['command'] == "update":
            self.update()
        elif command_dict['command'] == "delete":
            self.delete()

    def create(self, name, **kw):

        pass

    def read(self):
        # show
        pass

    def update(self):
        # modify
        pass

    def delete(self):
        pass

    def parse_command(self, command):
        pass

    '''
    command, object, parameters...
    create material: name, 7075; price, 20; unit, pcs.
    '''
