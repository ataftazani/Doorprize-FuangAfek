import streamlit as st
import extra_streamlit_components as stx
import os
import time
import random

# 1. Setup Halaman
st.set_page_config(page_title="Doorprize", layout="centered", initial_sidebar_state="collapsed")

# 2. CSS Custom untuk memastikan rata tengah dan tombol proporsional
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }
        header {visibility: hidden;}
        
        .stButton>button {
            min-height: 60px;
            font-size: 22px;
            font-weight: bold;
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Menampilkan Foto Banner (Biar ditengah, kita pakai kolom)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    try:
        # Ganti dengan nama file aslimu (banner.png atau banner.jpg)
        st.image("BANNER 2026 low.jpg", use_container_width=True) 
    except:
        pass

# 4. Teks Judul (Dipaksa Rata Tengah dengan gaya tegak/normal)
st.markdown("<h3 style='text-align: center; margin-bottom: 0;'>Halal Bihalal</h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-top: 0; margin-bottom: 0;'>Keluarga Besar</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-top: 0; margin-bottom: 20px;'>Fuang Ali & Fuang Ape'</h3>", unsafe_allow_html=True)

# 5. Mesin Nomor & Cookies (Dikembalikan seperti semula)
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
if user_number is None and 'temp_number' in st.session_state:
    user_number = st.session_state['temp_number']

# 6. Logika Tampilan & Animasi
if user_number is None:
    wadah_tombol = st.empty()
    diklik = wadah_tombol.button("AMBIL NOMOR", use_container_width=True)
    
    if diklik:
        wadah_tombol.empty()
        
        new_num = get_new_number()
        cookie_manager.set("doorprize_num", str(new_num), max_age=86400)
        st.session_state['temp_number'] = str(new_num)
        
        wadah_teks = st.empty()
        wadah_animasi = st.empty()
        
        wadah_teks.markdown("<p style='text-align: center; font-size: 16px; color: gray; margin-bottom: -15px;'>Mengacak nomor...</p>", unsafe_allow_html=True)
        
        for _ in range(15):
            angka_acak = random.randint(1, 999)
            # Animasi angka warna abu-abu
            wadah_animasi.markdown(f"<h1 style='text-align: center; font-size: 85px; margin-top: 0px; color: #888888; line-height: 1.2;'>{angka_acak:03d}</h1>", unsafe_allow_html=True)
            time.sleep(0.08)
            
        time.sleep(0.4)
        st.rerun() # <-- Kode ini yang bikin error tadi, sekarang sudah benar
else:
    # Tampilan Final (Nomor Asli Berwarna Hijau Tua / #1B5E20)
    st.markdown(f"<h1 style='text-align: center; font-size: 100px; margin-top: 10px; margin-bottom: 0px; color: #1B5E20; line-height: 1;'>{int(user_number):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 16px; margin-top: 10px; font-weight: normal;'>Tunjukkan layar ini ke panitia</p>", unsafe_allow_html=True)
