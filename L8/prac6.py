class Emp:
	def __init__(self,eid,ename,epds):
		self.eid=eid
		self.ename=ename
		self.epds=epds
	def __mul__(self,other):
		ans=self.epds*other.nodp
		return ans
class Attendance:
	def __init__(self,nodp):
		self.nodp=nodp
	
e=Emp(10,"amit",500)
a=Attendance(25)

sal = e*a
print(sal)
