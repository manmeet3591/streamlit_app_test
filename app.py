import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("2D Random Number Array Visualization")

# Slider to select the size of the array
size = st.slider("Select the size of the array", 10, 100)

# Generate a 2D random number array
data = np.random.rand(size, size)

# Display the array as a heatmap
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')
plt.colorbar(cax)
st.pyplot(fig)
