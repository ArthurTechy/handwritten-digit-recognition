# Handwritten Digit Recognition Web App

## Overview

This Streamlit-based web application uses a trained neural network to recognize and classify handwritten digits. Users can upload images of handwritten digits, and the app will predict the digit and provide confidence scores for each possible digit (0-9).

## Features

- Image upload functionality (supports PNG, JPG, and JPEG formats)
- Digit prediction with confidence score
- Visualization of probability distribution for all digits
- Display of preprocessed image as seen by the model
- Informative sidebar with app description and usage instructions

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/handwritten-digit-recognition.git
   cd handwritten-digit-recognition
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload an image of a handwritten digit using the file uploader.

4. View the prediction, confidence score, probability distribution, and preprocessed image.

## Dependencies

- streamlit==1.39.0
- tensorflow-cpu==2.16.2
- numpy==1.26.0
- Pillow==10.4.0
- matplotlib==3.7.1

## Model

The app uses a pre-trained neural network model (`mnist_model.h5`) that was trained on the MNIST dataset of handwritten digits.
#### -the model was trained using:
- python==3.10.11 (installed globally
- tensorflow-cpu==2.13.0
- numpy==1.24.3

## File Structure

- `app.py`: Main Streamlit application
- `mnist_model.h5`: Pre-trained neural network model
- `requirements.txt`: List of required Python packages

## How It Works

1. The user uploads an image of a handwritten digit.
2. The image is preprocessed:
   - Converted to grayscale
   - Resized to 28x28 pixels
   - Normalized to values between 0 and 1
   - Takes the normalized single image, flatten it, with single color in consideration (grey)
   - Invert the image to white digits on black background, in sychronous to mnist dataset used to train the model
     
3. The preprocessed image is fed into the neural network model.
4. The model predicts the digit and provides confidence scores for each possible digit.
5. Results are displayed, including:
   - Original uploaded image
   - Predicted digit and confidence score
   - Probability distribution chart for all digits
   - Preprocessed image as seen by the model

## Future Improvements

- Implement drawing functionality to allow users to draw digits directly in the browser
- Add support for recognizing multiple digits in a single image
- Improve model accuracy with more advanced architectures or additional training data

## Contributing

Contributions to improve the Handwritten Digit Recognition Web App are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

Please ensure your code adheres to the project's coding standards and include tests for new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or feedback about this project, please open an issue in the GitHub repository.
