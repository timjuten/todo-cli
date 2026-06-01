#!usr/bin/env python3
class Task:
    def __init__(self, name, status: bool = False) -> None:
        self.name = name
        self.status = status
        pass

    def change_status(self):
        self.status = True
        print("The task is finished.")
