from queue import *
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F','G'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E','G'],
         'G': ['C','F']}
visited={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0}
values={'A':20,'B':10,'C':5,'D':10,'E':3,'F':60,'G':0}

def best_first(node):
    mini= 9999999
    print(node)
    if node is 'G':
        exit(0) 
    for x in graph[node]:
        if values[x]<mini:
            mini=values[x]
            node=x  
    best_first(node)    
        
best_first('A')
