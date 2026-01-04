import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
    page_title="ReLU Activation Function",
    layout="centered"
)

st.title("Rectified Linear Unit (ReLU)")
st.write("This web application visualises the ReLU activation function.")


st.sidebar.header("Input Settings")
x_min = st.sidebar.slider("Minimum x value", -20.0, -1.0, -10.0)
x_max = st.sidebar.slider("Maximum x value", 1.0, 20.0, 10.0)
num_points = st.sidebar.slider("Number of points", 100, 1000, 400, step=50)


x = np.linspace(x_min, x_max, num_points)
y = np.maximum(0, x)

st.write("**Formula:** ReLU(x) = max(0, x)")
st.write(
    "**X-axis:** Input value to the neuron\n"
    "**Y-axis:** Output after applying the ReLU activation function"
)


df = pd.DataFrame({"Input (x)": x, "ReLU Output": y})
st.line_chart(df.set_index("Input (x)"))
