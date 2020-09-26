import win32net

f = open("test.txt","r")
enumList = []

domain = #domain\\

for line in f:
    try:
        shares,_,_ = win32net.NetShareEnum(f'{domain}{line}',0)
        enumList.append(line)
        print(shares)
    except Exception as e:
        if "denied" in str(e):
            print(f"Found {line}")
            enumList.append(line)

f.close()

print(enumList)