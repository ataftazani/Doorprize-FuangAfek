import streamlit as st
import extra_streamlit_components as stx
import os
import time
import random  # Tambahan untuk mengacak angka animasi

# 1. Setup Halaman
st.set_page_config(page_title="Doorprize", layout="centered", initial_sidebar_state="collapsed")

# 2. CSS Custom (Rekomendasi Spasi dan Margin yang lebih rapi)
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
        }
        header {visibility: hidden;}
        
        /* Desain Tombol dengan margin proporsional */
        .stButton>button {
            min-height: 60px;
            font-size: 22px;
            font-weight: bold;
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. URUTAN 1: Menampilkan Foto Banner
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    try:
        st.image("BANNER 2026 low.jpg", use_container_width=True) 
    except:
        pass 

# 4. SISTEM MESIN NOMOR & COOKIES
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

# Baca dari cookies atau memori sementara
user_number = cookie_manager.get(cookie="doorprize_num")
if user_number is None and 'temp_number' in st.session_state:
    user_number = st.session_state['temp_number']

# 5. URUTAN 2: AMBIL NOMOR (Tombol / Animasi / Hasil)
if user_number is None:
    # Buat wadah untuk tombol agar bisa disembunyikan saat ditekan
    wadah_tombol = st.empty()
    diklik = wadah_tombol.button("AMBIL NOMOR", use_container_width=True)
    
    if diklik:
        # 1. Sembunyikan tombol
        wadah_tombol.empty()
        
        # 2. Ambil nomor baru dan simpan
        new_num = get_new_number()
        cookie_manager.set("doorprize_num", str(new_num), max_age=86400)
        st.session_state['temp_number'] = str(new_num)
        
        # 3. Siapkan wadah untuk teks dan animasi angka
        wadah_teks = st.empty()
        wadah_animasi = st.empty()
        
        wadah_teks.markdown("<p style='text-align: center; font-size: 16px; color: gray; margin-bottom: -15px; margin-top: 15px;'>Mengacak nomor...</p>", unsafe_allow_html=True)
        
        # 4. LOOP ANIMASI
        for _ in range(15):
            angka_acak = random.randint(1, 999)
            # Tampilkan angka acak (abu-abu)
            wadah_animasi.markdown(f"<h1 style='text-align: center; font-size: 90px; margin-top: 10px; color: #888888; line-height: 1;'>{angka_acak:03d}</h1>", unsafe_allow_html=True)
            time.sleep(0.08) 
            
        # 5. Refresh untuk memunculkan nomor asli
        time.sleep(0.4)
        st.rerun()
else:
    # Tampilan Final Nomor (Warna Hijau Tua / #1B5E20)
    st.markdown(f"<h1 style='text-align: center; font-size: 100px; margin-top: 15px; margin-bottom: 0px; color: #1B5E20; line-height: 1;'>{int(user_number):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 15px; margin-top: 5px; margin-bottom: 25px; color: #555555;'>Tunjukkan layar ini ke panitia</p>", unsafe_allow_html=True)

# 6. URUTAN 3: TEKS HALAL BIHALAL DI BAWAH
st.markdown("<hr style='margin-top: 0px; margin-bottom: 20px; border: 0; border-top: 1px solid #EEEEEE;'>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; margin-top: 0px; margin-bottom: 10px; line-height: 1.4; color: #333333;'>Nomor Doorprize Halal Bihalal<br>Keluarga Besar<br>Fuang Ali & Fuang Ape'</h4>", unsafe_allow_html=True)
