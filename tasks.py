from celery import Celery
from time import sleep
app = Celery()

@app.task
def reverse(text):
    sleep(20)
    return text[::-1]


