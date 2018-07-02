# -*- coding: utf-8 -*-
from command import grade, learn, hint
from content import GroupData as groupData

helper = hint.Command_Help()

CommandList = [\
	grade.Command_Rank(), \
	grade.Command_Grade(), \
	grade.Command_Num(), \
	learn.Command_Learn(), \
	learn.Command_Forget(), \

	# add new command here
	
	helper
]

def matchTitle(str1, com):
	return str1.startswith("!" + com) or str1.startswith("！" + com)

def matchGroup(name, gro):
	return name.startswith(gro)

def permission(contact, groupTypeSet):
	if contact.ctype != "group":
		return False
	for type_ in groupTypeSet:
		for gro in groupData.getGroupSet(type_):
			if contact.name.startswith(gro):
				return True
	return False

def match(content, contacts):
	strList = content.split()
	if matchTitle(content, helper.cContent):
		return "".join([c.cHelp + "\n" if permission(contacts.groupContact, c.cGroupType) else "" for c in CommandList]) + hint.suffix
	for com in CommandList:
		length = len(com.cArgs)
		if matchTitle(content, com.cContent) and permission(contacts.groupContact, com.cGroupType):
			if length != 0:
				try:
					args = [strList[i] for i in range(1, length)] + [" ".join(strList[length:])]
					if len(args) != length or not args[0]:
						raise IndexError("")
					return com.cAction(contacts, *args)
				except Exception:
					return '参数错误！正确的指令是："' + com.cDocument + '"' + hint.suffix
			else:
				return com.cAction(contacts)
	return None