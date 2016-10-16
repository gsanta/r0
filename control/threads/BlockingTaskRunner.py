import asyncio
import concurrent.futures
import sys
import time


async def run_blocking(blockingTask, executor, eventLoop):
    print('run_blocking start')
    task = eventLoop.run_in_executor(executor, blockingTask)
    
    completed, pending = await asyncio.wait([task])
    results = [t.result() for t in completed]
    print(results)

class BlockingTaskRunner:

    def __init__(self, asyncio, eventLoop, executor):
        self.asyncio = asyncio
        self.eventLoop = eventLoop
        self.executor = executor

    def run(self, blockingTask):
         self.asyncio.ensure_future(run_blocking(blockingTask, self.executor, self.eventLoop))

def blocks():
    time.sleep(3)
    return 'task completed'

executor = concurrent.futures.ThreadPoolExecutor(
    max_workers=3,
)

event_loop = asyncio.get_event_loop()
try:
    taskRunner = BlockingTaskRunner(asyncio, event_loop, executor)
    taskRunner.run(blocks)
    event_loop.run_forever()
       
finally:
    event_loop.close()           
