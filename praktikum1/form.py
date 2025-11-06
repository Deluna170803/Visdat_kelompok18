import streamlit as st
st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Form")

# =========================================================
# BAGIAN 14: FORMS - TEXT BOX
# =========================================================
import streamlit as st

st.title('Text Box')

# ---------------------------------------------
# Creating Text Box
# ---------------------------------------------
name = st.text_input("Enter your Name")
st.write("Your Name is", name)

# ---------------------------------------------
# Creating Text Box with Character Limit
# ---------------------------------------------
name = st.text_input("Enter your Name", max_chars=10)

# ---------------------------------------------
# Creating Password Input
# ---------------------------------------------
password = st.text_input("Enter your password", type='password')


# =========================================================
# BAGIAN 15: TEXT AREA
# =========================================================
import streamlit as st

st.title("Text Area")

# ---------------------------------------------
# Creating Text Area
# ---------------------------------------------
input_text = st.text_area("Enter your Review")

# ---------------------------------------------
# Printing entered text
# ---------------------------------------------
st.write("You entered:\n", input_text)

# =========================================================
# BAGIAN 16: NUMBER INPUT
# =========================================================
import streamlit as st

st.title("Number Input")

# ---------------------------------------------
# Simple Number Input
# ---------------------------------------------
st.number_input("Enter your Number")

# ---------------------------------------------
# Number Input with Range and Step
# ---------------------------------------------
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, Max. Value is 10, Default Value is 5, Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

# =========================================================
# BAGIAN 17: TIME INPUT
# =========================================================
import streamlit as st

st.title("Time")

# ---------------------------------------------
# Defining Time Input
# ---------------------------------------------
st.time_input("Select Your Time")

# =========================================================
# BAGIAN 18: DATE INPUT
# =========================================================
import streamlit as st
import datetime

st.title("Date")

# ---------------------------------------------
# Simple Date Input
# ---------------------------------------------
st.date_input("Select Date")

# ---------------------------------------------
# Date Input with Min and Max Range
# ---------------------------------------------
st.date_input(
    "Select Your Date",
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1)
)

# =========================================================
# BAGIAN 19: COLOR PICKER
# =========================================================
import streamlit as st

st.title("Select Color")

# ---------------------------------------------
# Defining Color Picker
# ---------------------------------------------
color_code = st.color_picker("Select your Color")

# Menampilkan warna yang dipilih
st.header(color_code)

# =========================================================
# BAGIAN 20: DATASET UPLOAD
# =========================================================
import streamlit as st
import pandas as pd

st.title("CSV Upload")

# ---------------------------------------------
# Defining File Uploader
# ---------------------------------------------
data_file = st.file_uploader("Upload CSV", type="csv")

st.subheader("Check Details")

# Mengecek apakah ada file yang diunggah
if data_file is not None:
    file_details = {
        "File name": data_file.name,
        "File type": data_file.type,
        "File size": data_file.size
    }
    st.write(file_details)

    # Membaca file CSV dan menampilkannya
    df = pd.read_csv(data_file)
    st.dataframe(df)
else:
    st.write("No CSV File is Uploaded")

# =========================================================
# BAGIAN 21: SUBMIT BUTTON (FORM)
# =========================================================
import streamlit as st

# ---------------------------------------------
# Membuat Form
# ---------------------------------------------
my_form = st.form(key='form')

# Membuat input teks di dalam form
a = my_form.text_input(label='Enter any text')

# Membuat tombol submit di dalam form
submit_button = my_form.form_submit_button(label='Submit')

# Menampilkan hasil input setelah submit
if submit_button:
    st.write(a)

# =========================================================
# AKHIR MODUL
# =========================================================
st.write("----- Sekian Terima Kasih -----")

