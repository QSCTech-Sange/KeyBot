# -*- coding: utf-8 -*-
import keybot
import GroupData as groupData
import sys

class contact:
	ctype = ""
	name = ""
	
class bot:

	def SendTo(self, contact, content):
		print(contact.name, ":", content)

	def Stop(self):
		print("stop")
		sys.exit()

bot1 = bot()

contact1 = contact()
contact1.ctype = "group"
contact1.name = "debug"

member1 = contact()
member1.ctype = ""
member1.name = groupData.testGroup

while(True):
	keybot.onQQMessage(bot1, contact1, member1, input())