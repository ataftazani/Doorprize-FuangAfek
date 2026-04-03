import streamlit as st
import extra_streamlit_components as stx
import os
import time
import random
import datetime  # TAMBAHAN PENTING UNTUK MENGUNCI UMUR COOKIE

# 1. Setup Halaman
st.set_page_config(page_title="Doorprize", layout="centered")

# 2. CSS Custom 
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
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
            margin-top: 15px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# LOGIKA VERSI & COUNTER
# ==========================================
def get_current_version():
    if os.path.exists("version.txt"):
        with open("version.txt", "r") as f:
            return f.read().strip()
    return "1"

def get_total_count():
    if os.path.exists("counter.txt"):
        with open("counter.txt", "r") as f:
            return f.read().strip()
    return "0"

cookie_version = get_current_version()
NAMA_COOKIE_AKTIF = f"doorprize_v{cookie_version}"

# 3. URUTAN 1: Menampilkan Foto Banner
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    try:
        st.image("BANNER 2026 low.jpg", use_container_width=True) 
    except:
        st.error("🚨 Foto 'BANNER 2026 low.jpg' tidak ditemukan di GitHub!")

# 4. SISTEM MESIN NOMOR & COOKIES
cookie_manager = stx.CookieManager(key="manager_doorprize")

def get_new_number():
    file_name = "counter.txt"
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("100")
    with open(file_name, "r") as f:
        current_num = int(f.read().strip())
    new_num = current_num + 1
    with open(file_name, "w") as f:
        f.write(str(new_num))
    return new_num

# Baca status user
user_number = cookie_manager.get(cookie=NAMA_COOKIE_AKTIF)
if user_number is None and 'temp_number' in st.session_state:
    user_number = st.session_state['temp_number']

# 5. URUTAN 2: AMBIL NOMOR (Tombol / Animasi / Hasil)
if user_number is None:
    wadah_tombol = st.empty()
    if wadah_tombol.button("AMBIL NOMOR", use_container_width=True):
        wadah_tombol.empty()
        new_num = get_new_number()
        
        # ==========================================
        # PERBAIKAN BUG SAFARI (MENGUNCI COOKIE 7 HARI)
        # ==========================================
        kunci_kadaluarsa = datetime.datetime.now() + datetime.timedelta(days=7)
        cookie_manager.set(cookie=NAMA_COOKIE_AKTIF, val=str(new_num), expires_at=kunci_kadaluarsa)
        
        st.session_state['temp_number'] = str(new_num)
        
        wadah_teks = st.empty()
        wadah_animasi = st.empty()
        wadah_teks.markdown("<p style='text-align: center; font-size: 16px; color: #A0A0A0; margin-top: 10px;'>Mengacak nomor...</p>", unsafe_allow_html=True)
        
        for _ in range(15):
            angka_acak = random.randint(1, 999)
            wadah_animasi.markdown(f"<h1 style='text-align: center; font-size: 90px; margin-top: 0px; color: #888888; line-height: 1;'>{angka_acak:03d}</h1>", unsafe_allow_html=True)
            time.sleep(0.08) 
            
        time.sleep(0.4)
        st.rerun()
else:
    st.markdown(f"<h1 style='text-align: center; font-size: 110px; margin-top: 5px; margin-bottom: 0px; color: #1B5E20; line-height: 1;'>{int(user_number):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; margin-top: 0px; margin-bottom: 20px; color: #B0B0B0;'>Tunjukkan layar ini ke panitia</p>", unsafe_allow_html=True)

# 6. URUTAN 3: TEKS HALAL BIHALAL
st.markdown("<hr style='margin-top: 10px; margin-bottom: 10px; border: 0; border-top: 1px solid #444444;'>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; margin-top: 0px; margin-bottom: 30px; line-height: 1.3; color: #CCCCCC;'>Nomor Doorprize Halal Bihalal<br>Keluarga Besar<br>Fuang Ali & Fuang Ape'</h5>", unsafe_allow_html=True)

# ==========================================
# ⚙️ PANEL PANITIA (DENGAN STATISTIK)
# ==========================================
with st.expander("⚙️"):
    total_skrg = get_total_count()
    st.markdown(f"<p style='text-align: center; font-size:16px;'><b>Total Peserta: {total_skrg}</b></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size:11px; color:gray;'>Versi Sistem: {cookie_version}</p>", unsafe_allow_html=True)
    
    kode_akses = st.text_input("Kode Akses", type="password")
    if kode_akses == "726828":
        if st.button("🚨 RESET SEMUA DATA 🚨", use_container_width=True):
            with open("counter.txt", "w") as f: f.write("0")
            v_baru = int(cookie_version) + 1
            with open("version.txt", "w") as f: f.write(str(v_baru))
            if 'temp_number' in st.session_state: del st.session_state['temp_number']
            st.success("Berhasil direset!")
            time.sleep(1.5)
            st.rerun()
