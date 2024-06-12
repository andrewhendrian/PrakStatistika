#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import scipy.stats as stats


# Data waktu produksi dari ketiga mesin
metode_A = np.array([77, 54, 67, 74, 71])
metode_B = np.array([60, 41, 59, 65, 62])
metode_C = np.array([49, 52, 69, 47, 56])


# Gabungkan data ke dalam satu array
data_andrew = [metode_A, metode_B, metode_C]


# Hitung ANOVA menggunakan scipy.stats
f_statistic, p_value = stats.f_oneway(metode_A, metode_B, metode_C)


# Tampilkan hasil
print(f"Nilai F: {f_statistic}")
print(f"Nilai p: {p_value}")


# In[2]:


import numpy as np
import scipy.stats as stats


# Data waktu produksi dari ketiga mesin
ctrl = np.array([4.17, 5.58, 5.18, 6.11, 4.5, 4.61, 5.17, 4.53, 5.33, 5.14])
trt1 = np.array([4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69])
trt2 = np.array([6.31, 5.12, 5.54, 5.50, 5.37, 5.29, 4.92, 6.15, 5.80, 5.26])


# Gabungkan data ke dalam satu array
data_andrew = [ctrl, trt1, trt2]


# Hitung ANOVA menggunakan scipy.stats
f_statistic, p_value = stats.f_oneway(ctrl, trt1, trt2)


# Tampilkan hasil
print(f"Nilai F: {f_statistic}")
print(f"Nilai p: {p_value}")

