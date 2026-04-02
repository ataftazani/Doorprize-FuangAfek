import streamlit as st
import extra_streamlit_components as stx
import os

# 1. Setup Halaman
st.set_page_config(page_title="Doorprize", layout="centered")

# 2. CSS Custom agar super compact (hemat layar) & tombol jelas
st.markdown("""
    <style>
        /* Membuang ruang kosong di atas dan bawah layar */
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }
        /* Menghilangkan garis/menu bawaan Streamlit */
        header {visibility: hidden;}
        
        /* Desain tombol agar tebal, merah, dan gampang dipencet */
        .stButton>button {
            min-height: 60px;
            font-size: 22px;
            font-weight: bold;
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Menampilkan Foto (Ingat: Ganti 'banner.jpg' dengan nama file fotomu di GitHub!)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    try:
        st.image("BANNER 2026 low.jpg", use_container_width=True) 
    except:
        pass 

# 4. Teks Judul (Dibuat kecil dan padat)
st.markdown("<h4 style='text-align: center; margin-top: 5px; margin-bottom: 5px; line-height: 1.2;'>Halal Bihalal<br>Keluarga Besar Fuang Ali & Fuang Ape'</h4>", unsafe_allow_html=True)

# 5. Mesin Nomor & Cookies (INI BAGIAN YANG DIPERBAIKI)
# Langsung dipanggil tanpa cache agar tidak error
cookie_manager = stx.CookieManager(key="manager_doorprize")

def get_new_number():
    file_name = "counter.txt"
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("0")
    with open(file_name, "r") as f:
        current_num = int(f.read().strip())
    new_num = current_num + 1
    with open(file_name, "w") as f:
        f.write(str(new_num))
    return new_num

st.write("") 
user_number = cookie_manager.get(cookie="doorprize_num")

# 6. Logika Tampilan: Tombol VS Nomor Besar
if user_number is None:
    if st.button("AMBIL NOMOR", use_container_width=True):
        new_num = get_new_number()
        cookie_manager.set("doorprize_num", str(new_num), max_age=86400)
        st.rerun()
else:
    st.markdown(f"<h1 style='text-align: center; font-size: 85px; margin-top: 0px; color: #FF4B4B; line-height: 1;'>{int(user_number):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; margin-top: -15px; font-weight: bold;'>Tunjukkan layar ini ke panitia</p>", unsafe_allow_html=True)
