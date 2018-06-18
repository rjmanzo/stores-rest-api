# [CONFIG]

# production key
APP_KEY = 'xxxxxxxxxxxxxxxx'

# JWT URL endpoint. By default is /auth
AUTH_URL_PATH = '/login'
# JWT delta expiration time token in seconds
EXPIRATION_TIME = 1800

# JWT_AUTH = {
#     'JWT_AUTH_URL_RULE': AUTH_URL_PATH,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=EXPIRATION_TIME)
# }
