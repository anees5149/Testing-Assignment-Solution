import re
s = 'I love book()'
result = re.search(r'\(\)',s)
print(result.group())
s1 = 'I love book(s)'
result2 = re.sub(r'[\(\)]','',s1)
print(result2)