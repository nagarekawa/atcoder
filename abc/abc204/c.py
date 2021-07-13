


# for i in range(m):
#     group[a[i]-1][b[i]-1].append(b[i])
# for i in range(m):
#     for j in range(m):


n, m = map(int, input().split())
graph = [[] for _ in range(m)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)

    print(graph)
print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]
