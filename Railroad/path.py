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


def getpath(solset, goal, canv):
    path = [str(goal[2])]
    curr = goal[2]
    while solset[curr.id] != None:
        path.append(str(solset[curr.id]))
        coords = (solset[curr.id].longitude + 130.357220) * 13, (60.846820 - solset[curr.id].latitude) * 15, (
                curr.longitude + 130.357220) * 13, (60.846820 - curr.latitude) * 15
        canv.create_line(coords, fill='blue')
        curr = solset[curr.id]
    print(path[::-1])
    print("Distance: {} miles".format(goal[1]))


def solve(root, goal, canv, top):
    if root == goal:
        return {}
    first = calcd(root.latitude, root.longitude, goal.latitude, goal.longitude)
    openset = [(first, 0, root, None)]
    heapq.heapify(openset)
    clsdset = {}
    solset = {}
    while True:
        prev = heapq.heappop(openset)
        if prev[2].id not in clsdset:
            clsdset[prev[2].id] = prev[1]
            nbr = prev[2].con
            solset[prev[2].id] = prev[3]
            if prev[2].id == goal.id:
                return getpath(solset, prev, canv, top)
            for st in nbr:
                if st.id not in clsdset:
                    delta = calcd(st.latitude, st.longitude, prev[2].latitude, prev[2].longitude) + prev[1]
                    heapq.heappush(openset, (
                        calcd(st.latitude, st.longitude, goal.latitude,
                              goal.longitude) + delta if st.id != goal.id else 0, delta, st, prev[2]))
                    coords = (prev[2].longitude + 130.357220) * 13, (60.846820 - prev[2].latitude) * 15, (
                            st.longitude + 130.357220) * 13, (60.846820 - st.latitude) * 15
                    canv.create_line(coords, fill='red')
        if prev[2] is not root:
            coords = (prev[2].longitude + 130.357220) * 13, (60.846820 - prev[2].latitude) * 15, (
                    prev[3].longitude + 130.357220) * 13, (60.846820 - prev[3].latitude) * 15
            canv.create_line(coords, fill='green')
            top.update()


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
    w = tk.Canvas(top, height=650, width=900)
    w.pack()
    # for i in stations.values():
    #     coords = (i.longitude - (-130.357220)) * 10 - 1, (60.846820 - i.latitude) * 10 - 1, (
    #                 i.longitude - (-130.357220)) * 10 + 1, (60.846820 - i.latitude) * 10 + 1
    #     w.create_oval(coords)
    for i in stations.values():
        for z in i.con:
            coords = (z.longitude + 130.357220) * 13, (60.846820 - z.latitude) * 15, (
                    i.longitude + 130.357220) * 13, (60.846820 - i.latitude) * 15
            w.create_line(coords)

    m = sys.argv[1]
    count=2
    while m not in citytoid:
        m+=' '+sys.argv[count]
        count+=1
    k=""
    for z in range(count, len(sys.argv)):
        k+=sys.argv[z]+' '

    solve(stations[citytoid[m]], stations[citytoid[k[0:-1]]], w, top)
    top.mainloop()


if __name__ == "__main__":
    main()
