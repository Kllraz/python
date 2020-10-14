class MyException(Exception):
    def __init__(self, msg):
        self.txt = msg


class StringException(Exception):
    def __init__(self, msg):
        self.txt = msg