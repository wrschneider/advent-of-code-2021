from dijkstra import DijkstraSPF
from dijkstra.dijkstra import AbstractDijkstraSPF

input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split("\n")

input = [s.strip() for s in open("15.txt").readlines()]
input = [[int(x) for x in line] for line in input]

sz = len(input)

mx = (sz*5) - 1

class MyDijkstra(AbstractDijkstraSPF):
    @staticmethod
    def get_adjacent_nodes(G, u):
        i, j = u
        adj = []
        if i > 0:
            adj.append((i-1, j))
        if j > 0:
            adj.append((i, j-1))
        if i < mx:
            adj.append((i+1, j))
        if j < mx:
            adj.append((i, j+1))
        return adj

    @staticmethod
    def get_edge_weight(G, u, v):
        ofs = v[0] // sz + v[1] // sz
        orig = G[v[0] % sz][v[1] % sz]
        if orig + ofs > 9: 
            return orig + ofs - 9
        else: 
            return orig + ofs

m = MyDijkstra(input, (0,0))

print(m.get_distance((mx, mx)))

n1 = (0,0)
for n2 in m.get_path((mx, mx)):
  if n2[0] < n1[0] or n2[1] < n1[1]: print(n1, n2)
  n1 = n2
