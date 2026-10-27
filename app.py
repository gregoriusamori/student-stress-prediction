import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Deteksi Dini Kesehatan Mental Mahasiswa",
    page_icon="🧠",
    layout="centered"
)

# Header Aplikasi
st.title("🧠 Sistem Deteksi Dini Kesehatan Mental Mahasiswa")
st.markdown("""
Aplikasi berbasis *Cloud Computing* ini dikembangkan untuk mendeteksi tingkat stres dan kesehatan mental mahasiswa berdasarkan kuesioner kebiasaan harian dan akademik. 
Silakan isi parameter di bawah ini dengan jujur.
""")

st.markdown("---")

# Form Kuesioner Input Pengguna
st.subheader("📋 Kuesioner Penilaian Mandiri")

with st.form("mental_health_form"):
    # Fitur 1: Jam Tidur
    jam_tidur = st.slider(
        "1. Rata-rata waktu tidur Anda per malam (dalam jam):", 
        min_value=2, max_value=10, value=6
    )
    
    # Fitur 2: Tingkat Beban Akademik/Tugas
    beban_akademik = st.selectbox(
        "2. Bagaimana Anda menilai beban tugas/kuliah saat ini?", 
        ["Ringan", "Sedang", "Berat", "Sangat Berat"]
    )
    
    # Fitur 3: Frekuensi Kecemasan / Overthinking
    tingkat_kecemasan = st.slider(
        "3. Seberapa sering Anda merasa cemas atau *overthinking* terkait kuliah (Skala 1 - 10):", 
        min_value=1, max_value=10, value=5
    )
    
    # Fitur 4: Dukungan Sosial / Teman
    dukungan_sosial = st.selectbox(
        "4. Apakah Anda memiliki tempat bercerita/dukungan sosial yang baik?", 
        ["Ya, Sangat Baik", "Cukup", "Kurang / Jarang", "Tidak Ada"]
    )
    
    # Tombol Submit Form
    submit_button = st.form_submit_button(label="🔍 Analisis Tingkat Stres")

# Logika Prediksi (Simulasi Model Machine Learning / Rule-based Classification)
if submit_button:
    st.markdown("---")
    st.subheader("📊 Hasil Analisis Kesehatan Mental")
    
    # Bobot penilaian sederhana untuk simulasi model
    skor_risiko = 0
    
    if jam_tidur < 5:
        skor_risiko += 3
    elif jam_tidur < 6:
        skor_risiko += 2
        
    if beban_akademik in ["Berat", "Sangat Berat"]:
        skor_risiko += 3
    elif beban_akademik == "Sedang":
        skor_risiko += 1
        
    if tingkat_kecemasan >= 7:
        skor_risiko += 3
    elif tingkat_kecemasan >= 4:
        skor_risiko += 1
        
    if dukungan_sosial in ["Kurang / Jarang", "Tidak Ada"]:
        skor_risiko += 2

    # Menentukan hasil klasifikasi berdasarkan skor
    if skor_risiko >= 7:
        st.error("⚠️ **Hasil Klasifikasi: RISIKO STRES TINGGI**")
        st.write("""
        * **Analisis:** Anda menunjukkan indikasi tingkat stres yang cukup tinggi berdasarkan pola tidur, beban akademik, dan tingkat kecemasan.
        * **Saran:** Disarankan untuk meluangkan waktu beristirahat (*restarting*), melakukan relaksasi, dan jangan ragu untuk berkonsultasi dengan layanan konseling kampus atau profesional.
        """)
    elif skor_risiko >= 4:
        st.warning("⚠️ **Hasil Klasifikasi: RISIKO STRES SEDANG**")
        st.write("""
        * **Analisis:** Anda berada dalam kondisi stres tingkat moderat. Beban yang Anda hadapi mulai memengaruhi keseimbangan harian Anda.
        * **Saran:** Atur kembali manajemen waktu belajar, jaga pola tidur, dan perbanyak aktivitas fisik atau komunikasi dengan teman sebaya.
        """)
    else:
        st.success("✅ **Hasil Klasifikasi: KONDISI MENTAL STABIL / RISIKO RENDAH**")
        st.write("""
        * **Analisis:** Kondisi kesehatan mental dan tingkat stres Anda terpantau dalam batas aman dan stabil.
        * **Saran:** Pertahankan pola hidup sehat, manajemen waktu yang baik, dan tetap jaga keseimbangan antara akademik dan istirahat!
        """)

# Footer / Informasi tambahan untuk laporan tugas besar
st.markdown("---")
st.caption("© 2026 | Tugas Besar Cloud Computing - Program Studi Sistem Informasi Universitas Sari Mulia")
