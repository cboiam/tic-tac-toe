class PlayerMovedOutOfItsTurnException(Exception):

    def __init__(self):
        self.message = "You can't move in other players turn!"
