import math
import time
import hmac
import random
import hashlib

VERSION = (0, 2)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'Generate TTL based self expiring crumbs (token).'
__author__ = 'Abhinav Singh'
__author_email__ = 'mailsforabhinav@gmail.com'
__homepage__ = 'https://github.com/abhinavsingh/crumb.py'
__license__ = 'BSD'

class Crumb(object):
    
    choices = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    
    def __init__(self, uid, ttl, key=None, action=None, secret=None):
        self.uid = str(uid)
        self.ttl = int(ttl)
        self.key = str(key) if key else key
        self.action = str(action) if action else 'crumb'
        self.secret = str(secret) if secret else self.gen_secret()
    
    def gen_secret(self):
        return ''.join([random.SystemRandom().choice(self.choices) for _ in range(50)])
    
    def challenge(self, i):
        return hmac.new(self.secret, '%s%s%s' % (i, self.action, self.uid), hashlib.sha256).hexdigest()[-12:]
    
    def validate(self):
        assert self.key is not None
        
        t = time.time()
        i = math.ceil(t / int(self.ttl))
        
        c = self.challenge(i)
        if c == self.key:
            return True
        
        c = self.challenge(i-1)
        if c == self.key:
            return True
        
        return False
    
    def generate(self):
        t = time.time()
        i = math.ceil(t / int(self.ttl))
        self.key = self.challenge(i)
