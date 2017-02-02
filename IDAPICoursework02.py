from IDAPICourseworkLibrary import *
from IDAPICourseworkSkeleton import *
from numpy import *
from collections import deque

# Coursework 2 begins here
#
# Calculate the mutual information from the joint probability table of two variables
def MutualInformation(jP):
    mi=0.0
    marginal_states_a = numpy.array(jP).sum(axis=1)
    marginal_states_b = numpy.array(jP).sum(axis=0)
    for i in range(len(jP)):
        for j in range(len(jP[0])):
            if jP[i][j] != 0:
                denominator = marginal_states_a[i] * marginal_states_b[j]
                mi += jP[i][j] * numpy.log2(jP[i][j] / denominator)
    return mi

def marginalise_probability(jpt):
    p_b = sum([ sum(x) for x in jpt])
    p_a = sum([ sum(x) for x in numpy.transpose(jpt)])
    return p_a, p_b
        
#
# construct a dependency matrix for all the variables
def DependencyMatrix(theData, noVariables, noStates):
    MIMatrix = zeros((noVariables,noVariables))
    # Diagonal elements should be 0
    for i in range(len(MIMatrix)):
        for j in range(i+1, len(MIMatrix[0])):
            if i != j:
                mi = MutualInformation(JPT(theData, i, j, noStates))
                # Symmetrical matrix. Dep(A,B) = Dep(B,A)
                MIMatrix[i][j] = mi
                MIMatrix[j][i] = mi
            else:
                MIMatrix[i][i] = 0 
    return MIMatrix

# Function to compute an ordered list of dependencies
def DependencyList(depMatrix):
    depList=[]
    flattened_dep_matrix = [] 
    # Flatten dependency matrix, storing indexes.
    for i in range(len(depMatrix)):
        for j in range(len(depMatrix[0])):
            flattened_dep_matrix.append( (depMatrix[i][j], i, j) )
    # Cool python. indexing using [::2] gets every other element.
    depList = sorted(flattened_dep_matrix, key=lambda x: x[0], reverse=True)
    return array(depList)
#
# Functions implementing the spanning tree algorithm
# Coursework 2 task 4

# Assumes that depList is already sorted
def SpanningTreeAlgorithm(depList, noVariables):
    spanningTree = []
    threshold = 100
    highest_dependency, _, _ = depList[0]

    i = 0
    current_depedency, n1, n2 = dep_matrix[i]
    while highest_dependency > current_depedency * threshold:
        if not checkForLoop(spanningTree, n1, n2):
            spanningTree.append([n1,n2])
        i += 1
        current_depedency, n1, n2 = dep_matrix[i]

    return array(spanningTree)

# Checks if adding node would create a loop. Performs breadth first traversal
def checkForLoop(spanningTree, n1, n2):
    breadth_queue = deque()
    visited = [n1]
    breadth_queue.append( (n1, n2) )
    while len(breadth_queue) > 0:
        _, node = breadth_queue.popleft()
        visited.append(node) 
        for p, c in spanningTree:
            if p == node:
                if c in visited:
                    return True
                else:
                    breadth_queue.append( (node, c) )
    return False





# ----- UNCOMMENT FOR SUBMISSION -------- #
numpy.set_printoptions(suppress=True) # In order without scientific notation

noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("HepatitisC.txt")
theData    = [list(x) for x in array(datain)]
noStates   = list(noStates)
dep_matrix = DependencyMatrix(theData, noVariables, noStates)
dep_list   = DependencyList(dep_matrix)
#print(dep_list)

#AppendString("results02.txt", "Group members: Daniel Hernandez Perez")
#AppendString("results02.txt", "Dependency matrix for HepatitisC:")
#AppendString("results02.txt", "")
#AppendArray("results02.txt",)
