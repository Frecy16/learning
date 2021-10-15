class FormatError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '密码长度必须在{}到{}位之间'.format(self.x, self.y)
