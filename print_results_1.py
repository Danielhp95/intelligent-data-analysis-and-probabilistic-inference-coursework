from IDAPICourseworkSkeleton import *


noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("Neurones.txt")
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


