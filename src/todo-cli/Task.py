#!usr/bin/env python3
class Task:
    def __init__(self, name, index: int, status: bool = False) -> None:
        self.name = name
        self.index = index
        self.status = status
        pass
