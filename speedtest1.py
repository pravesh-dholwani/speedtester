import pyspeedtest
import speedtest
import streamlit as st


if st.button("Start Test"):
    spt = speedtest.Speedtest()
    for i in range(5000):
        download1 = spt.download() // 1000000
        download2 = spt.download() // 1000000
        download3 = spt.download() // 1000000
        download4 = spt.download() // 1000000
        # upload = spt.upload(threads=3) // 1000000

        st.text(f"Download - {download1} {download2} {download3} {download4}")
        # st.text(f"Upload - {upload}")


