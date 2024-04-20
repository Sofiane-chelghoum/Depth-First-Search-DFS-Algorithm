# Depth-First Search explores as far down a branch as possible before backtracking. 
# It uses a stack (or recursion) to implement the traversal.

graph = {
    'Arad': {'Zerind', 'Sibiu', 'Timisoara'},
    'Zerind': {'Oradea', 'Arad'},
    'Oradea': {'Zerind', 'Sibiu'},
    'Sibiu': {'Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'},
    'Timisoara': {'Arad', 'Lugoj'},
    'Lugoj': {'Timisoara', 'Mehadia'},
    'Mehadia': {'Lugoj', 'Drobeta'},
    'Drobeta': {'Mehadia', 'Craiova'},
    'Craiova': {'Drobeta', 'Rimnicu Vilcea', 'Pitesti'},
    'Rimnicu Vilcea': {'Sibiu', 'Craiova', 'Pitesti'},
    'Fagaras': {'Sibiu', 'Bucharest'},
    'Pitesti': {'Rimnicu Vilcea', 'Craiova', 'Bucharest'},
    'Bucharest': {'Fagaras', 'Pitesti'}
}
def dfs_search(graph, start, goal):
    stack = [start]
    visited = {}
    came_from = {}
    visited[start] = True
    came_from[start] = None
    
    while stack:
        current = stack.pop()
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = True
                came_from[neighbor] = current
                stack.append(neighbor)
    
    return None

# Example usage
start = 'Arad'
goal = 'Bucharest'
path = dfs_search(graph, start, goal)
if path:
    print("Path from", start, "to", goal, ":", path)
else:
    print("No path found from", start, "to", goal)
