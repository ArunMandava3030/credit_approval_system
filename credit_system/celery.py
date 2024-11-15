from celery import Celery

app = Celery('credit_system')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
