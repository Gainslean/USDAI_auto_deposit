import asyncio
import random
from datetime import datetime
from client import Client
from config import Chain_id, chain_name, rpc_url, explorer_url,USDAI
from datetime import datetime, time, timezone

target = time(14, 59, 30)  # целевое время UTC  ЧАСЫ/МИНУТЫ/СЕКУНДЫ , ТИПО БУДЕТ РАВНО 15:12:25


class DEPOSIT:
    def __init__(self, client: Client):
        self.client = client
        self.usdai = self.client.get_contract(
            contract_address="0x0A1a1A107E45b7Ced86833863f482BC5f4ed82EF",
            abi=USDAI
        )


    async def limit(self): # трекает общий лимит саплая, хз будет работать или нет

        while True:

            deposit_limit = await self.usdai.functions.supplyCap().call()/10**18

            if deposit_limit > 578430001:
                print(f"Текущий лимит на вклад {deposit_limit}    {datetime.now().strftime('%H:%M:%S')}")
                return True
            else:
                print(f"Текущий лимит на вклад {deposit_limit}    {datetime.now().strftime('%H:%M:%S')} - ")
                await asyncio.sleep(1)

    async def approve(self): # Делает апрув юсдс

        amount = random.randint(70000 * 10**6 , 999999999999 * 10**6)

        await self.client.make_approve("0xaf88d065e77c8cC2239327C5EDb3A432268e5831","0x0A1a1A107E45b7Ced86833863f482BC5f4ed82EF", amount)

        print(f"Успешно сделал апрув {amount/10**6}")


    async def time(self): #ждет опредленное время для запуска

        while True:
            now_utc = datetime.now(timezone.utc).time()

            formatted_utc = now_utc.strftime("%H:%M:%S")
            print(f"Время сейчас {formatted_utc} UTC")

            if now_utc < target:
                print(f"Еще рано, ждем {target}")
                await asyncio.sleep(1)
            else:
                print(f"Наступило {target} UTC")
                return True


    async def supply(self): # Основная функция депозита

        #await self.approve()  # апрув рандом суммы

        #await self.limit()  # ожидание расширения лимита

        await self.time()  # ожидание время для старта

        amount = await self.client.get_balance_erc("0xaf88d065e77c8cC2239327C5EDb3A432268e5831")

        print(f"Баланс {self.client.address} равен = {amount / 10**6} USDC")

        if amount == 0:
            print(f"Депать нечего")
            return False


        for attempt in range(1, 300):  # 300 попытки
            try:
                print(f"Попытка {attempt}/300: депозит {amount / 10 ** 6} USDC...")

                # Формируем транзакцию
                txn = await self.usdai.functions.deposit(
                    "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
                    amount,
                    int(amount * 0.99985), # минмалка на получение 0,015% слип
                    self.client.address
                                                         ).build_transaction(
                    await self.client.prepare_tx()
                )

                # Отправляем транзакцию
                tx_hash = await self.client.send_transaction(txn, need_hash=True)
                print(f"Транзакция успешно отправлена: {tx_hash}")

                # Ожидаем подтверждения
                success = await self.client.wait_tx(tx_hash)
                if success:
                    print(f"✅ Успешно сделал вклад {amount / 10 ** 6} USDC")
                    return True  # Выходим из функции, если успех

            except Exception as e:
                print(f"❌ Ошибка при отправке транзакции (попытка {attempt}): {e}")

            # Если неудачно и не последняя попытка — ждем 1 секунду
            if attempt < 299:
                await asyncio.sleep(3)

        print("⚠️ Все 300 попытки депозита не удались.")
        return False



chain_name = "Arbitrum" # Arbitrum Optimism Base Ethereum Mantle

proxy = '' # ПО ФАКТУ НЕ НУЖНЫ ТУТ
rpc_url = rpc_url[chain_name]
chain_id = Chain_id[chain_name]
explorer_url = explorer_url[chain_name]

async def start():

    with open("wallets.txt", "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.readlines()]

    private_keys = [ln for ln in lines]

    tasks = []
    for pk in private_keys:

        w3_client = Client(private_key=pk, proxy=proxy, chain_name=chain_name, chain_id=chain_id,
                           explorer_url=explorer_url, rpc_url=rpc_url)
        swap_client = DEPOSIT(client=w3_client)

        task = asyncio.create_task(swap_client.supply())
        tasks.append(task)

    await asyncio.gather(*tasks, return_exceptions=True)


asyncio.run(start())