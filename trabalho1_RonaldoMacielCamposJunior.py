from queue import Queue
graph = {
  0: [1, 2],
  1: [0, 3, 4],
  2: [0, 5, 6],
  3: [1, 7, 8],
  4: [1, 9, 10],
  5: [2, 11, 12],
  6: [2, 13, 14],
  7: [3, 15, 16],
  8: [3, 17, 18],
  9: [4, 19, 20],
  10: [4, 21, 22],
  11: [5, 23, 24],
  12: [5, 25, 26],
  13: [6, 27, 28],
  14: [6],
  15: [7],
  16: [7],
  17: [8],
  18: [8],
  19: [9],
  20: [9],
  21: [10],
  22: [10],
  23: [11],
  24: [11],
  25: [12],
  26: [12],
  27: [13],
  28: [13, 29, 30],
  29: [28],
  30: [28, 31, 32],
  31: [30],
  32: [30]
}

def breadth_first_search(graph, start_vertex, end_vertex):
  visited = set()
  queue = Queue()
  queue.put(start_vertex)
  while not queue.empty():
    current_vertex = queue.get()
    if current_vertex == end_vertex:
      print(f"Found: {current_vertex}")
      return
    if current_vertex not in visited:
      print(f"Visiting: {current_vertex}")
      visited.add(current_vertex)
      for neighbor in graph[current_vertex]:
        if neighbor not in visited:
          queue.put(neighbor)
  print("Not found.")

def depth_first_search(graph, start_vertex, end_vertex):
  visited = set()
  stack = [start_vertex]
  while stack:
    current_vertex = stack.pop()
    if current_vertex == end_vertex:
      print(f"Found: {current_vertex}")
      return
    if current_vertex not in visited:
      print(f"Visiting: {current_vertex}")
      visited.add(current_vertex)
      for neighbor in reversed(graph[current_vertex]):
        if neighbor not in visited:
          stack.append(neighbor)
  print("Not found.")


if __name__ == '__main__':
  #START
  starting_vertex = int(input("Enter the starting vertex: "))
  #END
  ending_vertex = int(input("Enter the ending vertex: "))
  #TYPE
  search_type = input("Enter the search type (b for breadth-first, d for depth-first)")
  if search_type == 'b':
    breadth_first_search(graph, starting_vertex, ending_vertex)
  elif search_type == 'd':
    depth_first_search(graph, starting_vertex, ending_vertex)
  else:
    print("Invalid option.")
