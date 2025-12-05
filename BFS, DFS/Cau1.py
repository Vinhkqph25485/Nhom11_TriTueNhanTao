from collections import deque

def read_graph(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        m = int(f.readline().strip())   # số cạnh

        graph = {}
        for _ in range(m):
            u, v = f.readline().split()
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, [])     # đảm bảo v có trong graph

        start, goal = f.readline().split()

    # sắp xếp danh sách kề cho đẹp, ổn định
    for u in graph:
        graph[u].sort()

    return graph, start, goal


def bfs(graph, start, goal, out_file):
    q = deque([start])
    visited = {start}
    parent = {start: None}
    step = 0

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(f"Thuật toán BFS từ {start} đến {goal}\n")

        while q:
            u = q.popleft()
            step += 1

            # Ghi thông tin từng bước
            f.write(f"\nBước {step}:\n")
            f.write(f"  Đỉnh đang xét: {u}\n")

            # duyệt hàng xóm
            for v in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    parent[v] = u
                    q.append(v)

            f.write("  Hàng đợi sau khi thêm hàng xóm: " +
                    " ".join(list(q)) + "\n")
            f.write("  Tập đỉnh đã thăm: " +
                    " ".join(sorted(list(visited))) + "\n")

            if u == goal:
                break

        # dựng lại đường đi
        if goal not in parent:
            f.write("\nKhông tìm được đường đi từ "
                    f"{start} đến {goal}.\n")
            return

        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        f.write("\nĐường đi từ trạng thái đầu đến trạng thái kết thúc:\n")
        f.write("  " + " -> ".join(path) + "\n")


def main():
    graph, start, goal = read_graph(r".\BFS, DFS\input.txt")

    bfs(graph, start, goal, ".\BFS, DFS\output.txt")
from collections import deque

def read_graph(filename):
    graph = {}
    start = None
    goal = None

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("START"):
                _, start = line.split()
                continue
            
            if line.startswith("GOAL"):
                _, goal = line.split()
                continue

            u, v = line.split()
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, [])  # đảm bảo v tồn tại

    # sắp xếp cho đẹp
    for u in graph:
        graph[u].sort()

    return graph, start, goal


def bfs(graph, start, goal, out_file):
    q = deque([start])
    visited = {start}
    parent = {start: None}
    step = 0

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(f"Thuật toán BFS từ {start} đến {goal}\n")

        while q:
            u = q.popleft()
            step += 1

            f.write(f"\nBước {step}:\n")
            f.write(f"  Đỉnh đang xét: {u}\n")

            for v in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    parent[v] = u
                    q.append(v)

            f.write("  Hàng đợi sau khi thêm hàng xóm: " + " ".join(q) + "\n")
            f.write("  Tập đỉnh đã thăm: " + " ".join(sorted(visited)) + "\n")

            if u == goal:
                break

        # dựng đường đi
        if goal not in parent:
            f.write("\nKhông tìm được đường đi.\n")
            return

        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        f.write("\nĐường đi từ trạng thái đầu đến kết thúc:\n  " + " -> ".join(path))


def main():
    graph, start, goal = read_graph(r".\BFS, DFS\input.txt")

    bfs(graph, start, goal, ".\BFS, DFS\output.txt")


if __name__ == "__main__":
    main()

