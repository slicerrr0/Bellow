'''Contains an instance of `celery.Celery` used to process
payment requests and verification.
'''

from celery import Celery

app = Celery(
    'payment',
    broker='amqp://localhost',   # used with RabbitMQ
    include=['payment.tasks']
)

# Celery instance will 'start' when imported
if __name__ == '__main__':
    app.start()