#Assignment 0: Each one of the datasets has properties which makes them hard to learn. Motivate which of the three problems is most difficult for a decision tree algorithm to learn.

2 is hardest bc no dependency.  

#Assignment 1: The file dtree.py defines a function entropy which calculates the entropy of a dataset. Import this file along with the monks datasets and use it to calculate the entropy of the training datasets.

1.0 monk1
0.957117428264771 monk2
0.9998061328047111 monk3

#Assignment 2: Explain entropy for a uniform distribution and a non-uniform distribution, present some example distributions with high and low entropy.

uniform = max entropy for dataset
non-uniform = lower entropy

low entropy = dataset of people dying from coconuts
high entropy = 100 sided dice roll

#Assignment 3: 
attribute  1
0.07527255560831925
0.0037561773775118823
0.007120868396071844

attribute  2
0.005838429962909286
0.0024584986660830532
0.29373617350838865

attribute  3
0.00470756661729721
0.0010561477158920196
0.0008311140445336207

attribute  4
0.02631169650768228
0.015664247292643818
0.002891817288654397

attribute  5
0.28703074971578435
0.01727717693791797
0.25591172461972755

attribute  6
0.0007578557158638421
0.006247622236881467
0.007077026074097326

for trainingset1: attribute 5 is max
for trainingset2: attribute 6 is max
for trainingset3: attribute 2 is max

#Assignment 4: For splitting we choose the attribute that maximizes the information gain, Eq.3. Looking at Eq.3 how does the entropy of the subsets, Sk, look like when the information gain is maximized? How can we motivate using the information gain as a heuristic for picking an attribute for splitting? Think about reduction in entropy after the split and what the entropy implies.

Most information gain minimizes entropy => maximizes gain.