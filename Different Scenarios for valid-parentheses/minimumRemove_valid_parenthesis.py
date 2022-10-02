def solve(s):
   stack = []
   indexes = set()
   i = 0

   for c in s:
      if c == '(':
         stack.append(i)
      elif c == ')':
         if len(stack) == 0:
            indexes.add(i)
         else:
            stack.pop()
      i += 1

   ret = ''
   indexes = indexes.union(stack)
   for i in range(len(s)):
      if i not in indexes:
         ret += s[i]

   return ret

s = "m()))n()(o)p"
print(solve(s))