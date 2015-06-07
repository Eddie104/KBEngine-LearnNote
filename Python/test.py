#coding=utf-8

from BaseApp import KBEngine #IDE语法提示时候用，放入服务端时候，注释掉这行


# #import KBEngine #放入服务端时候，启用这行

class ClientObject(object):
    pass


class Stuedent(KBEngine.Proxy):
	"""docstring for Stuedent"""
	def __init__(self,age,name):
		self.age = age
		self.name = name

	def showAge(self):
	# def showAge():
	# TypeError: shoAge() takes 0 positional arguments but 1 was given
		print ("Age: " ,  self.age)
		# print ("Age: " + self.age)
		# TypeError: Can't convert 'int' object to str implicitly
	def showName(self):
		print ("Name : " , self.name)

	__clience = ClientObject()

	# 表示属性
	@property
	def Instance(self):
		return  self.__clience


student = Stuedent(11,"zhangsan")
# student = new Stuedent(11,"zhangsan")	
# SyntaxError: invalid syntax	

print(student.Instance)

student.showName()

		
		
				


		
		
		
		