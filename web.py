import streamlit as fk
import function

toto = function.get_todos()
def liste_ekle():
    liste = fk.session_state["abo"] + "\n"
    toto.append(liste)
    function.write_todos(toto)





fk.title("Yapılacaklar Uygulaması")
fk.subheader("Benim yapacaklarım sayfası")
fk.write("Bu sayfa aktivitelerinizi artırmanıza yardımcı olacak.")

for i in toto:
    fk.checkbox(i)

fk.text_input(label="",
              placeholder="Yeni aktivite gir....", key="abo",
              on_change=liste_ekle)

