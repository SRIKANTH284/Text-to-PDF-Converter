import streamlit as st
from fpdf import FPDF
import base64

report_text = st.text_input("Report Text")

export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, report_text)
    
    pdf_output = pdf.output(dest="S").encode("latin-1")
    html = create_download_link(pdf_output, "test")

    st.markdown(html, unsafe_allow_html=True)
    st.success("Here you go!")  # Display success message
    st.balloons()  # Trigger balloons
