import tkinter as tk
import heapq
import sys
from distanceDemo import calcd


class Node:

    def __init__(self, i, lat, lon):
        self.degree = 0
        self.con = set()
        self.latitude = lat
        self.longitude = lon
        self.id = i
        self.name = ""

    def addname(self, n):
        self.name = n

    def __str__(self):
        if self.name == "":
            return self.id
        else:
            return self.name

    def addEdge(self, node):
        self.con.add(node)
        self.degree += 1

    def connect(self, other):
        self.addEdge(other)
        other.addEdge(self)


def solve(root, goal, canv, top):
    if root == goal:
        return {}
    first = calcd(root.latitude, root.longitude, goal.latitude, goal.longitude)
    openset = [(first, 0, root)]
    clsdset = {}
    solset = {}
    while True:
        prev = openset.pop()
        if prev[2].id not in clsdset:
            clsdset[prev[2].id] = prev[1]
            nbr = prev[2].con
            for st in nbr:
                if st.id not in clsdset:
                    if st.id == goal.id:
                        clsdset[goal.id] = prev[1] + calcd(prev[2].latitude, prev[2].longitude, st.latitude,
                                                           st.longitude)
                        solset[goal.id] = prev[2]
                        return solset
                    openset.append((calcd(st.latitude, st.longitude, goal.latitude, goal.longitude),
                                    prev[1] + calcd(prev[2].latitude, prev[2].longitude, st.latitude, st.longitude),
                                    st))
                    coords = (st.longitude - (-130.357220)) * 16, (60.846820 - st.latitude) * 16, (prev[2].longitude - (
                        -130.357220)) * 16, (60.846820 - prev[2].latitude) * 16
                    canv.create_line(coords, fill='blue')
                    top.update()
                    solset[st.id] = prev[2]
            if prev[2] is not root:
                coords = (prev[2].longitude - (-130.357220)) * 16 , (60.846820 - prev[2].latitude) * 16, (
                            solset[prev[2].id].longitude - (-130.357220)) * 16, (60.846820 - solset[prev[2].id].latitude) * 16
                canv.create_line(coords, fill='red')
            top.update()
        openset.sort(reverse=True)


def main():
    file = open('rrNodes.txt', "r+")
    k = file.readlines()
    stations = {line[0:7]: Node(line[0:7], float(line[8:17]), float(line[18:-1])) for line in k}
    file = open('rrNodeCity.txt', "r+")
    citytoid = {}
    k = file.readlines()
    for line in k:
        stations[line[0:7]].addname(line[8:-1])
        citytoid[line[8:-1]] = line[0:7]
    k = open('rrEdges.txt').readlines()
    for line in k:
        stations[line[0:7]].connect(stations[line[8:-1]])
    top = tk.Tk()
    w = tk.Canvas(top, height=800, width=1200)
    w.pack()
    # for i in stations.values():
    #     coords = (i.longitude - (-130.357220)) * 10 - 1, (60.846820 - i.latitude) * 10 - 1, (
    #                 i.longitude - (-130.357220)) * 10 + 1, (60.846820 - i.latitude) * 10 + 1
    #     w.create_oval(coords)
    for i in stations.values():
        for z in i.con:
            coords = (z.longitude - (-130.357220)) * 16, (60.846820 - z.latitude) * 16, (
                    i.longitude - (-130.357220)) * 16, (60.846820 - i.latitude) * 16
            w.create_line(coords)

    # m = sys.argv[1]
    # count=2
    # while m not in citytoid:
    #     m+=' '+sys.argv[count]
    #     count+=1
    # k=""
    # for z in range(count, len(sys.argv)):
    #     k+=sys.argv[z]+' '

    solve(stations[citytoid["Brooklyn"]], stations[citytoid["Los Angeles"]], w, top)
    top.mainloop()
    print(max(stations.values(), key=lambda x: x.latitude).latitude)


if __name__ == "__main__":
    main()
