#!/usr/bin/env python

import os



os.system('python ../manage.py loaddata users.json')
os.system('python ../manage.py loaddata shop-arvan.json')
os.system('python ../manage.py loaddata groups.json')
