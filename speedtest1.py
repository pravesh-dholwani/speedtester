import pyspeedtest
import speedtest
import streamlit as st
import requests
import time

def download_random_image():
    url = "https://picsum.photos/200"  # URL for a random 200x200 image
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Generate a unique filename
            # filename = f"image_{int(time.time())}.jpg"
            # with open(filename, 'wb') as f:
            #     f.write(response.content)
            print(f"Downloaded ")
        else:
            print(f"Failed to download image, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if st.button("Start Test"):
    spt = speedtest.Speedtest()
    for i in range(50000):
        # download_random_image()
        download1 = spt.upload() // 1000000
        download2 = spt.upload() // 1000000
        download3 = spt.upload() // 1000000
        download4 = spt.upload() // 1000000
        # upload = spt.upload(threads=3) // 1000000

        st.text(f"Download - {download1} {download2} {download3} {download4}")
        # st.text(f"Upload - {upload}")


