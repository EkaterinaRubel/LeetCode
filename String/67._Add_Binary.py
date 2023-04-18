#Given two binary strings a and b, return their sum as a binary string.

#Example 1:
#Input: a = "11", b = "1"
#Output: "100"
#Example 2:
#Input: a = "1010", b = "1011"
#Output: "10101"
 
#Constraints:
#1 <= a.length, b.length <= 104
#a and b consist only of '0' or '1' characters.
#Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a

        b = b.rjust(len(a), '0')
        summ = []

        counter = 0
        for i in range(len(a)-1, -1, -1):
            total = int(a[i]) + int(b[i]) + counter
            if total <= 1:
                summ.append(str(total))
                counter = 0
            else:
                summ.append(str(total%2))
                counter = total // 2
                
        while counter > 0:
            summ.append(str(counter%2))
            counter = counter // 2

        return  ''.join(summ[::-1])