import numpy as np

# Adjacency matrix
ad_matrix = [
    (0,1,0,0,1),
    (1,0,1,0,1),
    (0,1,0,1,0),
    (0,0,1,0,0),
    (1,1,0,0,0)
]
# Convert the adjacency matrix to a NumPy array
ad_matrix_np = np.array(ad_matrix)

# Print the NumPy array
print(ad_matrix_np)

# Adjacency matrix of a directed graph
ad_matrix_directed = [
    (0,1,0,0,0),
    (0,0,0,0,1),
    (0,1,0,0,0),
    (0,0,1,0,0),
    (1,0,0,0,0)
]
# Convert the adjacency matrix to a NumPy array
ad_matrix_directed_np = np.array(ad_matrix_directed)
print(ad_matrix_directed_np)

# Adjacent list of a graph directed
ad_list_directed={
    "s1":["s2"],
    "s2":["s5"],
    "s3":["s2"],
    "s4":["s3"],
    "s5":["s1"]
}
print(ad_list_directed)

# Edge list of a graph
edge_list=[
    ("s1","s2"),
    ("s1","s5"),
    ("s2","s1"),
    ("s2","s3"),
    ("s2","s5"),
    ("s3","s2"),
    ("s3","s4"),
    ("s4","s3"),
    ("s5","s1"),
    ("s5","s2")
]
print(edge_list)

# Edge list of a graph directed
edge_list_directed=[
    ("s1","s2"),
    ("s2","s5"),
    ("s3","s2"),
    ("s4","s3"),
    ("s5","s1")
]
print(edge_list_directed)


nodes=['s1','s2','s3','s4','s5']

# Adjacency list
ad_list={
    "s1":["s2","s5"],
    "s2":["s1","s3","s5"],
    "s3":["s2","s4"],
    "s4":["s3"],
    "s5":["s1","s2"]
}
print(ad_list)

# Find the degree of each node
degrees = np.sum(ad_matrix_np, axis=1)
print("Degrees of each node:", degrees)

# write a function to interconvert between adjacency matrix and adjacency list
dict1={
    0:"s1",
    1:"s2",
    2:"s3",
    3:"s4",
    4:"s5"
}
def coversion(matrix):
    adj_list = {}
    for i in range(len(matrix)):  # for each row
        adj_list[dict1[i]] = []
        for j in range(len(matrix[i])):  # for each column
            if matrix[i][j] == 1:
                adj_list[dict1[i]].append(dict1[j])
    return adj_list

print(coversion(ad_matrix))