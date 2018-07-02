# -*- coding: utf-8 -*-

from command import command
from content import GradeData as d

groupTypeSet = {1}

def getRank(grade):
    if grade >= 709:
        return -1
    elif grade <= 351:
        return -2
    else:
        if grade >= 700:
            return d.numList[0]
        else:
            return sum(d.numList[0:700-grade+1])

def getRank2(grade):
    if grade >= 688:
        return -1
    elif grade <= 361:
        return -2
    else:
        if grade >= 680:
            return d.WnumList[0]
        else:
            return sum(d.WnumList[0:680-grade+1])

def getNum(grade):
    if grade >= 700 and grade <= 708:
        return -1
    i = 700 - grade
    if i < 0 or i >= len(d.numList):
        return 0
    return d.numList[i]

def getNum2(grade):
    if grade >= 680 and grade <= 687:
        return -1
    i = 680 - grade
    if i < 0 or i >= len(d.WnumList):
        return 0
    return d.WnumList[i]

def getGrade(rank):
    if rank <= 0 or rank >= sum(d.numList):
        return -1
    if rank <= 7:
        return 708
    sum1 = 0
    k = 0
    for i in d.numList:
        sum1 += i
        k += 1
        if rank <= sum1:
            break
    return 700 - k + 1

def getGrade2(rank):
    if rank <= 0 or rank >= sum(d.numList):
        return -1
    if rank <= 4:
        return 687
    sum1 = 0
    k = 0
    for i in d.WnumList:
        sum1 += i
        k += 1
        if rank <= sum1:
            break
    return 680 - k + 1

class Command_Rank(command.command):

	def Rank(self, contacts, content):
	    score = int(content)
	    rank1 = getRank(score)
	    rank2 = getRank2(score)
	    str1 = str(score) + "分在福建省的排名为："

	    if rank1 == -1:
	        str1 = str1 + "超越状元的存在" 
	    elif rank1 == -2:
	        str1 = str1 + "暂无数据"
	    elif rank1 == d.numList[0]:
	        str1 = str1 + "前" + str(d.numList[0]) + "名"
	    else:
	        str1 = str1 + str(rank1)
	    str1 = str1 + "（理科），"

	    if rank2 == -1:
	        str1 = str1 + "超越状元的存在" 
	    elif rank2 == -2:
	        str1 = str1 + "暂无数据"
	    elif rank2 == d.WnumList[0]:
	        str1 = str1 + "前" + str(d.WnumList[0]) + "名"
	    else:
	        str1 = str1 + str(rank2)
	    str1 = str1 + "（文科）"
	    return str1

	def __init__(self):
		command.command.__init__(self, "查询排名", ["成绩"], "查询成绩在福建高考的排名", self.Rank, groupTypeSet)

class Command_Grade(command.command):

    def Grade(self, contacts, content):
        rank = int(content)
        score1 = getGrade(rank)
        score2 = getGrade2(rank)
        str1 = "福建省第" + str(rank) + "名的成绩为："
        
        if rank == 1:
            str1 += "708分（理科），687分（文科）"
            SendTo(bot, contact, str1)
            return
        if score1 == -1:
            str1 += "暂无数据"
        elif score1 == 708:
            str1 += "700-708分"
        else:
            str1 = str1 + str(score1) + "分"
        str1 = str1 + "（理科），"

        if score2 == -1:
            str1 += "暂无数据"
        elif score2 == 687:
            str1 += "680-687分"
        else:
            str1 = str1 + str(score2) + "分"
        str1 = str1 + "（文科）"
        return str1

    def __init__(self):
        command.command.__init__(self, "查询成绩", ["排名"], "查询指定排名的成绩", self.Grade, groupTypeSet)

class Command_Num(command.command):

    def Number(self, contacts, str1):

        score = int(str1)

        str1 = "福建省考" + str(score) + "分的人数为 "
        str1 = str1 + "理科："
        n = getNum(score)
        if n == 0:
            str1 = str1 + "暂无数据"
        elif n == -1:
            str1 = str1 + "[700, 708]分数段内有" + str(d.numList[0]) + "人"
        else:
            str1 = str1 + str(n) + "人"
        
        str1 = str1 + "，文科："
        n = getNum2(score)
        if n == 0:
            str1 = str1 + "暂无数据"
        elif n == -1:
            str1 = str1 + "[680, 687]分数段内有" + str(d.WnumList[0]) + "人"
        else:
            str1 = str1 + str(n) + "人"

        return str1

    def __init__(self):
        command.command.__init__(self, "查询人数", ["成绩"], "查询与该成绩重分的人数", self.Number, groupTypeSet)
