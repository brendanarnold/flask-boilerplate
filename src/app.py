from flask import Flask, jsonify
import log
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import exceptions
import config

sentry_sdk.init(
  dsn=config.SENTRY_DSN,
  integrations=[FlaskIntegration()],
  traces_sample_rate=1.0,
  environment=config.APP_ENV,
  release=config.APP_VERSION
)


app = Flask(__name__)

@app.route('/')
def root():
  json = jsonify({
    'version': config.APP_VERSION
  })
  return(json)

@app.route('/debug-sentry')
def debug_sentry():
  raise exceptions.DebugSentryException()

log.info('Server up')

