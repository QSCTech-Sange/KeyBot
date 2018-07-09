# -*- coding: utf-8 -*-
import command
import os
import fileName

def getPath(contacts):
    return fileName.learn_Name + "data_" + contacts.groupContact.name + ".dat"

def getDict(contacts):
    dict0 = {}
    if os.path.isfile(getPath(contacts)):
        with open(getPath(contacts), "r") as file1:
            dict0 = eval(file1.read())
        return dict0
    else:
        return dict0

def saveDir(contacts, dict1):
    with open(getPath(contacts),"w") as f:
        f.write(str(dict1))
        
def saveStr(contacts, str1, str2):
    dict1 = getDict(contacts)
    dict1[str1] = str2
    saveDir(contacts, dict1)

def readStr(contacts, str1):
	dict1 = getDict(contacts)
	if str1 in dict1:
		return dict1[str1]
	return 0

groupTypeSet = {0}

class Command_Learn(command.command):

    def Learn(self, contacts, str1, str2):
        saveStr(contacts, str1, str2)
        return '学习成功！对我说“' + str1 + '”试试吧！'

    def __init__(self):
        command.command.__init__(self, "学习", ["消息A", "消息B"], "让机器人在收到消息A时回复消息B", self.Learn, groupTypeSet)

class Command_Forget(command.command):

    def Forget(self, contacts, str1):
        dict1 = getDict(contacts)
        if str1 in dict1:
            dict1.pop(str1)
            saveDir(contacts, dict1)
            return '成功忘记“' + str1 + '”！'
        else:
            return '诶？我好像没记住过“' + str1 + "”"

    def __init__(self):
        command.command.__init__(self, "遗忘", ["消息A"], "让机器人忘记消息A", self.Forget, groupTypeSet)