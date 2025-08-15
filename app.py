import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman
st.set_page_config(
    page_title="🎉 Selamat Ulang Tahun!",
    page_icon="🎂",
    layout="wide"
)

# Hide Streamlit style untuk tampilan lebih bersih
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
div[data-testid="stToolbar"] {visibility: hidden;}
.stApp > header {display: none;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Cache untuk performa lebih baik
@st.cache_data
def load_html():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return """
        <div style="text-align:center; padding:50px;">
            <h1>❌ File index.html tidak ditemukan!</h1>
            <p>Pastikan file index.html ada di folder yang sama dengan app.py</p>
        </div>
        """

# Load HTML content
html_content = load_html()

# Display HTML dengan full height
components.html(html_content, height=800, scrolling=True)

# Footer kecil (opsional)
st.markdown("---")
st.markdown("💝 **Made with love for your special day!** | 🚀 **Powered by Streamlit**", 
           unsafe_allow_html=True)
