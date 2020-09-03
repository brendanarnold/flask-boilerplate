from flask import Flask, jsonify
import log

APP_VERSION = '0.0.1'

app = Flask(__name__)

@app.route('/')
def root():
  json = jsonify({
    'version': APP_VERSION
  })
  return(json)

log.info('Server up')

