#python3

import numpy as np
import pandas as pd

from Bio import SeqIO
import numpy as np 

positives_train=[]
negatives_train=[]
positives_test=[]
negatives_test=[]

for seq_record in SeqIO.parse('AMP.tr.fa', "fasta"):
    
    positives_train.append(str(seq_record.seq))
    
for seq_record in SeqIO.parse('DECOY.tr.fa', "fasta"):
    
    negatives_train.append(str(seq_record.seq))
    
for seq_record in SeqIO.parse('DECOY.te.fa', "fasta"):
    
    negatives_test.append(str(seq_record.seq)) 
    
for seq_record in SeqIO.parse('AMP.te.fa', "fasta"):
    
    positives_test.append(str(seq_record.seq))
    
    
X_train=list(positives_train+negatives_train)
X_train=np.array(X_train)

y_train=list(np.ones(np.array(positives_train).shape[0]))+list(np.zeros(np.array(negatives_train).shape[0]))
y_train=np.array(y_train)

X_test=list(positives_test+negatives_test)
X_test=np.array(X_train)

y_test=list(np.ones(np.array(positives_test).shape[0]))+list(np.zeros(np.array(negatives_test).shape[0]))
y_test=np.array(y_train)

X=list(X_train)
for i in X_test : 
    X.append(i) 

with open('peptides.txt', 'w') as f:
    for item in X:
        f.write("%s\n" % item)
