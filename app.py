import streamlit as st
import extra_streamlit_components as stx
import os
import time
import random
import threading  # TAMBAHAN BARU: Untuk sistem antrean anti-bentrok

# 1. Setup Halaman
st.set_page_config(page_title="Doorprize", layout="centered", initial_sidebar_state="collapsed")

# 2. CSS Custom 
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 0rem !important;
        }
        header {visibility: hidden;}
        div[data-testid="stVerticalBlock"] { gap: 0rem !important; }
        
        .stButton>button {
            min-height: 55px;
            font-size: 20px;
            font-weight: bold;
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            margin-top: 10px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Menampilkan Foto Banner
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    try:
        st.image("BANNER 2026 low.jpg", use_container_width=True) 
    except:
        pass 

# ==========================================
# 4. SISTEM MESIN NOMOR (ANTI BENTROK)
# ==========================================
cookie_manager = stx.CookieManager(key="manager_doorprize")

# Membuat Pintu Kunci (Lock) agar proses klik barengan tetap ngantre
file_lock = threading.Lock()

def get_new_number():
    with file_lock:  # <--- Ini yang menjamin nomor TIDAK AKAN PERNAH KEMBAR
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

user_number = cookie_manager.get(cookie="doorprize_num")
if user_number is None and 'temp_number' in st.session_state:
    user_number = st.session_state['temp_number']

# ==========================================
# 5. AMBIL NOMOR (Tombol / Animasi / Hasil)
# ==========================================
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
        
        wadah_teks.markdown("<p style='text-align: center; font-size: 16px; color: #A0A0A0; margin-bottom: 0px; margin-top: 10px;'>Mengacak nomor...</p>", unsafe_allow_html=True)
        
        for _ in range(15):
            angka_acak = random.randint(1, 999)
            wadah_animasi.markdown(f"<h1 style='text-align: center; font-size: 90px; margin-top: 0px; margin-bottom: 0px; color: #888888; line-height: 1;'>{angka_acak:03d}</h1>", unsafe_allow_html=True)
            time.sleep(0.08) 
            
        time.sleep(0.4)
        st.rerun()
else:
    st.markdown(f"<h1 style='text-align: center; font-size: 110px; margin-top: 0px; margin-bottom: 0px; color: #1B5E20; line-height: 1;'>{int(user_number):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; margin-top: 0px; margin-bottom: 15px; color: #B0B0B0;'>Tunjukkan layar ini ke panitia</p>", unsafe_allow_html=True)

# 6. TEKS HALAL BIHALAL
st.markdown("<hr style='margin-top: 5px; margin-bottom: 10px; border: 0; border-top: 1px solid #444444;'>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; margin-top: 0px; margin-bottom: 0px; line-height: 1.3; color: #CCCCCC;'>Nomor Doorprize Halal Bihalal<br>Keluarga Besar<br>Fuang Ali & Fuang Ape'</h5>", unsafe_allow_html=True)

# ==========================================
# 7. PANEL RAHASIA PANITIA (DISAMARKAN)
# ==========================================
# Memberikan jarak spasi yang jauh ke bawah agar terpisah dari teks utama
st.markdown("<br><br><br><br><br>", unsafe_allow_html=True) 

# Disamarkan sebagai tulisan versi aplikasi (v.1.0.0)
with st.expander("v.1.0.0"):
    pin = st.text_input("Kode Akses", type="password")
    if pin == "7268": # PIN-nya 7268
        if os.path.exists("counter.txt"):
            with open("counter.txt", "r") as f:
                total_terambil = f.read().strip()
        else:
            total_terambil = "0"
        
        st.success(f"Total partisipan: **{total_terambil} orang**")
        
        if st.button("RESET NOMOR KE 0", use_container_width=True):
            with open("counter.txt", "w") as f:
                f.write("0") 
            st.success("Direset! Memuat ulang...")
            time.sleep(1)
            st.rerun()
