class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = "".join(sorted(s))
        b = "".join(sorted(t))

        if len(a)!=len(b):
            return False

        if a==b:
            return True
        else:
            return False
        