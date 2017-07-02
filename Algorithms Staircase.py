n = int(raw_input().strip())

for i in range(1,n+1):
    spaces=n-i
    sym=i*"#"
    print spaces*" "+sym
