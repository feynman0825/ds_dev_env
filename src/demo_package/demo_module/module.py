from typing import Iterator, Optional

from pydantic import BaseModel


class ComputerModel(BaseModel):
    brand: str
    ram: str
    storage: str
    ssd: Optional[bool] = None


def demo_func(param) -> None:
    """_summary_

    Args:
        param (_type_): _description_

    Returns:
        _type_: _description_
    """
    return f"demo function with {param}"


# In[]
from typing import Iterator, Optional


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


next(fib(5))
# TODO

# In[]

1 + 1
# %%
