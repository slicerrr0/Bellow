from celery import Celery

app = Celery(
    'payment',
)

if __name__ == '__main__':
    app.start()