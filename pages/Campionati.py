import pandas as pd
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

st.title("Campionati Regionali")
st.set_option('deprecation.showPyplotGlobalUse', False)

def classifica(df):
    df['H']=[1 if x>y else 0 for x,y in zip(df['Gol Casa'],df['Gol Tras'])]
    df['D'] = [1 if x == y else 0 for x, y in zip(df['Gol Casa'], df['Gol Tras'])]
    df['A'] = [1 if x < y else 0 for x, y in zip(df['Gol Casa'], df['Gol Tras'])]
    df['PH'] = [x * 3 + y for x, y in zip(df['H'], df['D'])]
    df['PA'] = [x * 3 + y for x, y in zip(df['A'], df['D'])]
    casa=df.groupby('Casa',as_index=False).agg({'PH':'sum','H':'sum','D':'sum','A':'sum','Gol Casa':'sum','Gol Tras':'sum'}).rename(columns={'Casa':'Squadra','PH':'Punti','H':'W','A':'L','Gol Casa':'GF','Gol Tras':'GS'})
    tras = df.groupby('Tras', as_index=False).agg(
        {'PA':'sum','A': 'sum', 'D': 'sum', 'H': 'sum', 'Gol Tras': 'sum', 'Gol Casa': 'sum'}).rename(columns={'Tras':'Squadra','PA':'Punti','A':'W','H':'L','Gol Tras':'GF','Gol Casa':'GS'})
    cl=pd.concat([casa,tras],ignore_index=True).groupby('Squadra',as_index=False).agg({'Punti':'sum','W':'sum','D':'sum','L':'sum','GF':'sum','GS':'sum'}).sort_values(['Punti'],ascending=False)
    return cl

def mappa(county,lista_com):
    italy_shp_file = "https://raw.githubusercontent.com/tommyblasco/simulazioneComuni/main/ITA_adm3.shp"
    italy_csv_file = "https://raw.githubusercontent.com/tommyblasco/simulazioneComuni/main/ITA_adm3.csv"
    gdf_italy = gpd.read_file(italy_shp_file)
    csv_ita = pd.read_csv(italy_csv_file, sep=',')
    gdf_italy['Comune'] = csv_ita['NAME_3']
    gdf_italy['Regione'] = csv_ita['NAME_1']
    regione = gdf_italy[gdf_italy['Regione']==county]
    fig, ax = plt.subplots()
    regione.boundary.plot(ax=ax, color='black')
    gruppo = gdf_italy[gdf_italy['Comune'].isin(lista_com)]
    gruppo.plot(ax=ax, color='red', legend=False)
    if county=='Apulia':
        plt.xlim([14.5, 18.5])
        plt.ylim([39.5, 42])
    else:
        plt.xlim([9.5, 13])
        plt.ylim([42, 44.5])
    #plt.show()

sel_regione=st.selectbox('Scegli una regione',['Apulia','Toscana'])
if sel_regione=='Apulia':
    db_prov=pd.read_csv("https://raw.githubusercontent.com/tommyblasco/simulazioneComuni/main/New%20Puglia.csv",
                           sep=";",decimal=",")
    db_ris=pd.read_csv("https://raw.githubusercontent.com/tommyblasco/simulazioneComuni/main/Risultati%20Puglia.csv",
                           sep=";",decimal=",")
else:
    db_prov=pd.read_csv("https://raw.githubusercontent.com/tommyblasco/simulazioneComuni/main/New%20Toscana.csv",
                           sep=";",decimal=",")
    db_ris = pd.read_csv("https://raw.githubusercontent.com/tommyblasco/simulazioneComuni/main/Risultati%20Toscana.csv",
                          sep=";", decimal=",")
lista_gironi=tuple(sorted(set(db_ris['Gruppo'])))
sel_girone=st.selectbox('Scegli un girone',lista_gironi)

db_prov_gir = db_prov[db_prov['Group']==sel_girone]
db_ris_gir = db_ris[db_ris['Gruppo']==sel_girone]

st.pyplot(mappa(county=sel_regione,lista_com=list(db_prov_gir['Nome'])))

tab1, tab2, tab3 = st.tabs(["Comuni Partecipanti","Risultati","Classifica"])
with tab1:
    st.write('Tutti i comuni del girone:')
    db_prov_gir['url_stemma']=['https://www.araldicacivica.it/wp-content/uploads/2016/04/'+str(x)+'.jpg' for x in db_prov_gir['Nome']]
    st.data_editor(db_prov_gir[['url_stemma','Nome','Prov']],
                   column_config={'url_stemma':st.column_config.ImageColumn("Stemma")},hide_index=True)
    #st.dataframe(db_prov_gir[['Nome','Prov']].sort_values('Nome'),hide_index=True)
with tab2:
    st.write('Tutte le partite del girone:')
    st.dataframe(db_ris_gir.drop('Gruppo',axis=1),hide_index=True)
with tab3:
    st.write('La classifica finale del girone:')
    st.dataframe(classifica(db_ris_gir),hide_index=True)
