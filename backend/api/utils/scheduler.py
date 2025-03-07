from flask_apscheduler import APScheduler
import logging

scheduler = APScheduler()

def scheduler_init(app):
    try:
        # check if scheduler is running
        if not scheduler.running:
            scheduler.init_app(app)
            scheduler.start()
            logging.info('scheduler start ---------------')
    except BaseException as error:
        # fix log format problem
        logging.error(f"scheduler start error: {str(error)} ---------------")
        pass
