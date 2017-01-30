#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Coursework in Python 
from IDAPICourseworkLibrary import *
from numpy import *
#
# Coursework 1 begins here
#
# Function to compute the prior distribution of the variable root from the data set
def Prior(theData, root, noStates):
    prior = zeros((noStates[root]), float )
    for i in range(len(theData)):
        prior[theData[i][root]] += 1
    prior = [ x/(len(theData)) for x in prior]
    return prior
	 
    
# Function to compute a CPT with parent node varP and xchild node varC from the data array
# it is assumed that the states are designated by consecutive integers starting with 0
def CPT(theData, varC, varP, noStates):
    cPT = zeros((noStates[varC], noStates[varP]), float )
    for i in range(cPT.shape[0]):
        for j in range(cPT.shape[1]):
            ocurrences = __count_occurences(theData, (varC,i), (varP,j)) 
            if ocurrences == 0:
                cPT[i][j] = 0
            else:
                cPT[i][j]  = (ocurrences / __count_occurences(theData, (varP,j)))
    __fix_zero_columns(cPT)
    return cPT

def __count_occurences(data_points, *var_and_state):
    occurrences = 0
    for i in range(len(data_points)):
        if (__do_states_match(data_points[i], *var_and_state)):
            occurrences += 1
    return occurrences

def __do_states_match(data_point, *var_and_state):
    for i in range(len(var_and_state)):
        variable = var_and_state[i][0] 
        state    = var_and_state[i][1]
        if data_point[variable] != state:
            return False
    return True 
    
def __fix_zero_columns(matrix):
    for j in range(len(matrix[0])):
        is_all_zero = True
        for i in range(len(matrix)):
            if matrix[i][j] != 0:
                is_all_zero = False
        if is_all_zero:
            __populate_uniformly(matrix, j)

def __populate_uniformly(matrix, column):
    for j in range(len(matrix)):
        matrix[j][column] = 1 / len(matrix)
        
        
# Function to calculate the joint probability table of two variables in the data set
def JPT(theData, varRow, varCol, noStates):
    jPT = zeros((noStates[varRow], noStates[varCol]), float )
    total_data_points = len(theData)
    for i in range(jPT.shape[0]):
        for j in range(jPT.shape[1]):
            occurrences = __count_occurences(theData, (varRow,i), (varCol,j))
            jPT[i][j] = occurrences / total_data_points
    return jPT
    
# Function to convert a joint probability table to a conditional probability table
# It creates another table, rather than changing the input table
def JPT2CPT(aJPT):
    temp = zeros((len(aJPT[0]), len(aJPT)), float)
    tr_jpt = numpy.transpose(aJPT)
    for i in range(len(tr_jpt)):
        total = sum(tr_jpt[i])
        if total == 0:
            temp[i] = numpy.full((1,len(tr_jpt[i])), 1 / len(tr_jpt[i]))
        else:
            temp[i] = [x/total for x in tr_jpt[i]]
    return numpy.transpose(temp)

#
# Function to query a naive Bayesian network
def Query(theQuery, naiveBayes): 
    rootPdf = zeros((naiveBayes[0].shape[0]), float)
# Coursework 1 task 5 should be inserted here
  

# end of coursework 1 task 5
    return rootPdf
#
# End of Coursework 1
#
# Coursework 2 begins here
#
# Calculate the mutual information from the joint probability table of two variables
def MutualInformation(jP):
    mi=0.0
# Coursework 2 task 1 should be inserted here

# end of coursework 2 task 1
    return mi
#
# construct a dependency matrix for all the variables
def DependencyMatrix(theData, noVariables, noStates):
    MIMatrix = zeros((noVariables,noVariables))
# Coursework 2 task 2 should be inserted here
    

# end of coursework 2 task 2
    return MIMatrix
# Function to compute an ordered list of dependencies 
def DependencyList(depMatrix):
    depList=[]
# Coursework 2 task 3 should be inserted here
    

# end of coursework 2 task 3
    return array(depList2)
#
# Functions implementing the spanning tree algorithm
# Coursework 2 task 4

def SpanningTreeAlgorithm(depList, noVariables):
    spanningTree = []
  
    return array(spanningTree)
#
# End of coursework 2
#

#
# main program part for Coursework 1
#
noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("Neurones.txt")
#theData = array(datain)
theData  = [list(x) for x in array(datain)]
noStates = list(noStates)
AppendString("results.txt","Coursework One Results by dfg")
AppendString("results.txt","Group members: Daniel Hernandez")
AppendString("results.txt","") #blank line
AppendString("results.txt","The prior probability of node 0")
prior = Prior(theData, 0, noStates)
AppendList("results.txt", prior)
conditional_probability = CPT(theData, 2, 0, noStates)
AppendString("results.txt", "Conditional probability p(0|2)")
AppendArray("results.txt",conditional_probability)
joint_probability       = JPT(theData, 2, 0, noStates)
AppendString("results.txt", "Joint probability p(0 & 2)")
AppendArray("results.txt",joint_probability)
converted_joint_probability = JPT2CPT(joint_probability)
AppendString("results.txt", "Converted joint to conditional probability table")
AppendArray("results.txt",converted_joint_probability)
#
# continue as described
#
#


