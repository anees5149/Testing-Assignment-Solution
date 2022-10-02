class Solution:
   def minAddToMakeValid(self, S):
      if not S:
         return 0
      count = 0
      temp = []
      temp_counter = 0
      for i in S:
         if i =='(':
            temp.append(i)
         else:
            if len(temp)>0 and temp[len(temp)-1] =='(':
               temp.pop(len(temp)-1)
            else:
               temp.append(i)
      return len(temp)
ob = Solution()
print(ob.minAddToMakeValid("()))(()"))