from collections import deque

"اضافه به ابتدا و حذف از انتها"
L=deque()
L=deque(["ali","ahmad","reza"])
L.append("javad")
L.popleft()

"اضافه به انتها و حذف از انتها"
L.append("javad")
L.pop()

"مثال صف"
q=deque()
add_q=q.append
del_q=q.popleft
add_q(10)
add_q(20)
add_q(40)
add_q(30)
print(del_q)
print(del_q)
print(del_q)
print(del_q)

"مثال پشته"
stack=deque()
push=stack.append
pop=stack.pop
push(10)
push(20)
push(40)
push(30)
print(pop)
print(pop)
print(pop)
print(pop)

"مثال صف با توجه به ظرفیت آن"
q=deque()
add_q=q.append
del_q=q.popleft
max_q=50
def q_is_full():
    if len(q)==max_q:
        return True
    return False
def q_is_empty():
    if len(q)==0:
        return True
    return False

"مثال پشته با توجه به ظرفیت آن"
stack=deque()
push=stack.append
pop=stack.pop
max_stack=50
def stack_is_full():
    if len(stack)==max_stack:
        return True
    return False
def stack_is_empty():
    if len(stack)==0:
        return True
    return False

"شبیه سازی جستجو در پوشه های کامپیوتر با استفاده از صف"
This_pc={'a':['b','c','d'],
         'b':['e','f'],
         'c':[],
         'd':['g'],
         'e':[],'f':[],'g':[]}
visited=[]
add_q('a')
visited.append('a')
while not q_is_empty():
    n=del_q()
    print(n)
    L=This_pc[n]
    for item in L:
        if item not in visited:
            add_q(item)
            visited.append(item)

"شبیه سازی جستجو در پوشه های کامپیوتر با استفاده از پشته"
This_pc={'a':['b','c','d'],
         'b':['e','f'],
         'c':[],
         'd':['g'],
         'e':[],'f':[],'g':[]}
visited=[]
push('a')
visited.append('a')
while not stack_is_empty():
    n=pop()
    print(n)
    L=This_pc[n]
    for item in L:
        if item not in visited:
            push(item)
            visited.append(item)

"بازی ماز به روش صف"
stack = deque()       # L = list()
add_stack = stack.append  # L.append
del_stack = stack.popleft # L.pop(0)

max_stack = 50
def stack_is_full():
    if len(stack)== max_stack:
        return True
    return False

def stack_is_empty():
    if len(stack)== 0:
        return True
    return False

maze = [ [0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0],
         [0, 1, 0, 1, 0] ]

def  nextSteps(n):
    x, y = n
    L = []
    if x>0 and maze[x-1][y]==0:
        L.append( (x-1,y) )
    if x<4 and maze[x+1][y]==0:
        L.append( (x+1,y) )
    if y>0 and maze[x][y-1]==0:
        L.append( (x,y-1) )
    if y<4 and maze[x][y+1]==0:
        L.append( (x,y+1) )
    return L    
        
visited = []
add_stack( (0,0) )
visited.append( (0,0) )
while not stack_is_empty():
    n = del_stack()
    print(n)
    if n==(4,4):
        print("END.")
        break;
    L = nextSteps(n)
    for item in L:
        if item not in visited:
            add_stack(item)
            visited.append( item )

"بازی ماز به روش پشته"
stack = deque()      # L = list()
push = stack.append  # L.append
pop  = stack.pop     # L.pop(0)

max_stack = 50
def stack_is_full():
    if len(stack)== max_stack:
        return True
    return False

def stack_is_empty():
    if len(stack)== 0:
        return True
    return False

maze = [ [0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0],
         [0, 1, 0, 1, 0] ]

def nextSteps(n):
    x,y = n
    L = []
    if x-1>0 and maze[x-1][y]==0:
        L.append( (x-1, y) )        
    if x+1<5 and maze[x+1][y]==0:
        L.append( (x+1, y) )        
    if y-1>0 and maze[x][y-1]==0:
        L.append( (x, y-1) )        
    if y+1<5 and maze[x][y+1]==0:
        L.append( (x, y+1) )
    return L     

visited = []
push( (0,0) )
visited.append((0,0))
while not stack_is_empty():
    n = pop()
    print(n)
    if n==(4,4):
        print("END.")
        break;
    L = nextSteps(n)
    for item in L:
        if  item not in visited:
            visited.append(item)
            push(item)
