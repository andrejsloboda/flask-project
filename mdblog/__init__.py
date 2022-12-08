from celery import Celery

# instancia flask app dostane nazov podla
# mena modulu, v ktorom je vytvorena
celery = Celery("mdblog.factory")