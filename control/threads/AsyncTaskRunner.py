async def run_delayed(task, delay):
    await asyncio.sleep(delay)
    task.execute()

async def run_periodic(task, period, delayFirstRun):
    if delayFirstRun == False and task.isComplete() == False:
        task.execute()

    while task.isComplete() == False:
        task.execute()


class AsyncTaskRunner:

    def __init__(self, asyncio):
        self.asyncio = asyncio

    def run(self, task, delay = 0):
        self.asyncio.ensure_future(run_delayed(task, delay))
    
    def run_periodic(self, task, period, delayFirstRun = True):
        run_periodic(task, period, delayFirstRun)
