# -*- coding: utf-8 -*-
import itertools
import command as c
import random
import time

GroupType = {0}

import os

fileName = ""
KEY_PROBLEM = "problem"
KEY_TIME = "time"
KEY_PLAYER = "player"
KEY_NUM = "num"

suffix = '游戏中支持的指令：\n“!答案”：查看该题答案并进入下一题\n“!结束”：结束游戏\n“!排行榜”：查看当前积分排行'


def getPath(contacts):
    return "24_{:}.dat".format(contacts.groupContact.name)

def getDict(contacts):
    dict0 = {}
    if os.path.isfile(getPath(contacts)):
        with open(getPath(contacts), "r") as file1:
            dict0 = eval(file1.read()) 
        return dict0
    else:
        return dict0

def saveDict(contacts, dict1):
    with open(getPath(contacts),"w") as f:
        f.write(str(dict1))

def isPlaying(contacts):
	return getDict(contacts).get(KEY_PROBLEM, None) != None

def setProblem(contacts, clist):
	dict1 = getDict(contacts)
	dict1[KEY_PROBLEM] = " ".join(clist)
	dict1[KEY_TIME] = str(time.time())
	dict1[KEY_NUM] = dict1.get(KEY_NUM, 0) + 1
	saveDict(contacts, dict1)

def gameOver(contacts):
	if os.path.exists(getPath(contacts)):
		os.remove(getPath(contacts))

def cal(n1, n2, n3, n4):

	exps = ('(({:} {:} {:}) {:} {:}) {:} {:}',
	'({:} {:} {:}) {:} ({:} {:} {:})',
	'({:} {:} ({:} {:} {:})) {:} {:}',
	'{:} {:} (({:} {:} {:}) {:} {:})',
	'{:} {:} ({:} {:} ({:} {:} {:}))')

	def check(exp):
		try:
			return eval(exp) == 24.0
		except:
			return False

	numlist = [float(n1), float(n2), float(n3), float(n4)]
	permutation = list(itertools.permutations(numlist, 4))
	op = list(itertools.product("+-*/", repeat=3))
	count = 0
	str1=""
	for nums in permutation:
		for o in op:
			ex = [nums[i//2] if i % 2 == 0 else o[i//2] for i in range(0, 7)]
			for e in exps:
				str1 = e.format(*ex)
				if check(str1):
					ex = [ex[i] if i % 2 == 1 else int(ex[i]) for i in range(0,7)]
					str1 = e.format(*ex)
					return str1
	return None

def getProblemStr(n, clist):
	return "第{:d}题：{:}".format(n, " ".join(clist))

maxTuple = (10,12,15,20,30,50,70,100,150,200)

def newGame(contacts, n):
	while (True):
		a, b, c, d = random.randint(1,maxTuple[n-1]), random.randint(1,maxTuple[n-1]), random.randint(1,maxTuple[n-1]), random.randint(1,maxTuple[n-1])
		sa, sb, sc, sd = str(a), str(b), str(c), str(d)
		if cal(a, b, c, d) != None:
			setProblem(contacts, (sa, sb, sc, sd))
			return sa, sb, sc, sd

def nextGame(contacts):
	dict0 = getDict(contacts)
	if dict0.get(KEY_NUM) == 10:
		rank = getRank(contacts, dict0.get(KEY_PLAYER))
		if rank[0] != None:
			str1 = "游戏结束！排行榜：" + rank[0]
			str1 += "恭喜" + rank[1] + '获得冠军！'
		else:
			str1 = "游戏结束！"
		gameOver(contacts)
	else:
		numList = newGame(contacts, int(getDict(contacts)[KEY_NUM]))
		str1 = getProblemStr(int(getDict(contacts)[KEY_NUM]), numList)
	return str1

class Command_24(c.command):

	def problem(self, contacts):

		problemList = getDict(contacts).get(KEY_PROBLEM, "-1").split()
		if problemList != ["-1"]:
			return '游戏正在进行中！题目：' + " ".join(problemList) + '\n' + suffix

		sa, sb, sc, sd = newGame(contacts, 1)
		return ('24点游戏规则：bot在群里公布十道题目。玩家用上题目给的所有数字，\
使用加减乘除或括号组成表达式计算出24，并直接群里发送表达式。每个人都可以参与抢答，最先回答正确结果\
者得一分。题目保证存在一个解。\n' + suffix + "\n" + getProblemStr(1, (sa, sb, sc, sd)))	

	def __init__(self):
		c.command.__init__(self, "24点", [], "玩一盘紧张刺激的24点游戏", self.problem, GroupType)

def getRank(contacts, playerDict):
	i = 0
	str1 = "\n"
	champion = ""
	for item in sorted(getDict(contacts).get(KEY_PLAYER, {}).items(), key=lambda x: x[1], reverse=True):
		i += 1
		str1 += "No." + str(i) + " " + str(item[0]) + ": " + str(item[1]) + "分\n"
		if i == 1:
			champion = item[0]
	if i == 0:
		return (None, )
	return (str1, champion)

def answer(contacts):
	dict0 = getDict(contacts)
	problemList = dict0.get(KEY_PROBLEM, None).split()
	if problemList == None:
		return (None)
	else:
		ans = cal(int(problemList[0]), int(problemList[1]), int(problemList[2]), int(problemList[3]))
		str1 = "答案： " + ans + "\n" + nextGame(contacts)
		return str1

def process(contacts, cstr):
	dict0 = getDict(contacts)
	if cstr.startswith("!答案") or cstr.startswith("！答案"):
		return answer(contacts)
	if cstr.startswith("!结束") or cstr.startswith("！结束"):
		dict0[KEY_NUM] = 10
		saveDict(contacts, dict0)
		return nextGame(contacts)
	if cstr.startswith("!排行榜") or cstr.startswith("！排行榜"):
		rank = getRank(contacts, dict0.get(KEY_PLAYER, {}))
		if rank[0] == None:
			return "当前没有人获得积分！"
		else:
			return "24点排行榜：" + rank[0]
	else:
		# check answer
		express = cstr
		express = express.replace("（", "(")
		express = express.replace("）", ")")
		express = express.replace("×", "*")
		express = express.replace("÷", "/")
		express = express.replace(" ", "")

		l = express.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ")\
		.replace("(", " ").replace(")", " ")
		expList = l.split()
		expList = sorted(expList, key=lambda x: int(x))
		proList = dict0[KEY_PROBLEM].split()
		proList = sorted(proList, key=lambda x: int(x))

		if not expList == proList:
			return None

		try:
			name = contacts.memberContact.name
			if eval(express) == 24.0:
				if name == "keybot":
					return "虽然回答正确了，但是匿名用户是没有分的哦！\n" + nextGame(contacts)
				playerDict = dict0.get(KEY_PLAYER, {})
				playerDict[name] = str(int(playerDict.get(name, 0)) + 1)
				dict0[KEY_PLAYER] = playerDict
				saveDict(contacts, dict0)

				return "恭喜 @" + name + " 回答正确，得一分！\n" + nextGame(contacts)
		except:
			return None
