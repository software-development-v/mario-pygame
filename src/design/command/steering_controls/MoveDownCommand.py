from src.design.command.Command import Command

class MoveDownCommand(Command):
    def execute(self):
        print("Moving down...")
