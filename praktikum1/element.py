import streamlit as st
import pandas as pd
import numpy as np
st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("DataFrame")
#DATAFRAME
#defining random balues in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(30,10),
columns=('col_no %d' % i for i in range (10)
))

#Defining random balues in a dataframe using pandas and numpy

df = pd.DataFrame(
np.random.randn(30,10),
columns=('col_no %d' % i for i in range (10)
))

#highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

#TABLE
st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Table")
#defining random values in a dataframe using pandas and numpy
df =pd.DataFrame(
np.random.randn(30,10),
columns=('col_no %d' % i for i in range (10)
))
#defining data in table
st.table(df)

#metrics
st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Metrics")
# Defining Metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

# Defining Multiple Columns for Metrics
c1, c2, c3 = st.columns(3)

# Menampilkan beberapa metric di kolom
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric("Population", "123 Billions", "1 Billions", delta_color="inverse")
c3.metric("Customers", value=100, delta=10, delta_color="off")
st.metric("Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

#THE write() FUNCTION AS A SUPERFUNCTION
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col %d' % i for i in range(10))
)

# Menampilkan teks dan dataframe dengan write()
st.write("Here is our Data:", df, "Data is in dataframe format.\n", "Write is Super Function")

#importing necessary libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# defining random values for chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)

# Membuat chart menggunakan Altair
chart = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b',
    tooltip=['a', 'b']
)

# Menampilkan chart dengan write()
st.write(chart)

# =========================================================
# BAGIAN 5: MAGIC
# =========================================================
# Magic memungkinkan menulis teks atau hasil perhitungan tanpa st.write()

# ---------------------------------------------
# Operasi matematika tanpa fungsi
# ---------------------------------------------
"Adding 5 & 4 =", 5+4

# Menampilkan variabel secara otomatis
a = 5
'a:' ,  a

# ---------------------------------------------
# Markdown dengan Magic
# ---------------------------------------------
"""
### Magic Feature
Markdown working without defining its function explicitly.
"""

# ---------------------------------------------
# DataFrame menggunakan Magic
# ---------------------------------------------
import pandas as pd
df = pd.DataFrame({'col': [1, 2]})
'dataframe:', df

#magic working on charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax= plt.subplots()
ax.hist(s, bins=15)
#magic charts
"chart", chart
