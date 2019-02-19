# Author:GaoYuCai
#静态方法：
#只是名义上归类管理，实际上在静态方法里访问不良类或者实例中的任何属性
class School(object):
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def grade_numbers(self):
        print("班级数量为%s"%self.grade)
    @staticmethod
    def statement(self):
        print("%s的学校好漂亮！"%self.name)
s=School("育才",12)
s.statement(s)
School.statement(s)
