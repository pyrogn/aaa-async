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

    res = []

    def value(val):
        def foo(f):
            async def wrapper(*args, **kwargs):
                o = await f(*args, **kwargs)
                res.append(val)
                return o

            return wrapper

        return foo

    global task_1, task_2
    task_1 = value("1")(task_1)
    task_2 = value("2")(task_2)
    await task_1(i)

    return int("".join(res)[::-1])


if __name__ == "__main__":
    import asyncio

    res = asyncio.run(coroutines_execution_order(7))
    print(res)
