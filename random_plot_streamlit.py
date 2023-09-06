import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('Random Number Plotter')

num_points = st.slider('Number of points:', min_value=1, max_value=1000, value=100)

# Generate random numbers
x = np.linspace(0, 10, num_points)
y = np.random.randn(num_points)

# Create plot
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('Scatter plot of random numbers')
ax.set_xlabel('x')
ax.set_ylabel('Random Number')

# Show plot
st.pyplot(fig)
