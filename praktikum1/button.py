import streamlit as st
st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Button and Slide")

# =========================================================
# BAGIAN 6: BUTTONS DAN SLIDERS
# =========================================================
import streamlit as st

# ---------------------------------------------
# Membuat Button
# ---------------------------------------------
st.title('Creating a Button')

# Defining a Button
button = st.button('Click Here')

if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

# =========================================================
# BAGIAN 7: RADIO BUTTONS
# =========================================================
import streamlit as st

st.title('Creating Radio Buttons')

# Defining Radio Button
gender = st.radio(
    'Select your Gender:',
    ('Male', 'Female', 'Others')
)

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write('You have selected Female.')
else:
    st.write('You have selected Others.')

# =========================================================
# BAGIAN 8: CHECK BOXES
# =========================================================
import streamlit as st

st.title('Creating Checkboxes')
st.write('Select your Hobbies:')

# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Menampilkan hasil pilihan
if check_1:
    st.write("You like Books!")
if check_2:
    st.write("You like Movies!")
if check_3:
    st.write("You like Sports!")

# =========================================================
# BAGIAN 9: DROP-DOWNS (SELECTBOX)
# =========================================================
import streamlit as st

st.title('Creating Dropdown')

# Creating Dropdown
hobby = st.selectbox(
    'Choose your hobby:',
    ('Books', 'Movies', 'Sports')
)

st.write('Your selected hobby is:', hobby)

# =========================================================
# BAGIAN 10: MULTISELECTS
# =========================================================
import streamlit as st

st.title('Multi-Select')

# Defining Multi-Select with Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']  # default pre-selected options
)

# Menampilkan hasil pilihan
st.write("Your selected hobbies are:", hobbies)

# =========================================================
# BAGIAN 11: DOWNLOAD BUTTONS
# =========================================================
import streamlit as st

st.title('Download Button')

# Membuat tombol untuk mengunduh file gambar
down_btn = st.download_button(
    label="Download Image",
    data=open("../assets/panda.jpg", "rb"),
    file_name="../assets/panda.jpg",
    mime="image/jpg"
)

# Contoh tombol untuk mengunduh file CSV
st.download_button(
    label="Download CSV",
    data=open("../assets/animal.csv", "rb"),
    file_name="animal.csv",
    mime='csv',
)

# =========================================================
# BAGIAN 12: PROGRESS BARS
# =========================================================
import streamlit as st
import time

st.title('Progress Bar')

# Defining Progress Bar
download = st.progress(0)

for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)

st.write("Download Complete")

# =========================================================
# BAGIAN 13: SPINNERS
# =========================================================
import streamlit as st
import time

st.title('Spinner')

# ---------------------------------------------
# Defining Spinner
# ---------------------------------------------
with st.spinner('Loading...'):
    time.sleep(5)

st.write('Hello Data Scientists')