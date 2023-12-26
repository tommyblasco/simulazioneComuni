import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header("Procedimento, tecnica e strumenti")

st.subheader("STEP 1: Creazione gironi")
st.write("I gironi, all'interno delle varie regioni, vengono creati suddividendo il totale dei comuni \
              utilizzando il modulo *k_means_constrained* di Python, forzando il numero minimo e massimo di \
             ampiezza del cluster di comuni contigui tra loro. Un esempio a 13 gironi:")
st.code("clf = KMeansConstrained(n_clusters=13, size_min=19, size_max=20, random_state=0)")
st.subheader("STEP 2: Creazione calendario")
st.write("Una volta stabiliti i gironi e assegnato loro il nome in base alla collocazione geografica, si \
         procede alla creazione del calendario di partite andata e ritorno")
st.subheader("STEP 3: Simulazione dei risultati")
st.write("Infine, la simulazione dei risultati per il calendario appena stilato, consente di calcolare la \
         classifica finale. La simulazione avviene tramite un'estrazione casuale da una distribuzione \
         *Poisson* con parametro lambda pari alla media della media ponderata dell'attacco della squadra 1 e \
         della difesa della squadra 2 (e viceversa). La ponderazione dà peso maggiore alle partite recenti \
         per un fattore che utilizza l'esponenziale negativa:")
st.latex("W = e^{0.05(x-1)}, where  x=num. giornate")
l=st.slider("Scegli un valore per lambda:",min_value=0.5, max_value=4, value=1.5, step=0.1)
arr = np.random.poisson(l, 10000)
fig, ax = plt.subplots()
ax.hist(arr, bins=14)
st.pyplot(fig)
st.caption("Una generazione random Poisson con lambda="+str(l))
st.header("Altre ipotesi")
st.write("La distribuzione Poisson si avvicina all'ipotetica distribuzione dei gol di una squadra all'interno \
di una partita, giocando opportunamente col parametro lambda. Altre distribuzioni simili possono essere: Weibull o Skellam.")
