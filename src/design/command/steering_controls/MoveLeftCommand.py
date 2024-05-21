from src.design.command.Command import Command

class MoveLeftCommand(Command):
    def execute(self):
        print("Moving left...")
