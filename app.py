import streamlit as st
import google.generativeai as genai
import random

# Configure Google Gemini API
API_KEY = "AIzaSyDuEIsoGUODV3QUicBKgGSH4W_qFnUVlPA"
genai.configure(api_key=API_KEY)

# Function to fetch jokes
def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the JavaScript developer sad? Because he didn’t ‘null’ his feelings.",
        "How many programmers does it take to change a light bulb? None, that’s a hardware problem!"
    ]
    return random.choice(jokes)

# Function to generate recipes using AI
def generate_recipe(topic, word_count):
    try:
        st.info(f"👨‍🍳 Generating your recipe for '{topic}'... 🍽")
        st.write(f"🤖 Meanwhile, here's a joke for you: {get_joke()}")

        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Write a detailed recipe blog about {topic} with {word_count} words."

        response = model.generate_content(prompt)

        return response.text if response.text else "⚠ No content generated."
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("🍲 Flavour Fusion: AI-Driven Recipe Blogging 🚀")
st.write("Create unique, AI-generated recipes and food blogs instantly!")

# User Input Fields
recipe_topic = st.text_input("Enter Recipe Topic (e.g., Vegan Pasta, Spicy Tacos):")
word_count = st.slider("Select Word Count", 100, 2000, step=100)

# Generate Recipe Button
if st.button("Generate Recipe"):
    if recipe_topic:
        recipe_text = generate_recipe(recipe_topic, word_count)
        st.markdown("### 🍽 Your AI-Generated Recipe:")
        st.text_area("Recipe Output", recipe_text, height=300)

        # Option to download the generated recipe
        st.download_button(
            label="📥 Download Recipe",
            data=recipe_text,
            file_name=f"{recipe_topic.replace(' ', '_')}.txt",
            mime="text/plain",
        )
    else:
        st.warning("⚠ Please enter a recipe topic.")
