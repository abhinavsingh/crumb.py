import time
import unittest
from crumb import Crumb

class TestCrumb(unittest.TestCase):
    
    def test1(self):
        c = Crumb('tim@tom.com', 1, secret='!@#$')
        k = c.generate()
        time.sleep(1) # even though it may expire by here, will still pass validation due to previous interval validation check enabled
        c = Crumb('tim@tom.com', 1, secret='!@#$', key=k)
        assert c.validate() == True
        time.sleep(1) # will not pass validation after this sleep coz grace period (same as actual ttl) is over by now
        c = Crumb('tim@tom.com', 1, secret='!@#$', key=k)
        assert c.validate() == False

if __name__ == '__main__':
    unittest.main()
