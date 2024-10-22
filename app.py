import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt

# Load the saved model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('mnist_model.h5')

model = load_model()

st.title('Handwritten Digit Recognition')

# Add file uploader for PNG and JPEG
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    image = image.resize((28, 28))
    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    # Invert the image to white digits on black background
    img_array = 1 - img_array

    # Make prediction
    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)

    # Display results
    st.write(f"Prediction: {predicted_digit}")
    st.write(f"Confidence: {prediction[0][predicted_digit]:.2f}")

    # Create and display probability distribution chart
    fig, ax = plt.subplots()
    ax.bar(range(10), prediction[0])
    ax.set_xticks(range(10))
    ax.set_xlabel('Digit')
    ax.set_ylabel('Probability')
    ax.set_title('Probability Distribution')
    st.pyplot(fig)

    # Display preprocessed image
    st.write("Preprocessed Image:")
    st.image(img_array.reshape(28, 28), caption='Preprocessed Image', use_column_width=True)

# Add information about the model
st.sidebar.title("About")
st.sidebar.info("This app uses a neural network trained on the MNIST dataset to recognize handwritten digits.")

# Add instructions
st.sidebar.title("Instructions")
st.sidebar.write("1. Upload a PNG or JPG/JPEG image of a handwritten digit.")
st.sidebar.write("2. The app will display the original image, the prediction, and a probability distribution.")
st.sidebar.write("3. The preprocessed image shows how the digit appears to the model.")

# Footer
st.write('')
st.write('')
st.write('')
st.write('')
st.markdown("---")
st.markdown("Created by Arthur_Techy")