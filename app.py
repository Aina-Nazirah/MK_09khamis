import streamlit as st

st.title("Kalkulator BMI Klinik")

berat_input = st.text_input("Masukkan Berat (kg):")
tinggi_input = st.text_input("Masukkan Tinggi (meter):")

if st.button("Kira BMI"):
    try:
        berat = float(berat_input)
        tinggi = float(tinggi_input)

        if tinggi == 0:
            raise ZeroDivisionError
 
        if tinggi > 3.0:
            st.error("Ralat: Sila masukkan tinggi dalam meter (contoh: 1.47 dan bukannya 147).")
        else:
            bmi = berat / (tinggi * tinggi)

    except ValueError:
        st.error("Ralat: Sila masukkan nombor sahaja untuk berat dan tinggi!")
    except ZeroDivisionError:
        st.error("Ralat: Tinggi tidak boleh bernilai 0.0!")
    except Exception as e:
        st.error(f"Ralat tidak dijangka berlaku: {e}")
    else:
        if tinggi <= 3.0:
            st.success(f"Pengiraan Berjaya! Nilai BMI anda ialah: {bmi:.2f}")
    finally:
        st.info("Sistem selesai memproses permintaan anda.")

st.divider()

if st.button("Papar Rekod Lama"):
    try:
        with open("rekod_pesakit.txt", "r") as f:
            kandungan = f.read()
            st.write(kandungan)
    except FileNotFoundError:
        st.warning("Fail rekod belum diwujudkan.")