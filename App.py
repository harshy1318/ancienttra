import streamlit as st

st.set_page_config(page_title="Ancient Name Translator", page_icon="📜")
st.title("📜 Ancient Language Name Translator")

st.markdown("""
Translate **names / words** between:
- English ↔ Brahmi  
- English ↔ Tamil  
- English ↔ Hebrew  
- English ↔ Aramaic  
- English ↔ Greek  
- English ↔ Latin (Old Roman)
""")

# ---------------- BRAHMI ----------------
brahmi = {
    "a":"𑀅","i":"𑀇","u":"𑀉","e":"𑀏","o":"𑀑",
    "k":"𑀓","g":"𑀕","c":"𑀘","j":"𑀚",
    "t":"𑀢","d":"𑀤","n":"𑀦",
    "p":"𑀧","m":"𑀫","y":"𑀬",
    "r":"𑀭","l":"𑀮","v":"𑀯",
    "s":"𑀲","h":"𑀳"
}
brahmi_rev = {v:k for k,v in brahmi.items()}

# ---------------- TAMIL ----------------
tamil = {
    "a":"அ","i":"இ","u":"உ","e":"எ","o":"ஒ",
    "k":"க","c":"ச","t":"த","n":"ந",
    "p":"ப","m":"ம","y":"ய","r":"ர",
    "l":"ல","v":"வ","s":"ஸ","h":"ஹ"
}
tamil_rev = {v:k for k,v in tamil.items()}

# ---------------- HEBREW ----------------
hebrew = {
    "a":"א","b":"ב","g":"ג","d":"ד","h":"ה",
    "k":"כ","l":"ל","m":"מ","n":"נ",
    "r":"ר","s":"ש","t":"ת","y":"י","v":"ו"
}
hebrew_rev = {v:k for k,v in hebrew.items()}

# ---------------- ARAMAIC ----------------
aramaic = {
    "a":"𐡀","b":"𐡁","g":"𐡂","d":"𐡃",
    "h":"𐡄","k":"𐡊","l":"𐡋","m":"𐡌",
    "n":"𐡍","r":"𐡓","s":"𐡔","t":"𐡕"
}
aramaic_rev = {v:k for k,v in aramaic.items()}

# ---------------- GREEK ----------------
greek = {
    "a":"Α","b":"Β","g":"Γ","d":"Δ","e":"Ε",
    "z":"Ζ","i":"Ι","k":"Κ","l":"Λ",
    "m":"Μ","n":"Ν","o":"Ο","p":"Π",
    "r":"Ρ","s":"Σ","t":"Τ","u":"Υ"
}
greek_rev = {v:k for k,v in greek.items()}

# ---------------- LATIN ----------------
latin = {chr(i): chr(i).upper() for i in range(97,123)}
latin_rev = {v:k for k,v in latin.items()}

# ---------------- FUNCTIONS ----------------
def to_script(text, mapping):
    return "".join(mapping.get(c.lower(), c) for c in text)

def to_english(text, reverse_map):
    return "".join(reverse_map.get(c, c) for c in text)

# ---------------- UI ----------------
mode = st.selectbox("Choose Translation Mode", [
    "English → Ancient",
    "Ancient → English"
])

text = st.text_input("Enter text:")

if text:
    if mode == "English → Ancient":
        st.subheader("Translations")
        st.write("Brahmi:", to_script(text, brahmi))
        st.write("Tamil:", to_script(text, tamil))
        st.write("Hebrew:", to_script(text, hebrew))
        st.write("Aramaic:", to_script(text, aramaic))
        st.write("Greek:", to_script(text, greek))
        st.write("Latin:", to_script(text, latin))

    else:
        st.subheader("English (phonetic)")
        st.write("From Brahmi:", to_english(text, brahmi_rev))
        st.write("From Tamil:", to_english(text, tamil_rev))
        st.write("From Hebrew:", to_english(text, hebrew_rev))
        st.write("From Aramaic:", to_english(text, aramaic_rev))
        st.write("From Greek:", to_english(text, greek_rev))
        st.write("From Latin:", to_english(text, latin_rev))
