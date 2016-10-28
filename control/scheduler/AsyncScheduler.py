
async def schedule_delayed(task, delay, asyncio):
    await asyncio.sleep(delay)
    task.execute()

class AsyncScheduler:
    
    def __init__(self, asyncio, delay):
        self.delay = delay
        self.asyncio = asyncio
        
    def schedule(self, task):
        self.asyncio.ensure_future(schedule_delayed(task, self.delay))
        
