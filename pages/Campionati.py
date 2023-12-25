import pandas as pd
import streamlit as st

st.title("Campionati Regionali")

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

sel_regione=st.selectbox('Scegli una regione',['Puglia','Toscana'])
if sel_regione=='Puglia':
    db_prov=pd.read_csv("https://raw.githubusercontent.com/tommyblasco/MantraCevapci/main/Dati/.csv",
                           sep=";",decimal=",")
    db_ris=pd.read_csv("https://raw.githubusercontent.com/tommyblasco/MantraCevapci/main/Dati/.csv",
                           sep=";",decimal=",")
else:
    db_prov=pd.read_csv("https://raw.githubusercontent.com/tommyblasco/MantraCevapci/main/Dati/.csv",
                           sep=";",decimal=",")
    db_ris = pd.read_csv("https://raw.githubusercontent.com/tommyblasco/MantraCevapci/main/Dati/.csv",
                          sep=";", decimal=",")
lista_gironi=tuple(sorted(set(db_ris['Gruppo'])))
sel_girone=st.selectbox('Scegli un girone',lista_gironi)

tab1, tab2, tab3 = st.tabs(["Comuni Partecipanti","Risultati","Classifica"])
db_prov_gir = db_prov[db_prov['Group']==sel_girone]
db_ris_gir = db_ris[db_ris['Gruppo']==sel_girone]
with tab1:
    st.write('Tutti i comuni del girone:')
    st.dataframe(db_prov_gir[['Nome','Prov']].sort_values('Nome'))
with tab2:
    st.write('Tutte le partite del girone:')
    st.dataframe(db_ris_gir.drop('Gruppo',axis=1))
with tab3:
    st.write('La classifica finale del girone:')
    st.dataframe(classifica(db_ris_gir))
