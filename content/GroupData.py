# -*- coding: utf-8 -*-

# this group can use all methods
groupList0 = {"debug"}

# this group can get grades about the 2018 Entrance Examination for College.
groupList1 = {}

testGroup = "debug"

__groupDict = {0: groupList0, 1: groupList1}

def getGroupSet(cType):
	if cType == 0:
		set_ = set([])
		for item in __groupDict.items():
			set_ |= item[1]
	else:
		try:
			set_ = __groupDict[0] | __groupDict[cType]
		except KeyError:
			print("key error")
			set_ = __groupDict[0]
	return set_