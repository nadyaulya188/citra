import streamlit as st
import base64

# ===== Fungsi menghitung normalitas =====
def hitung_normalitas(massa, berat_ekivalen, volume_ml):
    if berat_ekivalen <= 0 or volume_ml <= 0:
        return None
    return (massa / berat_ekivalen) / (volume_ml / 1000)

# ===== Tambahkan background dari file atau URL =====
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        img_bytes = img_file.read()
    encoded = base64.b64encode(img_bytes).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ===== Program utama =====
def main():
    set_background("bg.jpg")  # Ganti dengan nama file gambar latar kamu

    st.title("🔬 Kalkulator Normalitas Larutan")

    st.markdown("Masukkan data untuk menghitung normalitas (N):")

    massa = st.number_input("Massa zat (gram)", min_value=0.0, format="%.4f")
    berat_ekivalen = st.number_input("Berat ekivalen (g/ek)", min_value=0.0, format="%.4f")
    volume = st.number_input("Volume larutan (mL)", min_value=0.0, format="%.2f")

    if st.button("Hitung Normalitas"):
        normalitas = hitung_normalitas(massa, berat_ekivalen, volume)
        if normalitas is not None:
            st.success(f"✅ Normalitas larutan: {normalitas:.4f} N")
        else:
            st.error("❌ Berat ekivalen dan volume harus lebih dari 0.")

    st.markdown("---")
    st.info("Created with ❤️ using Streamlit by [Nama Kamu]")

if __name__ == "__main__":
    main()
