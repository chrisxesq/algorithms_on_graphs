import sys
def negative_cycle(adj, cost):

    inf = 0 
    for i in cost:
        for j in i:
            if j>0:
                inf += j
    inf += 1

    dist = [inf for i in adj]
    prev = [-1  for i in adj]
    changed=0
    dist[0]=0
    #print(range(len(adj)))
    for u in range(len(adj)):
        if len(adj[u])==0:
            pass
        else:
            for i, v in enumerate(adj[u]):
                #print('i,v:',i,v)
                #print(dist,dist[u],cost[u][i])
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
    dist1=dist[:]
    for u in range(len(adj)):
        if len(adj[u])==0:
            pass
        else:            
            for i, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    changed +=1
        if dist[v] > dist[u] + cost[u][i]:
            return 1
        else:
            i += 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data=[4,4,1,2,1,4,1,2,2,3,2,1,3,5]
    #data=[5,9,1,2,4,1,3,2,2,3,2,3,2,1,2,4,2,3,5,4,5,4,1,2,5,3,3,4,4]
    #data=[3,3,1,2,7,1,3,5,2]
    #data=[4,4,1,2,-5,4,1,2,2,3,2,3,1,1]
    #data=[4,4,1,2,1,4,1,2,2,3,2,3,1,-5]
    #data=[4,4,2,1,1,4,1,2,2,3,2,1,1,-5]
    #data=[6,6,1,2,1,1,3,1,2,3,1,4,5,-1,5,6,-2,6,4,1]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
