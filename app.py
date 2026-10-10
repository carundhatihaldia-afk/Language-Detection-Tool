
import streamlit as st
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0

LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "bn": "Bengali",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese (Simplified)",
    "ru": "Russian",
    "ar": "Arabic",
    "ur": "Urdu",
    "ta": "Tamil",
    "te": "Telugu",
    "mr": "Marathi",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "nl": "Dutch",
    "hr": "Croatian",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "id": "Indonesian",
    "pl": "Polish",
    "ro": "Romanian",
    "sv": "Swedish",
    "el": "Greek",
    "he": "Hebrew"
}

st.set_page_config(
    page_title="Language Detection Tool",
    page_icon="🌍",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f0fff4, #f4f0ff);
}
h1 {
    color: #176b4d;
}
.stButton > button {
    background-color: #16845b;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: bold;
}
.stButton > button:hover {
    background-color: #106b48;
    color: white;
}
.result-card {
    background: white;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #d8eadf;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Language Detection Tool")
st.write(
    "Enter a sentence or paragraph and discover "
    "which language it is written in."
)

st.info(
    "Free Python language detection. "
    "No API key required."
)

text = st.text_area(
    "Enter your text",
    placeholder="Example: Hello, how are you today?",
    height=160
)

if st.button("🔎 Detect Language", use_container_width=True):
    cleaned_text = text.strip()

    if not cleaned_text:
        st.warning("Please enter some text first.")

    elif len(cleaned_text.split()) < 3:
        st.warning(
            "Please enter at least 3 words for better "
            "accuracy. Very short text may be misclassified."
        )

    else:
        try:
            code = detect(cleaned_text)
            language = LANGUAGES.get(
                code, f"Other language ({code})"
            )

            st.markdown("---")
            st.subheader("Detection Result")

            st.success(f"Detected Language: {language}")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Language Code", code)
            with col2:
                st.metric("Words Analyzed", len(cleaned_text.split()))

            st.caption(
                "Results are statistical estimates and may not "
                "always be correct. No translation is performed."
            )

        except LangDetectException:
            st.error(
                "Unable to detect the language. "
                "Please try a longer text."
            )

st.markdown("---")
st.caption("Language Detection Tool | Python Mini-Project")
