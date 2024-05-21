from src.design.command.Command import Command

class MoveUpCommand(Command):
    def execute(self):
        print("Moving up...")
