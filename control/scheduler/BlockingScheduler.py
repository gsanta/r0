import asyncio
import concurrent.futures
import sys
import time

def run_blocking(blockingTask):
    print('run_blocking')
    blockingTask.execute()

@asyncio.coroutine
def schedule_blocking(blockingTask, executor, eventLoop):
    print('schedule_blocking')
    task = eventLoop.run_in_executor(executor, run_blocking, blockingTask)
    
    completed, pending = yield from asyncio.wait([task])
    results = [t.result() for t in completed]
    
@asyncio.coroutine
def slow_operation(future):
    print('slow operation')
    yield from asyncio.sleep(1)
    future.set_result('Future is done!')

class BlockingScheduler:

    def __init__(self, asyncio, eventLoop, executor):
        self.asyncio = asyncio
        self.eventLoop = eventLoop
        self.executor = executor

    def schedule(self, task):
        print('schedule')
#         future = self.asyncio.Future()
#         self.asyncio.ensure_future(slow_operation(future))
        self.asyncio.ensure_future(schedule_blocking(task, self.executor, self.eventLoop))