import streamlit as fk
import function

toto = function.get_todos()
def liste_ekle():
    liste = fk.session_state["abo"] + "\n"
    toto.append(liste)
    function.write_todos(toto)
    fk.session_state["abo"] = ""




fk.title("Aşkım ile gün içinde yapacaklarımız")


for index, i in enumerate(toto):
    checkbox = fk.checkbox(i, key=i)
    if checkbox:
        toto.pop(index)
        function.write_todos(toto)
        del fk.session_state[i]
        fk.experimental_rerun()

fk.text_input(label="",
              placeholder="Yeni aktivite gir....", key="abo",
              on_change=liste_ekle)





