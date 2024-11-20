import sys

N = 0
G = []
used = None
components = {}


def read_console():
    global N
    N = int(sys.stdin.readline().split(" ")[0])
    for line in sys.stdin:
        u, v = line.replace("\n", "").split(" ")
        G.append([int(u), int(v)])


def dfs(c_num, vertex):
    used[vertex-1] = True
    components[c_num].add(vertex)
    for u, v in G:
        if vertex == u and not used[v-1]:
            dfs(c_num, v)
        elif vertex == v and not used[u-1]:
            dfs(c_num, u)
    pass


def writeToConsole():
    len_comp = len(components.keys())
    enter = "\n"
    sys.stdout.write(str(len_comp))
    for key in components.keys():
        vertices = components.get(key)
        len_vertex = len(vertices)
        sys.stdout.write(enter + str(len_vertex) + enter)
        for vertex in vertices:
            sys.stdout.write(str(vertex) + " ")


def main():
    global used
    read_console()
    c_num = 1
    used = [False] * N
    for i in range(1, N + 1):
        if not used[i - 1]:
            components[c_num] = set()
            dfs(c_num, i)
            c_num += 1
    writeToConsole()


if __name__ == '__main__':
    main()
