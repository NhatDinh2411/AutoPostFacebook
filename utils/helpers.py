import schedule
import time

def job(func, at_time:str="8:30"):
    schedule.every().day.at(at_time).do(func)
    while True:
        schedule.run_pending()
        time.sleep(60)

