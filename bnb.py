# 分支定界之单源最短路径https://blog.csdn.net/Gease_Gg/article/details/80621934
# 初始化图参数 用字典初始初始化这个图
G = {1: {2: 4, 3: 2, 4: 5},
     2: {5: 7, 6: 5},
     3: {6: 9},
     4: {5: 2, 7: 7},
     5: {8: 4},
     6: {10: 6},
     7: {9: 3},
     8: {10: 7},
     9: {10: 8},
     10: {}}

inf = 9999

#保存源点到各点的距离，为了让顶点和下标一致，前面多了一个inf不用在意。
length = [inf, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf]
Q = []


#FIFO队列实现
def branch(G,v0):
     Q.append(v0)
     dict=G[1]
     while len(Q)!=0:
          #队列头元素出队
          head=Q[0]
          #松弛操作，并且满足条件的后代入队
          for key in dict:
               if length[head] + G[head][key] <= length[key]:
                    length[key] = length[head] + G[head][key]
                    Q.append(key)
         #松弛完毕，队头出列
          del Q[0]
          if len(Q) != 0:
               dict = G[Q[0]]


#优先队列法实现
def branch(G, v0):
     Q.append(v0)
     while len(Q) != 0:
          min = 99999
          flag = 0
          #找到队列中距离源点最近的点
          for v in Q:
               if min > length[v]:
                    min = length[v]
                    flag = v
          head = flag
          dict=G[head]
          #找到扩散点后进行松弛操作
          for key in dict:
               if length[head] + G[head][key] <= length[key]:
                    length[key] = length[head] + G[head][key]
                    Q.append(key)
          #松弛完毕后，该扩散点出队
          Q.remove(head)

branch(G, 1)
print(length)