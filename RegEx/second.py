import sys

idx = int(sys.argv[1])-40

myRegexLst = [r'/^[xXoO\.]{64}$/', r'/^[xXoO]*\.[xXoO]*$/',r'/^\.|\.$|^[xX]+[oO]*\.|\.[oO]*[xX]+$/', r'/^.(..)*$/s', r'/^0([01]{2})*$|^1[01]([01]{2})*$/', r'/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i', r'/^0*(1+$|10$|100*)*$/', r'/^(a$|[bc]+|a[bc]*$)+a?[bc]*$/',r'/^[bc]*(a[bc]*a|b|c)+$/', r'/^(1[02]*?1|2)(1[02]*?1|2|0)*$/'] 

print(myRegexLst[idx])