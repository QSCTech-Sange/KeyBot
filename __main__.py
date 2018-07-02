# -*- coding: utf-8 -*-
import keybot
from content import GroupData as groupData

class contact:
	ctype = ""
	name = ""
	
class bot:

	def SendTo(self, contact, content):
		print(contact.name, ":", content)

	def Stop(self):
		print("stop")

bot1 = bot()

contact1 = contact()
contact1.ctype = "group"
contact1.name = "debug"

member1 = contact()
member1.ctype = ""
member1.name = groupData.testGroup

while(True):
	keybot.onQQMessage(bot1, contact1, member1, input())