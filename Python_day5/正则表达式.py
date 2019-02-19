# Author:GaoYuCai
#re.match从字符串开头开始匹配
#re.search从整体文本进行搜索
#re模块动态模糊的匹配字符串
#"."默认匹配出\n之外的任意一个字符
#"^"匹配字符开头
#"$"匹配以$符号之前字符结尾的字符，整个字符串以某字符结尾
#\D匹配非数字
#\w匹配[A-Za-z0-9]
#\W匹配非[A-Za-z0-9]
#\s匹配空白字符，\t \n \r
#\A只从字符开头匹配
#\z匹配字符结尾，同$
#(...) 分组匹配
#| 匹配|左|右的字符
#{n,m}匹配一个字符n到m次
#{m}匹配一个字符m次
#？ 匹配前一个字符1次或0次
#+  匹配前一个字符1次或多次
#*  匹配*号前的字符0次或多次
#使用findall方法就不需要使用group方法
#split()按什么分割
#sub替换
import re
s3=re.search("？P<id>[0-9]+","abcd1234f@34").groupdict()
s=re.match("^chen\d+","chen123Ronghua123")
print(s.group())
re.findall()#匹配所有符合的字符
print(s3)















