import asyncio

@asyncio.coroutine
def schedule_delayed(task, delay, asyncio):
    yield from asyncio.sleep(delay)
    task.execute()

class AsyncScheduler:
    
    def __init__(self, asyncio, delay):
        self.delay = delay
        self.asyncio = asyncio
        
    def schedule(self, task):
        self.asyncio.ensure_future(schedule_delayed(task, self.delay))
        
