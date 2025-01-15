Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
SyntaxError: multiple statements found while compiling a single statement

pip install pandas

SyntaxError: invalid syntax
import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = "/Users/leonardstaber/Documents/Uni/Semester 7/CRM/Projekt/fitness.csv"

# Load the CSV into a DataFrame
data = pd.read_csv(/Users/leonardstaber/Documents/Uni/Semester 7/CRM/Projekt/fitness.csv)

# Display the first few rows to ensure the file was loaded correctly
print(data.head())
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd
file_path = "/Users/leonardstaber/Documents/Uni/Semester 7/CRM/Projekt/fitness.csv"
data = pd.read_csv(/Users/leonardstaber/Documents/Uni/Semester 7/CRM/Projekt/fitness.csv)
SyntaxError: invalid syntax
data = pd.read_csv("/Users/leonardstaber/Documents/Uni/Semester 7/CRM/Projekt/fitness.csv")
print(data.head())
   Alter Geschlecht  Kinder Raucher   BMI  Ausgaben     Region
0     19     female       0     yes  27.9  16884.92  southwest
1     18       male       1      no  33.8   1725.55  southeast
2     28       male       3      no  33.0   4449.46  southeast
3     33       male       0      no  22.7  21984.47  northwest
4     32       male       0      no  28.9   3866.86  northwest
print(data.info())

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Alter       1338 non-null   int64  
 1   Geschlecht  1338 non-null   object 
 2   Kinder      1338 non-null   int64  
 3   Raucher     1338 non-null   object 
 4   BMI         1338 non-null   float64
 5   Ausgaben    1338 non-null   float64
 6   Region      1338 non-null   object 
dtypes: float64(2), int64(2), object(3)
memory usage: 73.3+ KB
None
>>> print(data.isnull().sum())
... 
Alter         0
Geschlecht    0
Kinder        0
Raucher       0
BMI           0
Ausgaben      0
Region        0
dtype: int64
>>> print(data.describe())
... 
             Alter       Kinder          BMI      Ausgaben
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.207025     1.094918    30.665471  13270.422414
std      14.049960     1.205493     6.098382  12110.011240
min      18.000000     0.000000    16.000000   1121.870000
25%      27.000000     0.000000    26.300000   4740.287500
50%      39.000000     1.000000    30.400000   9382.030000
75%      51.000000     2.000000    34.700000  16639.915000
max      64.000000     5.000000    53.100000  63770.430000
>>> data[‘Geschlecht’] = LabelEncoder().fit_transform(data[‘Geschlecht’])
SyntaxError: invalid character '‘' (U+2018)
>>> data["Geschlecht"] = LabelEncoder().fit_transform(data[‘Geschlecht’])
SyntaxError: invalid character '‘' (U+2018)
>>> data[“Geschlecht”] = LabelEncoder().fit_transform(data[“Geschlecht”])
... 
SyntaxError: invalid character '“' (U+201C)
>>> data[Geschlecht] = LabelEncoder().fit_transform(data[Geschlecht])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data[Geschlecht] = LabelEncoder().fit_transform(data[Geschlecht])
NameError: name 'LabelEncoder' is not defined
>>> data['Geschlecht'] = LabelEncoder().fit_transform(data['Geschlecht'])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data['Geschlecht'] = LabelEncoder().fit_transform(data['Geschlecht'])
NameError: name 'LabelEncoder' is not defined
>>> from sklearn.preprocessing import StandardScaler, LabelEncoder
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    from sklearn.preprocessing import StandardScaler, LabelEncoder
ModuleNotFoundError: No module named 'sklearn'
>>> from sklearn.preprocessing import StandardScaler, LabelEncoder
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    from sklearn.preprocessing import StandardScaler, LabelEncoder
ModuleNotFoundError: No module named 'sklearn'
>>> from sklearn.preprocessing import StandardScaler, LabelEncoder
>>> data[“Geschlecht”] = LabelEncoder().fit_transform(data[“Geschlecht”])
SyntaxError: invalid character '“' (U+201C)
>>> data['Geschlecht'] = LabelEncoder().fit_transform(data['Geschlecht'])
>>> data['Raucher'] = LabelEncoder().fit_transform(data['Raucher'])
>>> data = pd.get_dummies(data, columns=[‘Region’], drop_first=True)
SyntaxError: invalid character '‘' (U+2018)
>>> data = pd.get_dummies(data, columns=['Region'], drop_first=True)
