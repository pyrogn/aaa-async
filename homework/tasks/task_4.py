async def task_1(i: int):
    if i == 0:
        return "1"

    if i > 5:
        return "1" + await task_2(i // 2)
    else:
        return "1" + await task_2(i - 1)


async def task_2(i: int):
    if i == 0:
        return "2"

    if i % 2 == 0:
        return "2" + await task_1(i // 2)
    else:
        return "2" + await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212

    # but I guess it should be done without changing coroutines. Right?
    return int(await task_1(i))


if __name__ == "__main__":
    import asyncio

    res = asyncio.run(coroutines_execution_order(7))
    print(res)
