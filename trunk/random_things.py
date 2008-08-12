import random, string

#0,judge what kind of things should be raise
#1,bad things
#2,good things
#3,raise price
#4,bring down price

#现金收入都是百分比
good_things = {
   1:["过生日请朋友大吃大喝，你收到巨额红包。", 50, 0, 0, 0, -1, 2],
   2:["路上捡到一个钱包，你偷偷的揣进了怀里。。。", 10, 0, 0, 0, 0, -2],
   3:["帮院子里的大妈溜狗，大妈夸你是热心肠。", 0, 0, 0, 0, 0, 1],
   #4:["", 0, 0, 0, 0, 0, 0],
   #5:["", 0, 0, 0, 0, 0, 0],
   #6:["", 0, 0, 0, 0, 0, 0],
   #7:["", 0, 0, 0, 0, 0, 0],
   
   }

bad_things = {
   1:["抢小孩的糖被邻居发现。", 0, 0, 0, 0, 0, -2],
   2:["小胡同里被流氓打劫。", -10, 0, 0, 0, -3, 0],
   3:["老乡生病住院，你代付了大笔医药费。", -10, 0, 0, 0, 0, 3],
   4:["挤公交车被误认为流氓，挨了两耳光。", 0, 0, 0, 0, -1, -1],
   5:["公交车上一个大汉撞了你一下。。。", -20, 0, 0, 0, 0, 0],
   #6:["", 0, 0, 0, 0, 0, 0],
   #7:["", 0, 0, 0, 0, 0, 0],
   
   }

def get_random_int(mini, maxi):
   random.seed(random.random())
   return random.randint(mini, maxi)

def add_entry_valure(entry, value):
   entry.set_text(str(string.atoi(entry.get_text()) + value))

def do_action(wd, action):
   cash = int((action[1] * string.atoi(wd["et_cash"].get_text())) / 100)
   debt = action[2]
   fund = action[3]
   lend = action[4]
   health = action[5]
   repute = action[6]
   add_entry_valure(wd["et_cash"], cash)
   add_entry_valure(wd["et_debt"], debt)
   add_entry_valure(wd["et_fund"], fund)
   add_entry_valure(wd["et_lend"], lend)
   add_entry_valure(wd["et_health"], health)
   add_entry_valure(wd["et_repute"], repute)
   msg_str = ''
   if cash > 0:
      msg_str += '[现金增加了]'
   elif cash < 0:
      msg_str += '[现金减少了]'
   if debt > 0:
      msg_str += '[欠债增加了]'
   elif debt < 0:
      msg_str += '[欠债减少了]'
   if fund > 0:
      msg_str += '[存款增加了]'
   elif fund < 0:
      msg_str += '[存款减少了]'
   if lend > 0:
      msg_str += '[贷款增加了]'
   elif lend < 0:
      msg_str += '[贷款减少了]'
   if health > 0:
      msg_str += '[健康增加了]'
   elif health < 0:
      msg_str += '[健康减少了]'
   if repute > 0:
      msg_str += '[名声提高了]'
   elif repute < 0:
      msg_str += '[名声降低了]'
   return action[0] + msg_str

def random_action(show_msg, wd, all_goods):
   action_list = bad_things
   cash = string.atoi(wd["et_cash"].get_text())
   debt = string.atoi(wd["et_debt"].get_text())
   fund = string.atoi(wd["et_fund"].get_text())
   lend = string.atoi(wd["et_lend"].get_text())
   health = string.atoi(wd["et_health"].get_text())
   repute = string.atoi(wd["et_repute"].get_text())
   
   if random.randint(-5, 10) < 0:		#事件发生频率
      return
   #事件类型，好或者坏
   if get_random_int(0, repute) > 50:		#好事，默认是坏事
      action_list = good_things
   which_one = get_random_int(1, len(action_list))
   action = action_list[which_one]		#这个事件产生
   show_msg(do_action(wd, action))
   


