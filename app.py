import streamlit as st

# Fungsi untuk menghitung normalitas
def hitung_normalitas(gram_zat, berat_ekuivalen, volume_larutan):
    try:
        normalitas = (gram_zat / berat_ekuivalen) / (volume_larutan / 1000)
        return normalitas
    except ZeroDivisionError:
        return None

# Mengatur halaman
st.set_page_config(
    page_title="Kalkulator Normalitas",
    page_icon="🧪",
    layout="centered"
)

# Tambahkan CSS untuk background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1581091012184-5c9c0c203f33");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title("🧪 Kalkulator Normalitas Larutan")

st.markdown("Hitung normalitas larutan dengan memasukkan massa zat, berat ekuivalen, dan volume larutan.")

# Input pengguna
gram_zat = st.number_input("Massa zat (gram)", min_value=0.0, format="%.4f")
berat_ekuivalen = st.number_input("Berat ekuivalen (g/eq)", min_value=0.0001, format="%.4f")
volume_larutan = st.number_input("Volume larutan (mL)", min_value=0.0001, format="%.2f")

# Tombol hitung
if st.button("Hitung Normalitas"):
    normalitas = hitung_normalitas(gram_zat, berat_ekuivalen, volume_larutan)
    if normalitas is not None:
        st.success(f"Normalitas larutan adalah **{normalitas:.4f} N**")
    else:
        st.error("Kesalahan: Pembagian dengan nol!")

# Catatan tambahan
st.markdown("""
**Catatan**:
- Berat ekuivalen tergantung pada jenis reaksi dan zat (misalnya H₂SO₄ = 49 untuk 2H⁺).
- Volume harus dalam mililiter (mL).
""")

