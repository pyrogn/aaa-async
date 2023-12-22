import abc
import asyncio
from concurrent.futures import ThreadPoolExecutor


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model
        self.pool_executor = ThreadPoolExecutor(max_workers=2)  # больше и не надо

    async def handle_request(self) -> None:
        # Модель выполняет некий тяжёлый код (ознакомьтесь с ним в файле тестов),
        # вам необходимо добиться его эффективного конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины handle_request не слишком сильно
        # отличается от времени исполнения нескольких таких корутин, запущенных конкурентно.
        #
        # YOU CODE GOES HERE
        # Пояснение:
        # Если бы тяжелые вычисления запускались в питоне (кишки интерпретатора),
        # то код не стал бы быстрей синхронного. Но в данном случае вычисления происходят
        # вне интерпретатора, поэтому GIL на них не влияет.
        event_loop = asyncio.get_event_loop()
        task = event_loop.run_in_executor(self.pool_executor, self._model.compute)
        await task
