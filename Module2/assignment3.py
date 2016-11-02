import pandas as pd

# TODO: Load up the dataset
df=pd.read_csv('D:/Mindtree_work_16052016/Python/Python_for_Programming_edX/Module2_Datasets/servo.csv')
# Ensuring you set the appropriate header column names
#
print df.columns


# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
dfvgain=df[df.vgain==5]
#print dfvgain
print len(dfvgain)

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
df_mtr_scr=df[(df.motor=='E') & (df.screw=='E')]
#print df_mtr_scr
print len(df_mtr_scr)

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
dfpgain= df[df.pgain==4]
print dfpgain
#len(dfpgain)
import numpy as np
print np.mean(dfpgain.vgain)

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
df.dtypes
