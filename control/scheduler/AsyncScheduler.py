import asyncio

@asyncio.coroutine
def schedule_delayed(task, delay):
    yield from asyncio.sleep(delay)
    task.execute()

class AsyncScheduler:
    
    def __init__(self, delay):
        self.delay = delay
        
    def schedule(self, task):
        asyncio.async(schedule_delayed(task, self.delay))
        
