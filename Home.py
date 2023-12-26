import streamlit as st
st.set_page_config(page_title="Campionati Comunali di Python")

st.title("Campionati Comunali di Python")

st.subheader("Il primo torneo simulato in Python, dove a sfidarsi sono i comuni italiani")

st.header('Come funziona?🤔')
st.text_area("","Ogni regione è stata suddivisa in gironi da 20 comuni circa ciascuno. "
                "Ogni girone prevede un calendario di partite andata e ritorno all'italiana dove ogni comune "
             "sfida gli altri. I risultati vengono simulati da Python. "
             "Al termine del processo, viene calcolata una classifica finale.")
st.info("Per scoprire le classifiche finali, fai click nella sezione Campionati a sinistra!")
st.info("Per maggiori dettagli sul procedimento, fai click nella sezione Info a sinistra!")