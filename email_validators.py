'''
Author : Dhruv B Kakadiya

'''

import re
def fun(s):
    if ('@' not in s) or ('.' not in s) or (' ' in s):

            return False

    if s.count('@')>1:

            return False

    if s.count('.')>1:

            return False

    s=s.replace('@',' ')

    s=s.replace('.',' ')

    l=list(map(str,s.split()))

    if len(l)<3:

            return False

    for j in l[0]:

            if j.isalnum()==False and j!='_' and j!='-':

                    return False
    for j in l[1]:

        if j.isalnum()==False:
            return False
    if len(l[2])>3 or len(l[2])==0:
        return False
    return True