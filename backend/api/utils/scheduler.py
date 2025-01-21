from flask_apscheduler import APScheduler
import logging

scheduler = APScheduler()

def scheduler_init(app):
    try:
        scheduler.init_app(app)
        scheduler.start()
        logging.info('Scheduler Started,---------------')
    except BaseException as error:
        logging.error("Scheduler Started Error,---------------", error)
        pass
