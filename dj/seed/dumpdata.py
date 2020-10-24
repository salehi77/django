#!/usr/bin/env python

import os



os.system('python ../manage.py dumpdata users --indent 4 > users.json')
os.system('python ../manage.py dumpdata shop --indent 4 > shop.json')
os.system('python ../manage.py dumpdata auth.group --indent 4 > groups.json')
