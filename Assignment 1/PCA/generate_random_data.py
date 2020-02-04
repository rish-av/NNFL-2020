import pandas as pd
categories = ['X'+str(i) for i in range(15)]
data = np.random.randn(50,15)*3
last_col = [np.random.randint(0,2) for i in range(50)]
values = ["A","B","C","D","E"]
last_col1 = [values[np.random.randint(0,5)] for i in range(50)]
labels = [np.random.randint(10000,500000) for i in range(50)]

#introduction of correlation
data[:,2] = data[:,0]*3 + 4
data[:,5] = data[:,1]*4 + 1.2
data[:,7] = data[:,3]*5 + 1.1
data[:,8] = data[:,10]*10 + 1
data[:,11] = data[:,12]*7 + 4
data[:,14] = data[:,9]*4 + 44

df = pd.DataFrame(data,columns = categories)
df['X15'] = last_col
df['X16'] = last_col1
df['price'] = labels

df.to_csv('data_pca.csv')