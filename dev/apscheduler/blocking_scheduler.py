from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def my_block():
    print("Hello! The time is: %s" % datetime.now())


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # 每 3 秒執行一次 my_block 函式中的任務
    scheduler.add_job(my_block, "interval", seconds=3)
    scheduler.start()
