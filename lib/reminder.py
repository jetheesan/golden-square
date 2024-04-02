class Reminder:
    def __init__(self, name):
        self.name = name

    def remind_me_to(self, task):
        pass
        self.task = task

    def remind(self):
        return f"{self.task}, {self.name}!"
        pass


reminder = Reminder("Kay")
