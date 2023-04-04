# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:08:04 2023

@author: Bijon
"""

class Solution:
    def romanToInt( s: str) -> int:
        num = 0
        i = 0
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "0":0 }
        dic_ex = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        s += "0"
        for n in range(0, len(s)-1):
            if i >= len(s)-1:
                break
            if dic[s[i+1]] <= dic[s[i]]:
                num += dic[s[i]]
                i += 1
            else:
                num += dic_ex[s[i]+s[i+1]]
                i += 2
        return num
                
            

if __name__ == '__main__':
    print(Solution.romanToInt("LVIII"))