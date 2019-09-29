import rele
from settings import config

data = {'location': '/photos/123.jpg'}
rele.publish(topic='photo-uploaded', data=data)
