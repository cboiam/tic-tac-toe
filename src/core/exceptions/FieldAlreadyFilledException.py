class FieldAlreadyFilledException(Exception):

    def __init__(self):
        self.message = "Field must be empty to receive a value!"
