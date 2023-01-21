from typing import Iterator, Optional

from pydantic import BaseModel


class ComputerModel(BaseModel):
    brand: str
    ram: str
    storage: str
    ssd: Optional[bool] = None


def demo_func(param) -> None:
    return f"demo function with {param}"


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
