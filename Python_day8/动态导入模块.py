# Author:GaoYuCai
import  importlib
importlib.import_module("lib.aa")#lib.aa
mod=__import__("lib.aa")#lib
instance=getattr(mod.aa,'C')
obj=instance()
print(obj.name)