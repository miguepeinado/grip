import inspect
import re


def foo(a: int, b: 'annotation str'='hello') -> tuple:
    if a > 5:
        return a, b
    else:
        return 0, "less than 5"

sig = inspect.signature(foo)
print(sig.return_annotation)
code = inspect.getsource(foo)
x = code.find(chr(13))
print (x, code[:x])
pattern = re.compile('return [^\n]*')
x = re.findall(pattern, code)
print(x)
