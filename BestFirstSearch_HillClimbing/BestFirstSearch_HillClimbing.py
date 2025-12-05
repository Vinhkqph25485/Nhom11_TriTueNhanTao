import heapq

class Node:
    def __init__(self, name, heuristic, parent=None):
        self.name = name
        self.heuristic = heuristic  # Heuristic value (distance to goal)
        self.parent = parent  # Parent node to trace the path

    def __lt__(self, other):
        return self.heuristic < other.heuristic  # For the priority queue (min-heap)

    def __repr__(self):
        return f"{self.name}({self.heuristic})"

def read_graph(filename):
    # Đọc đồ thị từ file
    graph = {} 
    heuristics = {}
    start, goal = None, None
    
    with open(filename, 'r', encoding='utf-8') as f:
        start, goal = f.readline().strip(), f.readline().strip()
        m = int(f.readline().strip())  # Số cạnh trong đồ thị
        for _ in range(m):
            u, v, weight = f.readline().split()
            weight = int(weight)
            graph.setdefault(u, []).append((v, weight))
            graph.setdefault(v, [])  # Đảm bảo v có trong đồ thị
        for line in f.readlines():
            node, heuristic = line.split()
            heuristics[node] = int(heuristic)
    
    return graph, heuristics, start, goal


def best_first_search(graph, heuristics, start, goal, out_file):
    open_list = []
    closed_list = set()
    start_node = Node(start, heuristics[start])
    heapq.heappush(open_list, start_node)
    closed_list.add(start)  # Đánh dấu start đã thăm để tránh quay lại
    parent = {start: None}
    step = 0

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write("Bước thực hiện thuật toán Best First Search:\n")
        f.write(f"{'TT':<5} | {'Phát triển':<10} | {'Trạng thái kề':<20} | {'Danh sách L (Open List)':<30}\n")
        f.write("-" * 80 + "\n")

        while open_list:
            current_node = heapq.heappop(open_list)
            step += 1

            # Lấy danh sách kề để in ra (chỉ để hiển thị)
            neighbors_display = [neighbor for neighbor, _ in graph.get(current_node.name, [])]
            
            # Duyệt các hàng xóm và thêm vào Open List
            for neighbor, _ in graph.get(current_node.name, []):
                if neighbor not in closed_list:
                    closed_list.add(neighbor)
                    parent[neighbor] = current_node.name
                    heapq.heappush(open_list, Node(neighbor, heuristics.get(neighbor, float('inf')), current_node))

            # Ghi thông tin bước thực hiện
            neighbors_str = ', '.join(neighbors_display) if neighbors_display else '-'
            open_list_str = ', '.join([str(n) for n in sorted(open_list)]) # Sort để hiển thị đúng thứ tự ưu tiên
            f.write(f"{step:<5} | {current_node.name:<10} | {neighbors_str:<20} | {open_list_str}\n")

            if current_node.name == goal:
                break

        # Dựng lại đường đi từ start đến goal
        if goal not in parent:
            f.write("\nKhông tìm thấy đường đi từ "
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
    graph, heuristics, start, goal = read_graph(r".\BestFirstSearch_HillClimbing\input.txt")
    best_first_search(graph, heuristics, start, goal, r".\BestFirstSearch_HillClimbing\output.txt")


if __name__ == "__main__":
    main()
