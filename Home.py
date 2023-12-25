import streamlit as st
st.set_page_config(page_title="Campionati Comunali di Python")

st.title("Campionati Comunali di Python")

st.subheader("Il primo torneo simulato in Python, dove a sfidarsi sono i comuni italiani")

st.header('Come funziona?🤔')
st.text_area("","Le regioni italiane sono state suddivise in N gironi, con numero di comuni contigui partecipanti "
                "quanto più simile alla Serie A italiana (20 squadre). "
                "A questo scopo abbiamo utilizzato il k_means_constrained di Python. "
                "Successivamente abbiamo creato un calendario di partite andata e ritorno stile serie A, "
                "tra i comuni che compongono i vari gironi, a cui abbiamo assegnato un nome in base all'area della regione "
                "interessata. "
             "Infine abbiamo simulato l'intero campionato per stabilire la vincitrice del girone. "
             "La simulazione del risultato è stata performata con un'estrazione causale da una distribuzione Poisson, "
                "tenendo conto della forma delle 2 squadre pesata in modo decrescente (abbiamo assegnato più valore alle "
                "partite più recenti). "
                "I pesi decrescenti sono stati ottenuti tramite una funzione esponenziale negativa.")
st.subheader("Per scoprire le classifiche finali, fai click nella sezione Campionati a sinistra!")