import pandas as pd
import numpy as np

# CSV dosyasını oku
df = pd.read_csv('DataMiningDataSetContainsNan.csv')

mean_value = round(df['Yas'].mean())  #69803 ortalama değerimiz

# 'IngilizceBilme' sütunundaki NaN değerleri ortalama ile doldurmak
df['Yas'] = df['Yas'].fillna(mean_value)

# 'Yas' değerine göre 'KnowingEnglish' sütununu güncelle
df.loc[df['Yas'] <= 20, 'IngilizceBilme'] = 0
df.loc[(df['Yas'] > 20) & (df['Yas'] <= 40), 'IngilizceBilme'] = 1
df.loc[df['Yas'] > 40, 'IngilizceBilme'] = 2

# Güncellenmiş veri setini yeni dosyaya kaydet
df.to_csv('DataMiningDataSetContainsMeanInsteadOfNan.csv', index=False)
