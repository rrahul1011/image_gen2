import streamlit as st
import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
#API_URL = "https://api-inference.huggingface.co/models/minimaxir/sdxl-wrong-lora"

def main():
    st.sidebar.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    st.sidebar.image("/Users/rahulkushwaha/Desktop/Image gen/image_gen/code/cropped-Sigmoid_logo_3x.png", use_column_width=True)
    st.sidebar.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    api_key = st.sidebar.text_input("Enter Your API key", type="password")
    
    # Submit button to check the API key
    if st.sidebar.button("Submit"):
        if api_key:
            st.sidebar.success("API Detected")
        else:
            st.sidebar.warning("Please enter your API key")
    API_TOKEN = api_key
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    st.sidebar.markdown(
        "## ImageGenie App\n\n"
        "Welcome to ImageGenie, where you can generate vibrant images based on textual descriptions."
        "\n\n"
        "### How to Use?\n\n"
        "1. Enter a description in the text area on the left.""\n\n"
        "2. Click the 'Generate Image' button to see the generated image.""\n\n"
        "3. After generating, you can download the image using the 'Download Image' button below."
        "\n\n"
        "### Limitations\n\n"
        "Please note the following limitations:\n"
        "- The quality of generated images depends on the input description.""\n\n"
        "- Complex or highly specific descriptions may not yield accurate results."
        "\n\n"
        "Feel free to experiment and have fun!"
    )
    st.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center;'>"
        "<h2 style='color: #3366FF;'>🎨 Welcome! I am the ImageGenie! 🧞‍♂️</h2>"
        "<p style='color: #FF5733;'>I generate vibrant images based on your textual descriptions.</p>"
        "</div>",
        unsafe_allow_html=True
    )
    
    st.markdown("<p style='color: #3366FF; font-size: 18px; text-align: center;'>Ask & Visualize 🖼️</p>", unsafe_allow_html=True)
    
    # Apply CSS to style the horizontal lines
    st.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    
    user_input = st.text_area("Enter a Description", "")

    if st.button("Generate Image"):
        if user_input:
            st.info("Generating image...")
            payload = {
                "inputs": user_input,
            }
            image_bytes = query(payload)
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
            st.success("Image generated successfully!")
            st.download_button("Download Image", image_bytes, file_name="generated_image.png")
        else:
            st.warning("Please enter a text prompt.")

if __name__ == "__main__":
    main()
