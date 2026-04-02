import streamlit as st
import extra_streamlit_components as stx
import os
import time
import random  # Tambahan untuk mengacak angka animasi

# 1. Setup Halaman
st.set_page_config(page_title="Doorprize", layout="centered")

# 2. CSS Custom
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
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Menampilkan Foto (Ganti 'banner.jpg' dengan nama file di GitHub)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    try:
        st.image("BANNER 2026 low.jpg", use_container_width=True) 
    except:
        pass 

# 4. Teks Judul
st.markdown("<h4 style='text-align: center; margin-top: 5px; margin-bottom: 5px; line-height: 1.2;'>Nomor Doorprize Halal Bihalal<br>Keluarga Besar<br>Fuang Ali & Fuang Ape'</h4>", unsafe_allow_html=True)

# 5. Mesin Nomor & Cookies
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

# Baca dari cookies atau memori sementara
user_number = cookie_manager.get(cookie="doorprize_num")
if user_number is None and 'temp_number' in st.session_state:
    user_number = st.session_state['temp_number']

# 6. Logika Tampilan Utama & Animasi
if user_number is None:
    # Buat wadah untuk tombol agar bisa disembunyikan saat ditekan
    wadah_tombol = st.empty()
    diklik = wadah_tombol.button("AMBIL NOMOR", use_container_width=True)
    
    if diklik:
        # 1. Sembunyikan tombol
        wadah_tombol.empty()
        
        # 2. Ambil nomor baru dan simpan (Terjadi di belakang layar)
        new_num = get_new_number()
        cookie_manager.set("doorprize_num", str(new_num), max_age=86400)
        st.session_state['temp_number'] = str(new_num)
        
        # 3. Siapkan wadah untuk teks dan animasi angka
        wadah_teks = st.empty()
        wadah_animasi = st.empty()
        
        wadah_teks.markdown("<p style='text-align: center; font-size: 16px; color: gray; margin-bottom: -10px;'>Mengacak nomor...</p>", unsafe_allow_html=True)
        
        # 4. LOOP ANIMASI: Putar angka acak selama ~1.5 detik
        for _ in range(15):
            angka_acak = random.randint(1, 999)
            # Tampilkan angka acak dengan warna abu-abu agar terlihat sedang 'loading'
            wadah_animasi.markdown(f"<h1 style='text-align: center; font-size: 85px; margin-top: 0px; color: #CCCCCC; line-height: 1;'>{angka_acak:03d}</h1>", unsafe_allow_html=True)
            time.sleep(0.08) # Kecepatan pergantian angka
            
        # 5. Jeda sedikit untuk memastikan cookies aman, lalu refresh untuk memunculkan nomor asli
        time.sleep(0.4)
        st.rerun()
else:
    # Tampilan Final (Nomor Asli Berwarna Merah)
    st.markdown(f"<h1 style='text-align: center; font-size: 85px; margin-top: 0px; color: #FF4B4B; line-height: 1;'>{int(user_number):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; margin-top: -15px; font-weight: bold;'>Tunjukkan layar ini ke panitia</p>", unsafe_allow_html=True)
