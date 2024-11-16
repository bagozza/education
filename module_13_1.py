import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    champ_1 = asyncio.create_task(start_strongman('Alexandr ibn Isaak', 6))
    champ_2 = asyncio.create_task(start_strongman('Boris', 2))
    champ_3 = asyncio.create_task(start_strongman('Semen', 4))
    await champ_1
    await champ_2
    await champ_3

start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'Время соревнований {round(finish - start, 2)} секунд')
