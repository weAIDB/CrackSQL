from flask_apscheduler import APScheduler
import logging

scheduler = APScheduler()

def scheduler_init(app):
    try:
        # 检查调度器是否已经在运行
        if not scheduler.running:
            scheduler.init_app(app)
            scheduler.start()
            logging.info('调度器已启动 ---------------')
    except BaseException as error:
        # 修复日志格式问题
        logging.error(f"调度器启动错误: {str(error)} ---------------")
        pass
