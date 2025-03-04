import logging
from flask import Blueprint
from api.utils.response import ResMsg
from api.utils.util import route
from api.utils.scheduler import scheduler


bp = Blueprint("scheduler", __name__, url_prefix='/api/scheduler')

logger = logging.getLogger(__name__)


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

