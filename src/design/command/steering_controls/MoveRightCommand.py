from src.design.command.Command import Command

class MoveRightCommand(Command):
    def execute(self):
        print("Moving right...")
