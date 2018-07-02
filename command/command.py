# -*- coding: utf-8 -*-

# all commands should inherit this class
# refer to commandUtils.CommandList

class command:

	cContent = ""
	cHelp = ""
	cDocument = ""
	cAction = lambda contacts, args: ""
	cGroupType = {}
	cArgs = []

	# @content: the title of this command
	# @args: a list of string, used to record names of parameters about the command.
	# @hint: a simple instructions about the command
	# @action: a function object, whose parameters contains user info (see info.contacts),
	# and the parameters of the command. The number should be equal to the number of args.
	# @groupType: record what kind of group can use this command. See content.GroupData
	def __init__(self, content, args, hint, action, groupType):
		self.cContent = content
		self.cDocument = "！" + content + " " + " ".join(["[" + x + "]" for x in args])
		self.cHelp = self.cDocument + ": " + hint
		self.cAction = action
		self.cGroupType = groupType
		self.cArgs = args
