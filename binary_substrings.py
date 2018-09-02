s = "0110001111"#"00110011"
print s
print s.replace('01', '0 1').replace('10', '1 0')
s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
print zip(s, s[1:])
