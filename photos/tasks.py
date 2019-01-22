from celery.schedules import crontab
import celery
from celery.utils.log import get_task_logger
from photos.utils import save_latest_flickr_image

logger = get_task_logger(__name__)

@celery.decorators.periodic_task(
    run_every=(crontab(minute='*/15')),
    name="task_save_latest_flickr_image",
    ignore_result=False
)
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    print('task')
    save_latest_flickr_image()
    logger.info("Saved image from Flickr")
