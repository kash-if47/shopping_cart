from dataclasses import dataclass
from typing import List


@dataclass
class Basket(object):
    items: List

    def total(self):
        return len(self.items)