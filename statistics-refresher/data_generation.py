import numpy as np
import pandas as pd
from scipy import stats

# generate some individual samples
s1 = [round(15*np.random.randn()+100,2) for i in range(100)] # normal
s2 = np.random.uniform(0,25,100) # uniform
s3 = 25000*stats.skewnorm.rvs(15, size=100) # skew normal
s4 = [round(200*np.random.randn()+1000,2) for i in range(100)] # normal
# add some for demos
s1_demo = [round(5*np.random.randn()+60,2) for i in range(100)]
s2_demo = 200*stats.skewnorm.rvs(8, size=100)

# generate some pairs of samples
p1a, p1b = 25000*stats.skewnorm.rvs(15, size=50), 30000*stats.skewnorm.rvs(10, size=50)
p2a, p2b = [round(15*np.random.randn()+100,2) for i in range(50)], [round(15*np.random.randn()+100,2) for i in range(50)]
p3a, p3b = [round(10*np.random.randn()+55,2) for i in range(50)], [round(8*np.random.randn()+65,2) for i in range(50)]
p4a, p4b = np.random.uniform(0,50,50), np.random.uniform(20,60,50) 

# add some for demos
p1a_demo, p1b_demo = [round(100*np.random.randn()+1000,2) for i in range(50)], [round(80*np.random.randn()+950,2) for i in range(50)]
p2a_demo, p2b_demo = np.random.uniform(0,500,50), np.random.uniform(50,600,50)

# put these samples in dataframes for easier sharing
samples = pd.DataFrame({'demo1':s1_demo, 'demo2':s2_demo,
                        'sample1':s1, 'sample2':s2,
                       'sample3':s3, 'sample4':s4})

pairs = pd.DataFrame({'demo1a':p1a_demo, 'demo1b':p1b_demo,
                     'demo2a':p2a_demo, 'demo2b':p2b_demo,
                     'pair1a':p1a, 'pair1b':p1b,
                     'pair2a':p2a, 'pair2b':p2b,
                     'pair3a':p3a, 'pair3b':p3b,
                     'pair4a':p4a, 'pair4b':p4b})

# export sample data for later use
samples.to_csv('individual_samples.csv', index=False)
pairs.to_csv('paired_samples.csv', index=False)