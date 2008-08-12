#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

try:
  import pygtk
  #tell pyGTK, if possible, that we want GTKv2
  pygtk.require("2.0")
except:
  #Some distributions come with GTK2, but not pyGTK
  pass

try:
  import gtk
  import gtk.glade
except:
  print "You need to install pyGTK or GTKv2 ",
  print "or set your PYTHONPATH correctly."
  print "try: export PYTHONPATH=",
  print "/usr/local/lib/python2.2/site-packages/"
  sys.exit(1)

from signal_handle import *
from random_things import *
from get_obj_from_xml import *
__author__ = "Liu Qing"
__copyright__ = "Copyright (c)2008 Liu Qing"
__license__ = "GNU GPL version 2"
__version__ = "1"

#
#Start from here
#
xml = gtk.glade.XML('pycash.glade')

all_widget = get_objects(xml)

set_signal_handle(all_widget)

#init system
gobject.timeout_add(0, sys_init)

gtk.main()
sys.exit(0)

