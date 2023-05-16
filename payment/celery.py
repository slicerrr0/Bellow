from celery import Celery

app = Celery(
    'payment',
)

# Celery instance will 'start' when imported
if __name__ == '__main__':
    app.start()