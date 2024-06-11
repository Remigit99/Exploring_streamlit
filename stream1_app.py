import streamlit as st
import pandas as pd

price_table = pd.DataFrame({"Item": ["Laptop", "Phone", "Shoe", "Shirt", "TV"], "Price": [560000, 303000, 15000, 12000, 607000]})

st.title('Caesar Cipher')

# st.header("Text Encrytion And Decryption App")
# st.subheader('A simple Caesar Cipher Encryption App')
# st.text("This is a text in streamlit")
# st.markdown("**Caesar** *Cipher*")
# st.markdown("[Streamlit](https://streamlit.io/)")

# Writing JSON
# product_data = {"Name": "Nike Sneakers", "Price": "300"}
# st.json(product_data)

# st.code(
#     """""
#     print("Hello Everyone, I am learning Streamlit")
#     """""
# )
# st.code(
#     """""
#     print("Hello Everyone, I am learning Streamlit")
#     """"", language="python"
# )


#### Swiss Army Knife ###
# st.write("## Swiss Knife")
#fast unicode character - An Extension

#Using Metric
# st.metric(label ="Wind Speed", value="120ms⁻¹", delta="-0.5ms⁻¹")


### Creating Table with Streamlit

# st.table(price_table)
# st.dataframe(price_table)         ----#Sortable, downloadable table

st.image("./assets/product4.png", caption="Nike Shoe",width=96)
st.image("./assets/product5.png", caption="Nike Shoe 2",width=96)

input_txt = st.text_area('Enter text to be encrypted:')

if st.button('Submit'):
    st.write(f"Received: {input_txt}")


input_shift = st.text_input('Enter some data:')
