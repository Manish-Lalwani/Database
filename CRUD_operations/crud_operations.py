
import mysql.connector

class MysqlOperations:
	def __init__(self,details_dict):
		self.details_dict = details_dict

	def connection_init_func(self):
		self.conn_obj = mysql.connector.connect(host = details_dict['host'], database = details_dict['database'], user = details_dict['user'], password = details_dict['password'])
		if self.conn_obj.is_connected():
			print("connected successfully")
			return self.conn_obj

	def cursor_init_func(self,conn_obj):
		self.conn_obj = conn_obj
		self.cursor_obj = self.conn_obj.cursor()
		print("Cursor Initialized Successfully")
		return self.cursor_obj	

	def execute_query(self,cursor_obj,query):
		self.cursor_obj = cursor_obj
		self.query = query
		self.cursor_obj.execute(self.query)
		print("Query executed successfully") #we can change these print statement to logs check for logging in python
		return self.cursor_obj


	def display_result(self,cursor_obj):
		self.cursor_obj = cursor_obj
		self.row = self.cursor_obj.fetchone()
		while self.row != None:
			print(self.row)
			self.row = self.cursor_obj.fetchone()



details_dict = {
	'host' : 'localhost',
	'database' :'mydb',
	'user' :'root',
	'password' :'mypass'
}


obj = MysqlOperations(details_dict)
conn_obj = obj.connection_init_func()
cursor_obj = obj.cursor_init_func(conn_obj)
cursor_obj = obj.execute_query(cursor_obj,'select * from emp')
obj.display_result(cursor_obj)
