import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")

st.markdown("### Mathematical Formula")
st.latex(r"f(x) = \frac{1}{1 + e^{-x}}")

x = np.linspace(-10, 10, 100)
sigmoid = 1 / (1 + np.exp(-x))

st.markdown("### Visualization")
plt.figure()
plt.plot(x, sigmoid)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Sigmoid Function")

st.pyplot(plt)
