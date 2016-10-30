import asyncio
import concurrent.futures
import sys
import time

@asyncio.coroutine
def schedule_blocking(blockingTask, executor, eventLoop):
    task = eventLoop.run_in_executor(executor, blockingTask)
    
    completed, pending = yield from asyncio.wait([task])
    results = [t.result() for t in completed]

class BlockingScheduler:

    def __init__(self, asyncio, eventLoop, executor):
        self.asyncio = asyncio
        self.eventLoop = eventLoop
        self.executor = executor

    def schedule(self, task):
         self.asyncio.ensure_future(schedule_blocking(task, self.executor, self.eventLoop))

# def blocks():
#     time.sleep(3)
#     return 'task completed'
# 
# executor = concurrent.futures.ThreadPoolExecutor(
#     max_workers=3,
# )
# 
# event_loop = asyncio.get_event_loop()
# try:
#     taskRunner = BlockingTaskRunner(asyncio, event_loop, executor)
#     taskRunner.run(blocks)
#     event_loop.run_forever()
#        
# finally:
#     event_loop.close()           
