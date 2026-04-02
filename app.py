import streamlit as st
import extra_streamlit_components as stx
import os
import time

# 1. Setup Halaman
st.set_page_config(page_title="Doorprize", layout="centered")

# 2. CSS Custom agar super compact
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
st.markdown("<h4 style='text-align: center; margin-top: 5px; margin-bottom: 5px; line-height: 1.2;'>Halal Bihalal<br>Keluarga Besar Fuang Ali & Fuang Ape'</h4>", unsafe_allow_html=True)

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

# Baca dari cookies
user_number = cookie_manager.get(cookie="doorprize_num")

# PENGAMAN: Jika cookies telat terbaca, baca dari memori sementara
if user_number is None and 'temp_number' in st.session_state:
    user_number = st.session_state['temp_number']

# 6. Logika Tampilan Utama
if user_number is None:
    if st.button("AMBIL NOMOR", use_container_width=True):
        new_num = get_new_number()
        
        # 1. Simpan ke Cookies (Permanen)
        cookie_manager.set("doorprize_num", str(new_num), max_age=86400)
        
        # 2. Simpan ke Memori Sementara (Langsung muncul)
        st.session_state['temp_number'] = str(new_num)
        
        # 3. Beri jeda 0.5 detik agar browser HP sempat memproses
        time.sleep(0.5)
        st.rerun()
else:
    st.markdown(f"<h1 style='text-align: center; font-size: 85px; margin-top: 0px; color: #FF4B4B; line-height: 1;'>{int(user_number):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; margin-top: -15px; font-weight: bold;'>Tunjukkan layar ini ke panitia</p>", unsafe_allow_html=True)
