import streamlit as st
import extra_streamlit_components as stx
import os
import time

# 1. Setup halaman agar pas di layar HP peserta
st.set_page_config(page_title="Doorprize Halal Bihalal", layout="centered")

# ==========================================
# BAGIAN DESAIN ACARA (BANNER & JUDUL)
# ==========================================

# Menampilkan Foto Banner dari Link
st.image("https://i.ibb.co.com/6c5hxjD1/BANNER-2026.png", use_container_width=True)

# Menampilkan Judul Acara dengan HTML/CSS agar rapi
st.markdown("<h1 style='text-align: center; margin-bottom: 0px;'>Halal Bihalal</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; margin-bottom: 0px;'>Keluarga Besar Fuang Ali & Fuang Ape'</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-top: 5px; color: #555;'>Pontianak, 4 April 2026</h3>", unsafe_allow_html=True)

# Garis pembatas tipis
st.markdown("---")

# ==========================================
# BAGIAN SISTEM DOORPRIZE
# ==========================================

# 2. Inisialisasi pengelola Cookies
cookie_manager = stx.CookieManager(key="cookie_manager")
st.write("") # Jeda rendering agar cookie siap membaca browser

# 3. Fungsi untuk mengambil nomor urut secara berurutan
def get_new_number():
    file_name = "counter.txt"
    # Jika file belum ada, buat baru mulai dari 0
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("0")
    
    # Baca nomor terakhir
    with open(file_name, "r") as f:
        current_num = int(f.read().strip())
    
    # Tambah 1 untuk nomor baru
    new_num = current_num + 1
    
    # Simpan nomor baru kembali ke file
    with open(file_name, "w") as f:
        f.write(str(new_num))
        
    return new_num

# 4. Cek apakah HP ini sudah punya nomor (baca dari cookie)
cookie_num = cookie_manager.get("doorprize_num")

# 5. Tampilan Logika Utama
# Skenario A: Jika nomor sudah ada di HP mereka
if cookie_num is not None:
    st.markdown("<h4 style='text-align: center; margin-top: 10px;'>Nomor Undian Anda:</h4>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; font-size: 100px; color: #FF4B4B; line-height: 1.1;'>{int(cookie_num):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 16px;'>Tunjukkan layar ini ke panitia saat pengundian.</p>", unsafe_allow_html=True)

# Skenario B: Jika ini adalah momen pertama kali mereka ngeklik tombol
elif "baru_dapat" in st.session_state:
    st.markdown("<h4 style='text-align: center; margin-top: 10px;'>Nomor Undian Anda:</h4>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; font-size: 100px; color: #FF4B4B; line-height: 1.1;'>{int(st.session_state.baru_dapat):03d}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 16px;'>Tunjukkan layar ini ke panitia saat pengundian.</p>", unsafe_allow_html=True)

# Skenario C: Belum punya nomor dan belum klik tombol
else:
    st.markdown("<p style='text-align: center; font-size: 18px; margin-top: 10px;'>Silakan tekan tombol di bawah untuk mendapatkan nomor.</p>", unsafe_allow_html=True)
    
    # Tombol menggunakan sedikit styling bawaan Streamlit
    if st.button("AMBIL NOMOR DOORPRIZE", use_container_width=True, type="primary"):
        # Ambil urutan nomor baru
        new_num = get_new_number()
        
        # Simpan secara permanen ke browser (Cookie)
        cookie_manager.set("doorprize_num", str(new_num), max_age=86400)
        
        # Simpan ke memori sementara agar langsung tampil di layar
        st.session_state.baru_dapat = new_num
        
        # Beri waktu 0.5 detik agar cookie di-download browser, baru refresh
        time.sleep(0.5)
        st.rerun()