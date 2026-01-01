import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Brahmi Name Translator", page_icon="📜")
st.title("📜 Brahmi Name Translator")
st.write("Translate English names into Ancient Brahmi script")

# ---------------- BRAHMI MAPPING ----------------
brahmi_map = {
    "a":"𑀅","b":"𑀩","c":"𑀘","d":"𑀤","e":"𑀏","f":"𑀨","g":"𑀕",
    "h":"𑀳","i":"𑀇","j":"𑀚","k":"𑀓","l":"𑀮","m":"𑀫","n":"𑀦",
    "o":"𑀑","p":"𑀧","q":"𑀓","r":"𑀭","s":"𑀲","t":"𑀢",
    "u":"𑀉","v":"𑀯","w":"𑀯","x":"𑀓","y":"𑀬","z":"𑀚"
}

def english_to_brahmi(name):
    result = ""
    for ch in name.lower():
        if ch in brahmi_map:
            result += brahmi_map[ch]
        else:
            result += ch
    return result

# ---------------- UI ----------------
name = st.text_input("Enter a name (example: Harsh, Rama, Ashoka):")

if name:
    st.subheader("🪔 Brahmi Translation")
    st.write(english_to_brahmi(name))
