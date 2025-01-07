from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    rules = []
    updates = []
    reading_updates = False
    for line in lines:
        if ',' in line: 
            reading_updates = True
        if reading_updates:
            updates.append(line)
        else:
            rules.append(line)
    
    return rules, updates

def build_graph(rules):
    graph = defaultdict(set)
    for rule in rules:
        x, y = map(int, rule.split('|'))
        graph[x].add(y)
    return graph

def is_valid_order(update, graph):
    relevant = set(update)
    subgraph = {k: {v for v in values if v in relevant} for k, values in graph.items() if k in relevant}

    in_degree = {node: 0 for node in relevant}
    for u in subgraph:
        for v in subgraph[u]:
            in_degree[v] += 1

    queue = deque([node for node in relevant if in_degree[node] == 0])
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order == update

def reorder_update(update, graph):
    relevant = set(update)
    subgraph = {k: {v for v in values if v in relevant} for k, values in graph.items() if k in relevant}

    in_degree = {node: 0 for node in relevant}
    for u in subgraph:
        for v in subgraph[u]:
            in_degree[v] += 1

    queue = deque([node for node in relevant if in_degree[node] == 0])
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_order

def solve_puzzle(file_path):
    rules, updates = parse_input(file_path)

    graph = build_graph(rules)

    incorrect_updates = []
    for update in updates:
        update_list = list(map(int, update.split(',')))
        if not is_valid_order(update_list, graph):
            incorrect_updates.append(update_list)

    middle_pages = []
    for update in incorrect_updates:
        corrected_update = reorder_update(update, graph)
        middle_pages.append(corrected_update[len(corrected_update) // 2])

    return sum(middle_pages)

file_path = "input.txt"
result = solve_puzzle(file_path)
print("Sum of middle pages from corrected updates:", result)
