import monkdata as m
from dtree import entropy
from dtree import averageGain
print(entropy(m.monk1), 'monk1')
print(entropy(m.monk2), 'monk2')
print(entropy(m.monk3), 'monk3')

for i in range(6):
    print("\nattribute ", i)
    print(averageGain(m.monk1, m.attributes[i]))
    print(averageGain(m.monk2, m.attributes[i]))
    print(averageGain(m.monk3, m.attributes[i]))
    
    
    
    
    
    
    