from threading import Thread
from .scheduler import Scheduler
from .task import Task


class SchedulerWrapper:
    
    __scheduler: Scheduler = None
    __is_active: bool = False

    def __init__(self,  is_active: bool = False):
        self.__is_active = is_active

    def start_scheduler(self, tasks: list[Task]):
        self.__start(tasks)

    def restart_scheduler(self, tasks: list[Task]):
        if self.__scheduler is not None:
            self.__scheduler.stop()
        self.__start(tasks)

    def __start(self, tasks: list[Task]):
        if tasks is not None and self.__is_active:
            self.__scheduler = Scheduler(*tasks)
            Thread(target=self.__scheduler.run, daemon=True).start()
