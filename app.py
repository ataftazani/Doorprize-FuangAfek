import streamlit as st
import extra_streamlit_components as stx
import os
import time
import random

# 1. Setup Halaman (Sidebar di-set 'collapsed' agar sembunyi dari peserta)
st.set_page_config(page_title="Doorprize", layout="centered", initial_sidebar_state="collapsed")

# 2. CSS Custom (Ekstra Rapat & Kompak)
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 0rem !important;
        }
        header {visibility: hidden;}
        
        div[data-testid="stVerticalBlock"] {
            gap: 0rem !important; 
        }
        
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

# ==========================================
# 🤫 PANEL RAHASIA PANITIA (DI SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("<h3 style='text-align: center;'>🛠️ Panel Panitia</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:12px; color:gray;'>Masukkan kode rahasia untuk mereset antrian.</p>", unsafe_allow_html=True)
    
    # KODE RAHASIANYA ADALAH: fuang2026 (Bisa kamu ganti sendiri)
    kode_akses = st.text_input("Kode Akses", type="password")
    
    if kode_akses == "726828":
        st.success("Akses Terbuka!")
        if st.button("🚨 RESET SEMUA DATA 🚨", use_container_width=True):
            # 1. Reset angka counter kembali ke 0
            with open("counter.txt", "w") as f:
                f.write("0")
            
            # 2. Naikkan "Versi" Cookies agar HP peserta lama ter-reset
            if os.path.exists("version.txt"):
                with open("version.txt", "r") as f:
                    v = int(f.read().strip())
            else:
                v = 1
            with open("version.txt", "w") as f:
                f.write(str(v + 1))
            
            # 3. Hapus memori sementara di layar
            if 'temp_number' in st.session_state:
                del st.session_state['temp_number']
                
            st.success("Sistem berhasil direset! Semua peserta bisa ambil nomor baru.")
            time.sleep(2) # Beri waktu baca notif
            st.rerun()

# ==========================================
# LOGIKA MEMBACA VERSI COOKIE AKTIF
# ==========================================
if os.path.exists("version.txt"):
    with open("version.txt", "r") as f:
        cookie_version = f.read().strip()
else:
    cookie_version = "1"
    with open("version.txt", "w") as f:
        f.write("1")

# Nama cookie ini akan berubah tiap kali tombol reset dipencet (misal: doorprize_v1, doorprize_v2, dst)
NAMA_COOKIE_AKTIF = f"doorprize_v{cookie_version}"


# 3. URUTAN 1: Menampilkan Foto Banner
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    try:
        st.image("banner.jpg", use_container_width=True) 
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

# Baca dari cookies menggunakan nama cookie versi terbaru
user_number = cookie_manager.get(cookie=NAMA_COOKIE_AKTIF)
if user_number is None and 'temp_number' in st.session_state:
    user_number = st.session_state['temp_number']

# 5. URUTAN 2: AMBIL NOMOR (Tombol / Animasi / Hasil)
if user_number is None:
    wadah_tombol = st.empty()
    diklik = wadah_tombol.button("AMBIL NOMOR", use_container_width=True)
    
    if diklik:
        wadah_tombol.empty()
        
        new_num = get_new_number()
        # Simpan cookie pakai NAMA_COOKIE_AKTIF dengan umur 7 hari (604800 detik)
        cookie_manager.set(NAMA_COOKIE_AKTIF, str(new_num), max_age=604800)
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

# 6. URUTAN 3: TEKS HALAL BIHALAL DI BAWAH
st.markdown("<hr style='margin-top: 5px; margin-bottom: 10px; border: 0; border-top: 1px solid #444444;'>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; margin-top: 0px; margin-bottom: 0px; line-height: 1.3; color: #CCCCCC;'>Nomor Doorprize Halal Bihalal<br>Keluarga Besar<br>Fuang Ali & Fuang Ape'</h5>", unsafe_allow_html=True)
