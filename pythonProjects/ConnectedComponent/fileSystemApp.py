N = 0
G = []
used = None
components = {}


def readFile(filename: str):
    global N
    f = open(filename)
    try:
        N = int(f.readline().split(" ")[0])
        for line in f.readlines():
            u, v = line.split(" ")
            G.append([int(u), int(v)])
    finally:
        f.close()


def writeFile(filename: str):
    f = open(filename, "w")
    try:
        len_comp = len(components.keys())
        enter = "\n"
        f.write(str(len_comp))
        for key in components.keys():
            vertices = components.get(key)
            len_vertex = len(vertices)
            f.write(enter + str(len_vertex) + enter)
            for vertex in vertices:
                f.write(str(vertex) + " ")
    finally:
        f.close()


def dfs(c_num, vertex):
    used[vertex-1] = True
    components[c_num].add(vertex)
    for u, v in G:
        if vertex == u and not used[v-1]:
            dfs(c_num, v)
        elif vertex == v and not used[u-1]:
            dfs(c_num, u)
    pass


def main():
    global used
    readFile("test3.txt")
    comp_num = 1
    used = [False] * N
    for i in range(1, N + 1):
        if not used[i - 1]:
            components[comp_num] = set()
            dfs(comp_num, i)
            comp_num += 1
    writeFile("test3_res.txt")


if __name__ == '__main__':
    main()
