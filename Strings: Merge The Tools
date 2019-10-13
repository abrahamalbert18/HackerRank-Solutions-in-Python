def merge_the_tools(string, k):
    # your code goes here
    n = len(string)

    for i in range(int(n/k)):
        print(sub_task(string[i*k:(i*k)+k]))

def sub_task(string):
    string_set = set(string)
    u = ""
    for s in string:
        if s not in u and s in string_set:
            u += s
    return u
