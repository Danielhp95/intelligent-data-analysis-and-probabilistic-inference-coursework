from IDAPICourseworkLibrary import *
from numpy import *

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
    # Diagonal elements should be 0 (?)
    for i in range(len(MIMatrix)):
        for j in range(len(MIMatrix[0])):
            if i != j:
                mi = MutualInformation(JPT(theData, i, j, noStates))
                # Symmetrical matrix. Dep(A,B) = Dep(B,A)
                MIMatrix[i][j] = mi
                MIMatrix[j][i] = mi
    return MIMatrix

# Function to compute an ordered list of dependencies 
def DependencyList(depMatrix):
    depList=[]
    flattened_dep_matrix = [] 
    # Flatten dependency matrix, storing indexes.
    for i in range(len(depMatrix)):
        for j in range(len(depMatrix[0])):
            flattened_dep_matrix.append( (depMatrix[i][j], i, j) )
    depList = sorted(flattened_dep_matrix, key=lambda x: x[0])
    return array(depList)
#
# Functions implementing the spanning tree algorithm
# Coursework 2 task 4

def SpanningTreeAlgorithm(depList, noVariables):
    spanningTree = []
  
    return array(spanningTree)

#
# End of coursework 2
#

# ----- UNCOMMENT FOR SUBMISSION -------- #
noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("HepatitisC.txt")
print(datain)
#dep_matrix = DependencyMatrix()
#AppendString("results02.txt", "Group members: Daniel Hernandez Perez")
#AppendString("results02.txt", "Dependency matrix for HepatitisC:")
#AppendString("results02.txt", "")
#AppendArray("results02.txt",)
