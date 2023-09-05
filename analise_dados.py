import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import seaborn as sns  # Optional for styling

n = 8

df = pd.read_csv('clientefiftyfifty.csv')


print(df.head())

cubics = df[df['proto'].str.contains('cubic',case=False)]

renos = df[df['proto'].str.contains('reno',case=False)]

media_cubic = cubics['bps'].mean()
print('Cubic obteve uma média de transmissão de ',np.round(media_cubic/1000000,2) ,'Mbps')
media_reno = renos['bps'].mean()
print('Reno obteve uma média de transmissão de ',np.round(media_reno/1000000,2),'Mbps')

print('Reno está com uma eficácia de ',renos['bps'].mean() / cubics['bps'].mean() *100,'%')

t = 3.4995 #tabela 99% de confiança e 8 repeticoes
# np.random.standard_t()

# scipy.stats.




for proto in df['proto'].unique():
    for ber in df['ber'].unique():
        for e2e in df['e2e_delay'].unique():
             
            df_filtrado = df[(df['proto'] == proto) & (df['ber'] == ber) & (df['e2e_delay'] == e2e)]
            print(len(df_filtrado['bps']))
            intervalo = t*(df_filtrado['bps'].std()/np.sqrt(len(df_filtrado['bps'])))

            intervalo_inf = df_filtrado['bps'].mean() - t*(df_filtrado['bps'].std()/np.sqrt(len(df_filtrado['bps'])))
            intervalo_sup = df_filtrado['bps'].mean() + t*(df_filtrado['bps'].std()/np.sqrt(len(df_filtrado['bps'])))
            print('desvio padrao = ',df_filtrado['bps'].std())
            print('limite inferior do intervalo',np.round(intervalo_inf/1000000,2),'Mbps')
            print('limite superior do intervalo',np.round(intervalo_sup/1000000,2),'Mbps')
            count = 0
            for i, r in df_filtrado.iterrows():
                count += 1
                plt.bar( r['bps'],count, xerr=intervalo, align='center', alpha=0.5, ecolor='black', capsize=10)
                plt.scatter( r['bps'], count, color='g')

            plt.axvline(df_filtrado['bps'].mean(), ls='--', color='r')
            # plt.xticks([])
            plt.ylabel('Média Amostral')
            plt.show()