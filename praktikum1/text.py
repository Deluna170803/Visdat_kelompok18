import streamlit as st

st.write("Hello")
st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
#text element
st.write('world!!!')
st.title("This is our title")
st.header("This is our header")
st.subheader("This is our Sub-header")
st.caption("This is our caption")

st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Plain Text")
#Displaying Plain Text
st.text("Hi, \npeople\t!!!!!!!!!")
st.text('welcome to')
st.text("""streamlit's world""")

st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Markdown")
#Displaying Markdown
st.markdown("# Hi, \npeople\t!!!!!!!!!")
st.markdown('## welcome to')
st.markdown("""### streamlit's world""")

st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Rumus")
#Displaying Latex
st.latex(r'''cos2\theta =1 -2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t} 
=h^2 \left( \frac{\partial^2 u}{\partial x^2} 
+ \frac{\partial^2 u}{\partial y^2}
         + \frac{\partial^2 u}{\partial z^2} \right)''')

st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Kode Python")
#Displaying python code
st.subheader("""Python Code""")
code = '''def hello():
print("Hello, Streamlit!)'''
st.code(code, language='python')

st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Kode Java")
#Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
public static void main(String args[])
{
System.out.println("Hello world");
}
}""", language='javascript')
st.code(code, language='python')
st.subheader("""Javascript code""")
st.code(""" <p id="demo"></p>
<script>
try {
addlert("welocme guest!");
}
catch(err) {
document.getElementById("demo).innerHTML = err.message;
}
</script> """)