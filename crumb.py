import math
import time
import hmac
import random
import hashlib

VERSION = (0, 4)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'Generate TTL based self expiring crumbs (token).'
__author__ = 'Abhinav Singh'
__author_email__ = 'mailsforabhinav@gmail.com'
__homepage__ = 'https://github.com/abhinavsingh/crumb.py'
__license__ = 'BSD'

class Crumb(object):
    
    choices = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    
    def __init__(self, uid, ttl, key=None, action=None, secret=None):
        '''Initialize crumb object.
        
        `uid`:    (string) unique id to associate with the crumbs
        `ttl`:    (integer) generated crumbs will expire after ttl seconds
        `key`:    (string) this is the generated crumb from previous run (pass for validation)
        `action`: (string) generate several crumbs for same `uid`, `action` defines the context
        `secret`: (string) a secret to use for crumb generation. It is generally a good idea to
                  use a different secret for different `uid` used.
        '''
        self.uid = str(uid)
        self.ttl = int(ttl)
        self.key = str(key) if key else key
        self.action = str(action) if action else 'crumb'
        self.secret = str(secret) if secret else self.gen_secret()
    
    def gen_secret(self):
        '''Ramdomly generate a secret key.'''
        return ''.join([random.SystemRandom().choice(self.choices) for _ in range(50)])
    
    def challenge(self, i):
        '''Calculate challenge for passed bucket id `i`.'''
        return hmac.new(self.secret, '%s%s%s' % (i, self.action, self.uid), hashlib.sha256).hexdigest()[-12:]
    
    def get_nth_bucket_challenge(self, n):
        '''n=1 for upcoming bucket (in future), n=-1 for bucket in future, n=0 for current bucket.'''
        i = self.get_current_bucket_id()
        return self.challenge(i+n)
    
    def get_current_bucket_id(self):
        '''Get current time bucket id.'''
        return math.ceil(time.time() / int(self.ttl))
    
    def validate(self):
        '''Validate passed crumb key.'''
        assert self.key is not None
        if self.get_nth_bucket_challenge(0) == self.key \
        or self.get_nth_bucket_challenge(-1) == self.key:
            return True
        return False
    
    def generate(self):
        '''Generate a new crumb key.'''
        self.key = self.get_nth_bucket_challenge(0)
        return self.key
