import sys

idx = int(sys.argv[1])-30

myRegexLst = [r'/^0$|^10[01]$/', r'/^[01]*$/',r'/0$/', r'/\w*[aeiou]\w*[aeiou]\w*/i', r"/^1[01]*0$|^0$/",r'/^[01]*110[01]*$/',r'/^.{2,4}$/s', r"/^\d{3} *-? *\d\d *-? *\d{4}$/" , r"/^.*?d\w*/im", r"/^1[01]*1$|^0[01]*0$|^[01]?$/"]

print(myRegexLst[idx])
