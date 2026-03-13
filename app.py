#uploading in the streamlit 

import streamlit as st
import joblib
import pandas as pd

model = joblib.load("Mobile_Prices.joblib")

df = pd.read_csv("Flipkart_Mobiles.csv")

st.title("Mobile Prices Prediction")

brand = st.selectbox("Select Brand", df["Brand"].unique())

df_brand = df[df["Brand"] == brand]                                         #condition for brand

mobile_model = st.selectbox("Select Model", df_brand["Model"].unique())

df_model = df_brand[df_brand["Model"] == mobile_model]                      #condition for model

color = st.selectbox("Select Color", df_model["Color"].unique())

df_color = df_model[df_model["Color"] == color]                             #condition for color

memory = st.selectbox("Select Memory", df_color["Memory"].unique())

df_memory = df_color[df_color["Memory"] == memory]                          #condition for memory

storage = st.selectbox("Select Storage", df_memory["Storage"].unique())

rating = st.selectbox("Select Rating", df["Rating"].unique())

if st.button("Check Price"):

    input_df = pd.DataFrame({
        "Brand":[brand],
        "Model":[mobile_model],
        "Color":[color],
        "Memory":[memory],
        "Storage":[storage],
        "Rating":[rating]
    })

    prediction = model.predict(input_df)

    st.success(f"Final Price is: ₹{prediction[0]}")








# import streamlit as st
# import joblib
# import pandas as pd

# model = joblib.load("Mobile_Prices.joblib")

# df = pd.read_csv("Flipkart_Mobiles.csv")

# st.title("Mobile Prices Prediction")

# brand = st.selectbox("Select Brand", df["Brand"].unique())

# mobile_model = st.selectbox("Select Model", df["Model"].unique())

# color = st.selectbox("Select Color", df["Color"].unique())

# memory = st.selectbox("Select Memory", df["Memory"].unique())

# storage = st.selectbox("Select Storage", df["Storage"].unique())

# rating = st.selectbox("Select Rating", df["Rating"].unique())

# if st.button("Check Price"):

#     input_df = pd.DataFrame({
#         "Brand":[brand],
#         "Model":[mobile_model],
#         "Color":[color],
#         "Memory":[memory],
#         "Storage":[storage],
#         "Rating":[rating]
#     })

#     prediction = model.predict(input_df)

#     st.success(f"Final Price is: ₹{prediction[0]}")