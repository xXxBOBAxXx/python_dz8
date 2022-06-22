def print_all(t):
    for i in t:
        print(i[0], i[1])

def print_select(t,id):
    print(id, '<-',t[int(id)][0], '-', t[int(id)][1])

def print_task(t,id):
    for i in id:
        print(t[i][0], '-', t[i][1])
        
