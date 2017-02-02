from IDAPICoursework02 import *

# TABLE IS COMMUTATIVE. PRINT ONLY EVEN ENTRIES
def print_lateX_dep_list(dep_list):
    AppendString("dep_table_latex.tex",'\\begin{center}')
    AppendString("dep_table_latex.tex",'\\begin{tabular}{||c c c||}')
    AppendString("dep_table_latex.tex",'\\hline')
    AppendString("dep_table_latex.tex",'Dependency & Node & Node \\\\')
    AppendString("dep_table_latex.tex", '\\hline \\hline')
    for dep, n1, n2 in dep_list:
        AppendString("dep_table_latex.tex", str(dep) + ' & ' + str(int(n1)) + ' & ' + str(int(n2)) + '\\\\')
        AppendString("dep_table_latex.tex",'\\hline')
    AppendString("dep_table_latex.tex",'\\end{tabular}')
    AppendString("dep_table_latex.tex",'\\end{center}')
        
noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("HepatitisC.txt")
theData    = [list(x) for x in array(datain)]
noStates   = list(noStates)
dep_matrix = DependencyMatrix(theData, noVariables, noStates)
dep_list   = DependencyList(dep_matrix)
print_lateX_dep_list(dep_list)
