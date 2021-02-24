# Author: Mustafa Yagcioglu
# Author email: yagciogluengieering@gmail.com
# Coding date:  Feb 2021


# This Python 3 code finds the sortest path between two endpoints
# There may be some subpaths
# User has to define the links and coordinates
# Dijkstra's shortest path algorithm is used
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import math
import sys

# Function to find out which of the unvisited node
# needs to be visited next
def to_be_visited():
  global visited_and_distance
  v = -10
  # Choosing the vertex with the minimum distance
  for index in range(number_of_vertices):
    if visited_and_distance[index][0] == 0 \
      and (v < 0 or visited_and_distance[index][1] <= \
      visited_and_distance[v][1]):
        v = index
  return v

number_of_cells = 4
number_of_vertices = 7

#initializations
vertices = np.zeros((number_of_cells, number_of_vertices, number_of_vertices))
edges = np.zeros((number_of_cells, number_of_vertices, number_of_vertices))
coord = np.zeros((number_of_cells, number_of_vertices, 2))
distancelist=[]

# Creating the graph as an adjacency matrix
vertices[0] = [[0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0]]

coord[0] = np.array( [[3, 5],
          [10, 8],
          [11, 3],
          [14, 7],
          [15, 1],
          [18, 5],
          [22, 2]])


vertices[1] = [[0, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0]]

coord[1] = np.array( [[22, 2],
          [26, 4],
          [35, 8],
          [26, 9],
          [28, 13],
          [19, 9],
          [19, 13]])

vertices[2] = [[0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

coord[2] = np.array( [[19, 13],
          [21, 15],
          [24, 17],
          [30, 15],
          [34, 17],
          [46, 15],
          [38, 14]])

vertices[3] = [[0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 1, 0]]

coord[3] = np.array( [[38, 14],
          [42, 13],
          [41, 2],
          [46, 9],
          [48, 3],
          [51, 14],
          [54, 8]])

for k in range(number_of_cells):

    # Draw the vertices for debugging issues
    x, y = coord[k].T
    for i in range(coord[k].shape[0]):
        plt.text(coord[k][i,0], coord[k][i,1], str(i))
    plt.scatter(x, y)
    plt.show()


    #number_of_vertices = len(vertices[k][0])

    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            if vertices[k][i][j] == 1:
                dist = math.sqrt(math.pow((coord[k][i][0] - coord[k][j][0]),2) + math.pow((coord[k][i][1] - coord[k][j][1]),2))
                edges[k][i][j] = dist

    # The first element of the lists inside visited_and_distance
    # denotes if the vertex has been visited.
    # The second element of the lists inside the visited_and_distance
    # denotes the distance from the source.
    visited_and_distance = [[0, 0]]
    for i in range(number_of_vertices-1):
      visited_and_distance.append([0, sys.maxsize])

    for vertex in range(number_of_vertices):
      # Finding the next vertex to be visited.
      to_visit = to_be_visited()
      for neighbor_index in range(number_of_vertices):
        # Calculating the new distance for all unvisited neighbours
        # of the chosen vertex.
        if vertices[k][to_visit][neighbor_index] == 1 and \
         visited_and_distance[neighbor_index][0] == 0:
          new_distance = visited_and_distance[to_visit][1] \
          + edges[k][to_visit][neighbor_index]
          # Updating the distance of the neighbor if its current distance
          # is greater than the distance that has just been calculated
          if visited_and_distance[neighbor_index][1] > new_distance:
            visited_and_distance[neighbor_index][1] = new_distance
      # Visiting the vertex found earlier
      visited_and_distance[to_visit][0] = 1

    i = 0

    # Printing out the shortest distance from the source to each vertex
    for distance in visited_and_distance:
      print("The shortest distance of vertex ", i,\
      " from the source vertex 0 is:",distance[1])
      i = i + 1

    print("last vertex distance: ", visited_and_distance[number_of_vertices-1][1])
    distancelist.append(visited_and_distance[number_of_vertices-1][1])

#print sum of all subdistances
print("Distance from start to end: ", sum(distancelist))
