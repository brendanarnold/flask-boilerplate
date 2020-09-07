
__all__ = ['generate_readable_id']

import shortuuid
shortuuid.set_alphabet('ABCDEFGHJKLMNPQRDSTUWXYZ0123456789')


def generate_readable_id ():
  '''This generates a random readable alphanumeric which has low chance of collision'''
  return shortuuid.uuid()[:8]
