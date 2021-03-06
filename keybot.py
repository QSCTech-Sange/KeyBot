# -*- coding: utf-8 -*-
import GroupData as groupData
import commandUtils, contacts
import learn, point24

def SendTo(bot, contact, str1):
    bot.SendTo(contact, str1.rstrip() + " ")

def onQQMessage(bot, contact, member, content):
    if content.endswith(" "):
        return
    if contact.ctype == 'group' and contact.name == groupData.testGroup and content == '!stop':
        SendTo(bot, contact, "stop")
        bot.Stop()
    elif 'Key' in contact.name and 'test' in content:
        SendTo(bot, contact, "test: " + content)
    elif contact.ctype == 'group':
        cons = contacts.contacts(contact, member)
        str1 = commandUtils.match(content, cons)
        if str1 != None:
            SendTo(bot, contact, str1)
        elif point24.isPlaying(cons):
            str1 = point24.process(cons, content)
            if str1 != None:
                SendTo(bot, contact, str1)
        else:
            res = learn.readStr(cons, content)
            if res != 0:
                SendTo(bot, contact, str(res))