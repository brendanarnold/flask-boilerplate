import datetime
import utils

class AppException(Exception):
  def __init__(self, message = None):
    super().__init__(message)

    # Use this to match a user displayed ID to logging
    self.correlation_id = utils.generate_readable_id()

class DebugSentryException(AppException):
  def __init__(self, message = None):
    super().__init__(message)
    message = 'An error for checking sentry is working, raised at {}'.format(datetime.date.today().ctime())
