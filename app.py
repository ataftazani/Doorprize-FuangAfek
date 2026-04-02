import streamlit as st
import extra_streamlit_components as stx
import os
import time

# 1. Setup Halaman agar gelap dan rapi
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 2. Definisikan CSS yang Detail untuk Centering, Warna, dan Gaya
# Ganti warna hijau norak menjadi hijau tua yang elegan (#1B5E20)
css = """
    <style>
        /* Sembunyikan menu Streamlit untuk tampilan app bersih */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .main {background-color: #121212;}
        .reportview-container .main .block-container{padding-top: 1rem; padding-bottom: 0rem; padding-left: 1rem; padding-right: 1rem; color: #E0E0E0;}

        /* CSS untuk memusatkan semua konten */
        .centered-content {text-align: center; display: flex; flex-direction: column; align-items: center;}
        .banner-container {width: 100%; max-width: 600px; border-radius: 12px; overflow: hidden; margin-bottom: 2rem;}
s
        /* CSS untuk Gaya Teks: Tegak, Tebal, dan Sempurna di Tengah */
        .main-title {font-weight: bold; font-size: 1.5rem; margin-top: 1rem; margin-bottom: 0.5rem; color: #E0E0E0;}
        .sub-title {font-weight: bold; font-size: 1.8rem; margin-top: 0rem; margin-bottom: 1rem; color: #E0E0E0;}
        .main-subtitle-desc {font-weight: bold; font-size: 1.5rem; margin-top: 0rem; margin-bottom: 2rem; color: #E0E0E0;}

        /* CSS untuk Tampilan Nomor: Besar, Tebal, Tegak, Hijau Tua */
        .number-display {font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 8rem; color: #1B5E20; margin-top: 2rem; margin-bottom: 1rem; text-align: center; }
        .number-instruction {font-size: 1rem; color: #A0A0A0; font-weight: 400; margin-bottom: 3rem; text-align: center;}
        
        /* CSS untuk Tombol Ambil Nomor (untuk keadaan awal) */
        .stButton>button {width: 100%; border-radius: 20px; border: 2px solid #ff4b4b; color: white; background-color: #ff4b4b; font-size: 1.2rem; font-weight: bold; padding: 1rem; margin-bottom: 2rem;}
        
        .disclaimer {font-size: 0.8rem; color: #606060; font-weight: 300; margin-top: 1rem; text-align: center;}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# 3. State management untuk persistensi nomor
if 'number' not in st.session_state:
    st.session_state.number = None

# Fungsi untuk menampilkan nomor final
def display_final_number(number_str):
    with st.container():
        st.markdown(f'<div class="centered-content">', unsafe_allow_html=True)
        
        # Muat gambar banner (asumsi file bernama 'banner.png') dan pusatkan
        try:
            st.image('BANNER 2026 low.jpg', use_column_width=True)
        except:
            st.warning("Pastikan file 'banner.png' ada di folder aplikasi Anda.")

        # Judul Tegak, Tebal, Centered
        st.markdown(f'<div class="main-title">Halal Bihalal</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sub-title">Keluarga Besar</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="main-subtitle-desc">Fuang Ali & Fuang Ape\'</div>', unsafe_allow_html=True)

        # Bagian Nomor: Tegak, Hijau Tua, Besar, Centered
        st.markdown(f'<div class="number-display">{number_str}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="number-instruction">Tunjukkan layar ini kepada panitia saat pengambilan hadiah.</div>', unsafe_allow_html=True)
        st.markdown(f'</div>', unsafe_allow_html=True)

# Fungsi untuk menampilkan keadaan awal (sebelum ambil nomor)
def display_initial_state():
    with st.container():
        st.markdown(f'<div class="centered-content">', unsafe_allow_html=True)
        # Muat gambar banner (asumsi file bernama 'banner.png') dan pusatkan
        try:
            st.image('banner.png', use_column_width=True)
        except:
            pass

        # Judul Tegak, Tebal, Centered
        st.markdown(f'<div class="main-title">Halal Bihalal</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sub-title">Keluarga Besar</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="main-subtitle-desc">Fuang Ali & Fuang Ape\'</div>', unsafe_allow_html=True)

        if st.button("Ambil Nomor Doorprize"):
            # Animasi (acak nomor sebentar)
            with st.spinner("Mengacak nomor..."):
                import time
                time.sleep(1.5) # Durasi animasi
            st.session_state.number = "012" # Nomor mock
            st.experimental_rerun() # Refresh untuk menampilkan nomor

        st.markdown(f'</div>', unsafe_allow_html=True)

# Tampilkan halaman berdasarkan state nomor
if st.session_state.number:
    display_final_number(st.session_state.number)
else:
    display_initial_state()
