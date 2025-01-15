Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
file_path = "/Users/leonardstaber/Documents/Uni/GitHub/CRMProjekt/fitness.csv"
data = pd.read_csv("/Users/leonardstaber/Documents/Uni/GitHub/CRMProjekt/fitness.csv")
print(data.head())
   Alter Geschlecht  Kinder Raucher   BMI  Ausgaben     Region
0     19     female       0     yes  27.9  16884.92  southwest
1     18       male       1      no  33.8   1725.55  southeast
2     28       male       3      no  33.0   4449.46  southeast
3     33       male       0      no  22.7  21984.47  northwest
4     32       male       0      no  28.9   3866.86  northwest
print(data.isnull().sum()) #check NAs
Alter         0
Geschlecht    0
Kinder        0
Raucher       0
BMI           0
Ausgaben      0
Region        0
dtype: int64
print(data.describe())
             Alter       Kinder          BMI      Ausgaben
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.207025     1.094918    30.665471  13270.422414
std      14.049960     1.205493     6.098382  12110.011240
min      18.000000     0.000000    16.000000   1121.870000
25%      27.000000     0.000000    26.300000   4740.287500
50%      39.000000     1.000000    30.400000   9382.030000
75%      51.000000     2.000000    34.700000  16639.915000
max      64.000000     5.000000    53.100000  63770.430000
data['Geschlecht'] = LabelEncoder().fit_transform(data['Geschlecht'])
data['Raucher'] = LabelEncoder().fit_transform(data['Raucher'])
data = pd.get_dummies(data, columns=[‘Region’], drop_first=True)
SyntaxError: invalid character '‘' (U+2018)
data = pd.get_dummies(data, columns=['Region'], drop_first=True)
features = ['Alter’, ‘Geschlecht’, ‘Kinder’, ‘Raucher’, 'BMI', ‘Ausgaben’] + \
           [col for col in data.columns if col.startswith('Region_')] # Select relevant features for clustering
            
SyntaxError: unterminated string literal (detected at line 2)
features = ['Alter', 'Geschlecht', 'Kinder', 'Raucher', 'BMI', 'Ausgaben'] + \
           [col for col in data.columns if col.startswith('Region_')] # Select relevant features for clustering
            
scaler = StandardScaler()
            
scaled_data = scaler.fit_transform(data[features]) # Normalize data CHECK TO SEE F THEY HAVE BEEN TRANSFORMED
            
print(data.head())
            
   Alter  Geschlecht  ...  Region_southeast  Region_southwest
0     19           0  ...             False              True
1     18           1  ...              True             False
2     28           1  ...              True             False
3     33           1  ...             False             False
4     32           1  ...             False             False

[5 rows x 9 columns]
intertia = []
            
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

            
KMeans(n_clusters=1, random_state=42)
Traceback (most recent call last):
  File "<pyshell#19>", line 4, in <module>
    inertia.append(kmeans.inertia_)
NameError: name 'inertia' is not defined. Did you mean: 'intertia'?
inertia = []
            
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

            
KMeans(n_clusters=1, random_state=42)
KMeans(n_clusters=2, random_state=42)
KMeans(n_clusters=3, random_state=42)
KMeans(n_clusters=4, random_state=42)
KMeans(n_clusters=5, random_state=42)
KMeans(n_clusters=6, random_state=42)
KMeans(n_clusters=7, random_state=42)
KMeans(random_state=42)
KMeans(n_clusters=9, random_state=42)
KMeans(n_clusters=10, random_state=42)
import matplotlib.pyplot as plt
plt.plot(range(1, 11), inertia, marker='o')
[<matplotlib.lines.Line2D object at 0x123a70f50>]
plt.xlabel('Number of Clusters')
Text(0.5, 47.04444444444444, 'Number of Clusters')
plt.ylabel('SSE(Inertia)')
Text(40.81944444444443, 0.5, 'SSE(Inertia)')
plt.title('Elbow Method')
Text(0.5, 1.0, 'Elbow Method')
plt.show()
optimal_cluster = 5

kmeans = KMeans(n_clusters = optimal_cluster, random_state = 42)
data['Cluster'] = kmeans.fit_predict(scaled_data)
cluster_summary = data.groupby('Cluster').mean()
print(cluster_summary)
             Alter  Geschlecht  ...  Region_southeast  Region_southwest
Cluster                         ...                                    
0        39.536965    0.486381  ...             0.000             0.000
1        38.538732    0.485915  ...             0.000             0.000
2        38.673993    0.490842  ...             1.000             0.000
3        39.894161    0.463504  ...             0.000             1.000
4        39.456000    0.608000  ...             0.364             0.204

[5 rows x 9 columns]
cluster_summary.head(len(cluster_summary))
             Alter  Geschlecht  ...  Region_southeast  Region_southwest
Cluster                         ...                                    
0        39.536965    0.486381  ...             0.000             0.000
1        38.538732    0.485915  ...             0.000             0.000
2        38.673993    0.490842  ...             1.000             0.000
3        39.894161    0.463504  ...             0.000             1.000
4        39.456000    0.608000  ...             0.364             0.204

[5 rows x 9 columns]
>>> pd.set_option('display.max_columns', None)  # Show all columns
... pd.set_option('display.max_rows', None)
SyntaxError: multiple statements found while compiling a single statement
>>> pd.set_option('display.max_columns', None)  # Show all columns
>>> pd.set_option('display.max_rows', None)
>>> head(cluster_summary)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    head(cluster_summary)
NameError: name 'head' is not defined
>>> cluster_summary.head(len(cluster_summary))
             Alter  Geschlecht    Kinder   Raucher        BMI      Ausgaben  \
Cluster                                                                       
0        39.536965    0.486381  1.046693  0.000000  29.333852   9165.531946   
1        38.538732    0.485915  1.098592  0.059859  29.015493   9146.111866   
2        38.673993    0.490842  1.065934  0.000000  33.444689   8032.216300   
3        39.894161    0.463504  1.124088  0.025547  30.322263   8247.839927   
4        39.456000    0.608000  1.140000  1.000000  31.250000  33400.338080   

         Region_northwest  Region_southeast  Region_southwest  
Cluster                                                        
0                   0.000             0.000             0.000  
1                   1.000             0.000             0.000  
2                   0.000             1.000             0.000  
3                   0.000             0.000             1.000  
4                   0.164             0.364             0.204  
>>> from sklearn.decomposition import PCA
>>> pca = PCA(n_components = 2)
>>> reduced_data = pca.fit_transform(scaled_data)
>>> plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=data['Cluster'], cmap='viridis', s=50)
<matplotlib.collections.PathCollection object at 0x123aa9400>
>>> plt.title('Cluster Visualization')
Text(0.5, 1.0, 'Cluster Visualization')
>>> plt.xlabel('PCA 1')
Text(0.5, 47.04444444444444, 'PCA 1')
>>> plt.ylabel('PCA 2')
Text(88.44444444444443, 0.5, 'PCA 2')
>>> plt.colorbar(label='Cluster')
<matplotlib.colorbar.Colorbar object at 0x123aa97f0>
>>> plt.show()
