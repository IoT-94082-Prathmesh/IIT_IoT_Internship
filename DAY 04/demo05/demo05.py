
import pkg2.mod3
import pkg1.mod1 as mod1

from pkg1.mod2 import test
from pkg1.mod2 import sub

print(f"module name : {__name__}")

pkg2.mod3.test()
q = pkg2.mod3.div(40, 5)
print(f"q = {q}")

mod1.test()
s = mod1.add(10, 20)
print(f"s = {s}")

test()
d = sub(20, 10)
print(f"d = {d}")
