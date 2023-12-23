from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):  # coroutine function
        return await f()
    elif isinstance(f, Task):  # asyncio task
        return await f
    elif isinstance(f, Coroutine):  # coroutine object
        return await f
    else:
        raise ValueError("invalid argument")
