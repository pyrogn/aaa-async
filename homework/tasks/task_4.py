import functools


async def task_1(i: int):
    if i == 0:
        return

    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


async def task_2(i: int):
    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212

    # Я думал, что нельзя менять task_1 и task_2, поэтому задекорировал функции
    # с добавлением side effect на обновление списка
    # Куда проще это сделать, добавив значение 1 или 2 в return task_1, task_2
    func_calls = []

    def trace_call(val_to_list):
        def decorator(f):
            @functools.wraps(f)
            async def wrapper(*args, **kwargs):
                func_calls.append(val_to_list)  # side effect
                return await f(*args, **kwargs)  # will be None

            return wrapper

        return decorator

    global task_1, task_2
    task_1 = trace_call("1")(task_1)
    task_2 = trace_call("2")(task_2)

    await task_1(i)  # оставляет следы

    return int("".join(func_calls))


if __name__ == "__main__":
    import asyncio

    res = asyncio.run(coroutines_execution_order(7))
    print(res)
