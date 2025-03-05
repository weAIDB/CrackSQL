from flask import Blueprint
from api.utils.response import ResMsg
from api.utils.util import route
from api.utils.scheduler import scheduler
from config.logging_config import logger

bp = Blueprint("scheduler", __name__, url_prefix='/api/scheduler')


@route(bp, '/jobs', methods=["GET"])
def jobs():
    """
    Get all jobs
    :return:
    """
    scheduler_jobs = scheduler.get_jobs()
    res = ResMsg()
    res.update(data=str(scheduler_jobs))
    return res.data

