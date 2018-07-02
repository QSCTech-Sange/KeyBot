# -*- coding: utf-8 -*-
from command import command

suffix = "（提示：感叹号后无空格，每个参数前面空一格）"

class Command_Help(command.command):
	def __init__(self):
		command.command.__init__(self, "帮助", [], "查看所有支持的指令", None, {0})