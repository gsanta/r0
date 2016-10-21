
async def schedule_delayed(task, period, firstRunDelayed):
    if firstRunDelayed == False and task.isComplete() == False:
        task.execute()

    while task.isComplete() == False:
        task.execute()

class AsyncScheduler:
    
    def __init__(self, asyncio, delay):
        self.delay = delay
        self.asyncio = asyncio
        
    def schedule(self, task):
        self.asyncio.ensure_future(schedule_delayed(task, self.delay))
        