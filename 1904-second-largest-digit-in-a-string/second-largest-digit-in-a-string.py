class Solution(object):
    def secondHighest(self, s):
        lar=-1
        sec=-1

        for i in range(len(s)):
            if s[i].isdigit():
                if s[i]>lar :
                    sec=lar
                    lar=s[i]
                elif s[i]>sec and s[i]<lar:
                    sec=s[i]
        sec=int(sec)
        return sec 