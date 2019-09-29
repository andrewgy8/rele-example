from time import sleep
from rele import sub, Worker
from settings import config

@sub(topic='photo-uploaded')
def photo_uploaded(data, **kwargs):
    print(f"Someone has uploaded an image to our service, "
          f"and we stored it at { data['location'] }.")

if __name__ == '__main__':
    worker = Worker(
        [photo_uploaded],
        config.gc_project_id,
        config.credentials,
        config.ack_deadline,
    )
    worker.setup()
    worker.start()
    sleep(120)
