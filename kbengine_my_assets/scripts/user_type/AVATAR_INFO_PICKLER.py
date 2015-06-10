# -*- coding: utf-8 -*-

class AVATAR_INFO_TYPE(list):
	def __init__(self):
		list.__init__(self)

	def asDict(self):
		data = {
            "dbid"			: self[0],
            "roleType"		: self[1],
            "name"		    : self[2],
            "level"		: self[3],
		}

		return data

	def createFromDict(self, dictData):
		self.extend([dictData["dbid"], dictData["roleType"], dictData["name"], dictData["level"]])
		return self

class AVATAR_INFO_PICKLER:
	def __init__(self):
		pass

	# // 此接口被C++底层调用
	# // 引擎将数据交给脚本层管理，脚本层可以将这个字典重定义为任意类型
	# // dct中的数据为 {"k1" : 0, "k2" : 0}, 它就是一个字典，包含了2个固定的key
	# // 且值一定是符合alias.xml中定义的类型
	# // XXX_TYPE().createFromDict接口调用后，返回的是一个list([0, 0])
	# // createObjFromDict被调用后，返回的数据将直接赋值到脚本中的变量
	def createObjFromDict(self, dct):
		return AVATAR_INFO_TYPE().createFromDict(dct)

	# // 此接口被C++底层调用
	# // 底层需要从脚本层中获取数据，脚本层此时应该将数据结构还原为固定字典
	# // list([0, 0]) => {"k1" : 0, "k2" : 0}
	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, AVATAR_INFO_TYPE)

avatar_info_inst = AVATAR_INFO_PICKLER()

