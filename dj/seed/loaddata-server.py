#!/usr/bin/env python

import os



os.system('python ../manage.py loaddata users.json')
os.system('python ../manage.py loaddata shop-server.json')
os.system('python ../manage.py loaddata groups.json')
