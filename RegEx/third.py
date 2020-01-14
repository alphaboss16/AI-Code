import sys

idx = int(sys.argv[1])-50

myRegexLst = [r'/\w*(\w)\w*\1\w*/i', r'/\w*(\w)(\w*\1\w*){3}/i', r'/^(0|1)[01]*\1$|^[01]$/', r'/(?=\b(\w){6}\b)\w*cat\w*/i', r'/(?=\b(\w){5,9}\b)(?=\w*bri\w*)(?=\w*ing\w*)\w*/i', r'/(?!\w*cat\w*)\b\w{6}\b/i', r'/(?!\w*(\w)\w*\1\w*|\b[ .]|\b$)\b\w*\b/i', r'/(?=^[01]*$)(?!.*10011).*/', r'/\w*([aeiou])(?!\1)[aeiou]\w*/i', r'/(?=^[01]*$)(?!.*(101|111)).*/'] 

print(myRegexLst[idx])