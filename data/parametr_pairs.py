import os
from typing import Any

from allpairspy import AllPairs

from data.generator import gen


class ParametrPairs:
    def __init__(self):
        self.username: str = os.getenv("AUTH_LOGIN")
        self.password: str = os.getenv("AUTH_PASSWORD")

    def parametr(self) -> list[list[str]]:
        parametr = [
            ["", " ", f"{self.username}", gen.string_random(100)],
            ["", " ", f"{self.password}", gen.string_random(100)],
        ]
        return parametr

    def testdata(self) -> list[tuple[Any, ...]]:
        return [
            tuple(combination)
            for combination in AllPairs(
                self.parametr(),
                filter_func=(
                    lambda row: not (self.username in row and self.password in row)
                ),
            )
        ]
