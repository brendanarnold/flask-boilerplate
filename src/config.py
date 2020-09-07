import os
from dotenv import load_dotenv

load_dotenv()

APP_VERSION = '0.0.1'
APP_ENV = os.getenv('APP_ENV')

SENTRY_DSN = os.getenv('SENTRY_DSN')
