# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rwGt1uoHSPHC-mwPhYWzlKGwtOUHAJdA
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for tr in S:
            if tr in J:
                count=count+1
        return count