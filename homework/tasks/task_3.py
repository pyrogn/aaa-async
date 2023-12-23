import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины, затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #

    tickets = await asyncio.gather(*coros)  # получаем результат от всех корутин
    keys = [ticket.key for ticket in sorted(tickets, key=lambda x: x.number)]
    return "".join(keys)


if __name__ == "__main__":  # для самотестирования

    async def just_return_ticket(t: Ticket) -> Ticket:
        return t

    tickets = [
        Ticket(number=2, key="мыла"),
        Ticket(number=1, key="мама"),
        Ticket(number=3, key="раму"),
    ]
    coros: list[Awaitable[Ticket]] = [just_return_ticket(t) for t in tickets]
    res = asyncio.run(coroutines_execution_order(coros))
    print(res)
