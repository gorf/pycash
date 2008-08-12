#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""模块名
@version: $Id$
@author: U{Liu Qing}
"""

import pygtk
#pygtk.require('2.0')
import gtk, gobject, gtk.glade
import os, sys, time, string, copy, random, filedialogs
from accounts import *
from random_things import *
from sqlite3 import dbapi2 as sqlite
from datetime import datetime
#import gtkdialogs
import gettext
_ = gettext.gettext

storage_space = 100
win_main_title = '你不理财，财不理你'

#days_past = 40
wd = {}
pre_address = 1			#防止连续点同一个地方
DB_FILE=""
def create_book(data):
    global DB_FILE   
	#bookdlg=gtk.FileChooserDialog("输入帐本名字",wd["win_main"],gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_OK, gtk.RESPONSE_OK, gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
	#fileresponse=bookdlg.run()
	#print bookdlg.
	#if fileresponse == gtk.RESPONSE_OK:
	#	print "OK"
	#else:
	#	print "Cancel"
	#print fileresponse
    DB_FILE= filedialogs.save(title='输入帐本名字', current_name='untitled.cash')


	#DB_FILE = "mydb"
	
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    con = sqlite.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("""create table accounts(accname varchar(20),acctype
    varchar(20), accdescription varchar(20), accbalance real)""")
    cur.execute("insert into accounts(accname,acctype,accdescription, accbalance) values ('cash','asset','刘清的现金',0)")
    con.commit()
    cur.close()
    con.close()
    open_book()
def open_book(data=None):
    global DB_FILE
    print data
    if data!=None:
        DB_FILE= filedialogs.open(title=_('Open'), patterns=['*.cash'])
    print DB_FILE
    con = sqlite.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("""select * from accounts""")
    wd["tview_all_account"].get_model().clear()
    refresh_tv_all_account(cur)
    con.commit()
    cur.close()
    con.close()
    

def add_account(data):
    global DB_FILE
    print DB_FILE
    con = sqlite.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("""insert into accounts(accname,acctype,accdescription,accbalance) values ('cash of heyu','asset','何玉的现金',0)""")
    con.commit()
    wd["tview_all_account"].get_model().clear()
    print "here"
    cur.execute("""select * from accounts""")
    refresh_tv_all_account(cur)
    cur.execute("""
        	create table if not exists cash_of_heyu
	        (
        	  date		date,
		  cement	varchar(20),
		  debt		float,
		  credit	float,
	          balance       float
        	)
	        """)

    #cur.execute("insert into register (date,cement,debt,credit,balance) values ('20080101','测试',3.50,0,3.5)")

    con.commit()
    cur.close()
    con.close()

#更新利息
def refresh_accrual():
   debt = int(string.atoi(wd["et_debt"].get_text()) * 106 / 100)
   fund = int(string.atoi(wd["et_fund"].get_text()) * 101 / 100) 
   lend = int(string.atoi(wd["et_lend"].get_text()) * 102 / 100)
   wd["et_debt"].set_text(str(debt))
   wd["et_fund"].set_text(str(fund))
   wd["et_lend"].set_text(str(lend))

def tview_2clicked(tv, evnet):
   if evnet.type != gtk.gdk._2BUTTON_PRESS:
      return
   aa,bb = tv.get_selection().get_selected()
   if bb is None:
      return
   if tv == wd["tview_all_account"]:
      b_buy_sell_clicked(wd["b_buy"])
   elif tv == wd["tview_register"]:
      b_buy_sell_clicked(wd["b_sell"])
   else:
      return

def set_win_main_title():
   #global days_past
   #wd["win_main"].set_title(win_main_title + '    还剩 ' + str(days_past) + ' 天')
   wd["win_main"].set_title(win_main_title)
   #days_past -= 1

def m_start_clicked(menu):
   show_msg('未完成')

def m_rich_clicked(menu):
   show_msg('未完成')

def m_exit_clicked(menu):
   gtk.main_quit()

def show_msg(msg):
   wd["l_msg"].set_text(str(msg))
   wd["win_msg"].show_all()

def get_num_of_accounts():
   tm = wd["tview_register"].get_model()
   iter_t = tm.get_iter_first()
   num = 0
   while iter_t is not None:
      num += string.atoi(tm.get_value(iter_t, 2))
      iter_t = tm.iter_next(iter_t)
   return num

def get_price(tv, name):
   tm = tv.get_model()
   iter_t = tm.get_iter_first()
   while iter_t is not None:
      if tm.get_value(iter_t, 0) == name:
         return string.atoi(tm.get_value(iter_t, 1))
      iter_t = tm.iter_next(iter_t)
   return -1

def sell_accounts(tv, name, num):
   tm = tv.get_model()
   iter_t = tm.get_iter_first()
   while iter_t is not None:
      if tm.get_value(iter_t, 0) == name:
         num_storage = string.atoi(tm.get_value(iter_t, 2))
         num_now = num_storage - num
         if num_now < 0:
            return -1
         elif num_now == 0:
            tm.remove(iter_t)
         else:
            tm.set_value(iter_t, 2, str(num_now))
         return 0
      iter_t = tm.iter_next(iter_t)
   return -1

def tree_view_add_row(tv, name, type, description, balance):
   ls = tv.get_model()
   iter_t = ls.append()
   ls.set(iter_t, 0, name, 1, type, 2, description, 3, balance)

def get_a_accounts(tv, name, price, num):
   #judge whether we already have this accounts
   already_exist = 0
   tm = tv.get_model()
   iter_t = tm.get_iter_first()
   while iter_t is not None:
      if tm.get_value(iter_t, 0) == name:
         already_exist = 1
         break
      iter_t = tm.iter_next(iter_t)
   if already_exist == 1:
      price_pre = string.atoi(tm.get_value(iter_t, 1))
      num_pre = string.atoi(tm.get_value(iter_t, 2))
      num_now = num_pre + num
      price_now = (price_pre * num_pre + price * num) / num_now
      tm.set(iter_t, 0, name, 1, str(price_now), 2, str(num_now))
   else:
      tree_view_add_row(tv, name, str(price), num)

def get_random_price(p_l, p_n, p_h):
   return (p_n + random.randint(p_l, p_h)) / 2

def refresh_tv_all_account(accounts):
   #pre_added = 1
    tv_m = wd["tview_all_account"]
    #l_accounts = list(accounts)
    #print list(accounts)
    for (name,type,description,balance) in accounts:
        print 'refresh all account list'
        print '%s帐户是%s类型的，是%s' % (name,type,description)
        tree_view_add_row(tv_m, name,type,description, balance)

def init_tree_view():
   tv_m = wd["tview_all_account"]
   tv_s = wd["tview_register"]
   ls_m = gtk.ListStore(str, str, str, str)
   ls_s = gtk.ListStore(str, str, str)
   tv_m.set_model(ls_m)
   tv_s.set_model(ls_s)
   
   tvc_1 = gtk.TreeViewColumn('帐户名          ')
   tv_m.append_column(tvc_1)
   tvc_type = gtk.TreeViewColumn('帐户类型')
   tv_m.append_column(tvc_type)
   tvc_2 = gtk.TreeViewColumn('描述')
   tv_m.append_column(tvc_2)
   tvc_3 = gtk.TreeViewColumn('余额')
   tv_m.append_column(tvc_3)
   tvc_4 = gtk.TreeViewColumn('日期')
   tv_s.append_column(tvc_4)
   tvc_5 = gtk.TreeViewColumn('序号')
   tv_s.append_column(tvc_5)
   tvc_6 = gtk.TreeViewColumn('描述')
   tv_s.append_column(tvc_6)
   tvc_7 = gtk.TreeViewColumn('对方帐户')
   tv_s.append_column(tvc_7)
   tvc_8 = gtk.TreeViewColumn('是否对帐')
   tv_s.append_column(tvc_8)
   tvc_9 = gtk.TreeViewColumn('借方')
   tv_s.append_column(tvc_9)
   tvc_10 = gtk.TreeViewColumn('贷方')
   tv_s.append_column(tvc_10)
   tvc_11 = gtk.TreeViewColumn('余额')
   tv_s.append_column(tvc_11)
   
   # create a CellRenderers to render the data
   cell1 = gtk.CellRendererText()
   cell_type = gtk.CellRendererText()
   cell2 = gtk.CellRendererText()
   cell3 = gtk.CellRendererText()
   cell4 = gtk.CellRendererText()
   cell5 = gtk.CellRendererText()
   
   # add the cells to the columns - 2 in the first
   tvc_1.pack_start(cell1, True)
   tvc_type.pack_start(cell_type, True)
   tvc_2.pack_start(cell2, True)
   tvc_3.pack_start(cell3, True)
   tvc_4.pack_start(cell4, True)
   tvc_5.pack_start(cell5, False)
   tvc_1.set_attributes(cell1, text = 0)
   tvc_type.set_attributes(cell_type, text = 1)
   tvc_2.set_attributes(cell2, text = 2)
   tvc_3.set_attributes(cell3, text = 3)
   tvc_4.set_attributes(cell4, text = 1)
   tvc_5.set_attributes(cell5, text = 2)
   #refresh_tv_all_account(all_accounts)

def sys_init():
   print 'System initialise...'
   wd["win_trading"].set_screen(wd["win_main"].get_screen())
   #copy data to my_stat&all_accounts, clean my_accounts
   global all_accounts
   all_accounts = copy.copy(all_accounts_origin)
   init_tree_view()
   #set_win_main_title()
   return 0

def win_delete_event(win, data):
   win.hide()
   return True

def b_boss_come_clicked(button):
   wd["win_main"].hide()
   wd["win_boss_come"].show_all()

def win_boss_come_close(win, event):
   wd["win_main"].show_all()
   return win_delete_event(win, event)

def b_post_office_ok_clicked(button):
   cash = string.atoi(wd["et_cash"].get_text())
   debt = string.atoi(wd["et_debt"].get_text())
   pay = int(wd["spb_post_office"].get_value())
   #判断是否需要还钱
   if debt <= 0:
      show_msg('你没欠债不需要还钱。')
      return
   #判断还多少钱
   if debt < pay:
      show_msg('不需要还这么多。')
      return
   #判断钱够不够
   if cash < pay:
      show_msg('钱不够。')
      return
   #执行还钱动作
   debt -= pay
   cash -= pay
   wd["et_cash"].set_text(str(cash))
   wd["et_debt"].set_text(str(debt))
   wd["win_post_office"].hide()

#更换地方
def b_address_clicked(button):
   global pre_address
   if id(pre_address) == id(button):
      return
   #if days_past < 0:			#game over
      #cash = string.atoi(wd["et_cash"].get_text())
      #debt = string.atoi(wd["et_debt"].get_text())
      #fund = string.atoi(wd["et_fund"].get_text())
      #lend = string.atoi(wd["et_lend"].get_text())
      #msg = '   40天时间到了，你一共赚了' + str(cash - debt + fund - lend) + '大元， 恭喜恭喜~~该回家讨老婆啦 !^_^~~\n'
      #show_msg(msg)
      #return
   pre_address = button
   wd["tview_all_account"].get_model().clear()
   refresh_tv_all_account(all_accounts)			#刷新商品
   refresh_accrual()				#利息
   set_win_main_title()				#刷新天数
   random_action(show_msg, wd, all_accounts)	#随机事件

def spb_trading_keypress(widget, event):
   if event.keyval == gtk.keysyms.Escape:
       win.iconify()
   if event.keyval == gtk.keysyms.Return:
       on_button1_clicked(None)

#买进、卖出按钮
def b_buy_sell_clicked(button):
   button_text = button.get_label()
   label_string = ''
   num = 100
   if button_text.find('买') >= 0:
      aa,bb=wd["tview_all_account"].get_selection().get_selected()
      if bb is None:
         show_msg('请选择要购买的物品')
         return
      label_string = '买进数量：'
      num = storage_space - get_num_of_accounts()		#剩余空间
      can_buy = int(string.atoi(wd["et_cash"].get_text()) / string.atoi(aa.get_value(bb, 1)))
      if num > can_buy:
         num = can_buy
   elif button_text.find('卖') >= 0:
      aa,bb=wd["tview_register"].get_selection().get_selected()
      if bb is None:
         show_msg('请选择要出售的物品')
         return
      label_string = '卖出数量：'
      tm = wd["tview_register"].get_model()
      num = string.atoi(tm.get_value(bb, 2))
   wd["l_trading"].set_text(label_string)
   wd["spb_trading"].set_value(num)
   wd["win_trading"].show_all()

def b_trading_clicked(button):
   button_text = button.get_label()
   wd["win_trading"].hide()
   if button_text.find('取消') >= 0:
      return
   elif button_text.find('确定') >= 0:
      trading_type = 1						#1:sell  0:buy
      label_string = wd["l_trading"].get_text()
      tv_from = wd["tview_register"]
      tv_to = wd["tview_all_account"]
      if label_string.find('买') >= 0:				#judge buy or sell
         trading_type = 0
         tv_from = wd["tview_all_account"]
         tv_to = wd["tview_register"]
      
      aa_f,bb_f = tv_from.get_selection().get_selected()
      name_f = aa_f.get_value(bb_f, 0)				#get name
      price_f = string.atoi(aa_f.get_value(bb_f, 1))		#get price
      num = int(wd["spb_trading"].get_value())			#get spin_button nummber
      cash = string.atoi(wd["et_cash"].get_text())		#get cash
      
      if num <= 0 or cash <= 0:
         return
      if trading_type == 0:				#buy...
         cash = cash - (num * price_f)
         if cash < 0:						#judge whether have enough money
            show_msg('钱不够')
            return
	 if get_num_of_accounts() + num > storage_space:
	    show_msg('空间不够，最大空间' + str(storage_space))
            return
         wd["et_cash"].set_text(str(cash))			#pay the money
         get_a_accounts(tv_to, name_f, price_f, num)		#get accounts
      else:						#sell...
         aa_t,bb_t = tv_to.get_selection().get_selected()
         price_t = get_price(tv_to, name_f)
         if price_t < 0:					#market does not sell this accounts
            show_msg("不卖这种货")
            return
         cash = cash + price_t * num
         
         if sell_accounts(tv_from, name_f, num) < 0:		#remove accounts
            show_msg("没那么多货物")
            return
         wd["et_cash"].set_text(str(cash))			#get money

def set_signal_handle(data):
   global wd
   wd = data
   wd["win_main"].connect('destroy', m_exit_clicked)
   wd["win_about"].connect('delete_event', win_delete_event)
   wd["win_trading"].connect('delete_event', win_delete_event)
   wd["win_msg"].connect('delete_event', win_delete_event)
   wd["win_boss_come"].connect('delete_event', win_boss_come_close)
   wd["win_post_office"].connect('delete_event', win_delete_event)

   #wd["m_start"].connect('activate', m_start_clicked)
   #wd["m_rich"].connect('activate', m_rich_clicked)
   wd["m_create_book"].connect('activate', create_book)
   wd["m_open_book"].connect('activate', open_book)
   wd["m_exit"].connect('activate', m_exit_clicked)
   wd["m_about"].connect_object('activate', gtk.Window.show_all, wd["win_about"])
   wd["b_about"].connect_object('clicked', gtk.Window.hide, wd["win_about"])
   wd["b_add_account"].connect('clicked', add_account)
   wd["b_msg"].connect_object('clicked', gtk.Window.hide, wd["win_msg"])
   wd["tview_all_account"].connect('button_press_event', tview_2clicked)
   wd["tview_register"].connect('button_press_event', tview_2clicked)




   wd["b_post_office_ok"].connect('clicked', b_post_office_ok_clicked)
   wd["b_post_office_cancel"].connect_object('clicked', gtk.Window.hide, wd["win_post_office"])

