import rele
from google.oauth2 import service_account

RELE = {
    'GC_CREDENTIALS': service_account.Credentials.from_service_account_file(
        'credentials.json'
    ),
    'GC_PROJECT_ID': 'photo-uploading-app',
}
config = rele.config.setup(RELE)
