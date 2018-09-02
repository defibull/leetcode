a = "ard=1"
s = a.strip().split("&")
for ch in s:
    if ch[:4] == 'card':
        print "found fucking card"
print s
