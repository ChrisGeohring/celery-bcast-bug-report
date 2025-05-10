from celery import Celery
import os

from kombu.common import Broadcast
from kombu import Queue

app = Celery('bugreport')
app.config_from_object('celery.app.defaults', namespace='CELERY')

app.conf.task_default_queue_type = 'quorum'
app.conf.task_default_queue = 'direct'
app.conf.result_backend = 'rpc://'
app.conf.broker_transport_options = {"confirm_publish": True}
app.conf.task_ignore_result = True

app.conf.task_queues = {
    Queue('direct', queue_arguments={"x-queue-type": "quorum"}),
    Broadcast(
        'broadcast',
        durable=True,
        auto_delete=False,
        queue_arguments={"x-queue-type": "quorum"},
    ),
}