#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data_andrew = pd.read_clipboard()

#Menampilkan data
print(data_andrew)


# In[2]:


andrew = data_andrew[data_andrew['Bedrooms'] == 2]

#Menampilkan nama
print(andrew)


# In[4]:


andrew['Bathrooms'] = pd.to_numeric(andrew['Bathrooms'])

import numpy as np

andrew['Bathrooms'] = andrew['Bathrooms'].apply(lambda x: 'large' if x > 2 else 'small')

#Menampilkan DataFrame setelah modifikasi
print(andrew)


# In[10]:


import numpy as np

andrew['newvariable'] = np.where(andrew['Offers'] > 2, 'large', 'small')

# Menampilkan DataFrame 'andrew' setelah penambahan kolom baru
print(andrew)


# In[11]:


# Menambahkan kolom baru 'newvariable' 
andrew['newvariable'] = andrew['Price'] / andrew['SqFt']

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(andrew)


# In[12]:


andrew = andrew.drop(columns=['newvariable'])

# Menampilkan DataFrame 'andrew' 
print(andrew)


# In[13]:


kolom1dan2 = data_andrew.iloc[:, 0:2]

# Menampilkan DataFrame kolom1dan2
print(kolom1dan2)


# In[14]:


# Memilih kolom 1 dan 2 dari DataFrame data_andrew
kolom3dan4 = data_andrew.iloc[:, 2:4]

# Menampilkan DataFrame kolom3dan4
print(kolom3dan4)


# In[15]:


# Menggabungkan dua DataFrame 
kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4], axis=1)

# Menampilkan DataFrame kolom1sd4
print(kolom1sd4)


# In[23]:


#import pandas library
import pandas as pd

# Menggabungkan baris dari dua DataFrame
baris1sd3 = data_andrew.iloc[0:3, :]
baris4sd6 = data_andrew.iloc[3:6, :]
baris1sd6 = pd.concat([baris1sd3, baris4sd6])

# Menampilkan DataFrame baris1sd6
print(baris1sd6)


# In[25]:


data_andrew_sort = data_andrew.sort_values(by='Price')

print(data_andrew_sort)


# In[6]:


import pandas as pd

data_nama = pd.read_csv("prakprob\Data_jaga_jaga_praktikum_statistika.csv")
print(data_nama)


# In[7]:


andrew = data_nama['Tinggi Badan']

#menampilkan nama
print(andrew)


# In[14]:


import pandas as pd

data_nama['Tinggi Badan'] = pd.to_numeric(data_nama['Tinggi Badan'])

import numpy as np

data_nama['Tinggi Badan'] = data_nama['Tinggi Badan'].apply(lambda x:'Tinggi' if x > 160 else 'pendek')
                                                      
#Menampilkan DataFrame
print(data_nama)                                                      


# In[27]:


import numpy as np
data_nama['Jurusan'] = 'infor20'
data_nama['Fakultas'] = 'FTI'

#Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(data_nama)


# In[29]:


data_nama = data_nama.drop(columns=['Fakultas'])

#Menampilkan DataFrame 'nama'
print(data_nama)


# In[30]:


kolom1dan2 = data_nama.iloc[:,0:2]

#menampilkan dataframe kolom1dan2
print(kolom1dan2)

#memilih kolom 1 dan 2 dari dataframe data_nama

#menampilkan dataframe kolom3dan4
print(kolom3dan4)

#menggabungkan dua dataframe
kolom1sd4 = pd.concat([kolom1dan2,kolom3dan4],axis=1)

#menampilkan dataframe kolom1sd4
print(kolom1sd4)


# In[31]:


import pandas as pd

#menggabungkan baris dua dataframe
baris1sd5 = data_nama.iloc[0:5,:]
baris25sd30 = data_nama.iloc[24:31,:]
baris1sd5dan25sd30 = pd.concat([baris1sd5, baris25sd30])

#menampilkan dataframe baris 1sd6
print(baris1sd5dan25sd30)


# In[33]:


data_nama_sort = data_nama.sort_values(by='Tinggi Badan')

print(data_nama_sort)


# In[ ]:




