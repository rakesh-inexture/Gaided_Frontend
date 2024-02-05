
import streamlit as st
import requests
import json

# Define the FastAPI web app URL
BACKEND_URL = "http://localhost:8000"

# Streamlit app title and description
st.title("Gaided Backend Testing App")
st.write("Enter Point of Interest (POI) and City to test Backend web app of Gaided.")

# User input for POI and City
poi = st.text_input("Enter Point of Interest (POI):")
city = st.text_input("Enter City:")

# Button to trigger API request
if st.button("Generate"):
    #Making request for API 
    api_url = f"{BACKEND_URL}/api/manual-fact/generate-fact"
    params = {"poi": poi, "city": city}
    response = requests.post(api_url, json=params)

    # Display API response
    if response.status_code == 200:
        result = response.json()
        st.success("API Response:")
        st.json(result)

        # st.success(f"API Response: {json.dumps(result, indent=2)}")
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
