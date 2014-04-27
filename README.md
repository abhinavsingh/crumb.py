crumb.py
========

Generate TTL based self expiring crumbs (token).

Usage
-----

```
pip install --upgrade crumb.py
```

```
>>> from crumb import Crumb
>>>
>>> # generate crumb for user that expires in 30 seconds
>>> c = Crumb('tim@tom.com', 30, secret='!@#$')
>>> c.generate()
830b60fe77b2
>>>
>>> # key attribute also contains the generated crumb
>>> print c.key
830b60fe77b2
>>> 
>>> # verify the generated crumb
>>> c = Crumb('tim@tom.com', 30, secret='!@#$', key='830b60fe77b2')
>>> c.validate()
True
>>>
>>> # try to verify again after 60 sec
>>> c.validate()
False
```
