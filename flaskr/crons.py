import schedule
import time
from threading import Thread
from flaskr.services.teste_debug_cron_sv import TesteDebugCronSv

class Crons(Thread):
    def __init__(self, **kwargs):
        super(Crons, self).__init__(**kwargs)
        
        schedule.every(30).seconds.do(
            job_func = TesteDebugCronSv().escrever_debug )


    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(2)