
from langdetect import detect, DetectorFactory, LangDetectException

# Make detection more consistent
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
    "zh-tw": "Chinese (Traditional)",
    "ru": "Russian",
    "ar": "Arabic",
    "ur": "Urdu",
    "ta": "Tamil",
    "te": "Telugu",
    "mr": "Marathi",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "hr": "Croatian",
    "nl": "Dutch",
    "pl": "Polish",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "th": "Thai",
    "el": "Greek",
    "sv": "Swedish",
    "da": "Danish",
    "fi": "Finnish",
    "no": "Norwegian",
    "he": "Hebrew",
    "id": "Indonesian",
    "ro": "Romanian",
    "cs": "Czech",
    "hu": "Hungarian"
}


def detect_language(text):
    text = text.strip()

    # Check for empty input
    if not text:
        return "Please enter some text."

    # Require at least 3 words for more reliable detection
    if len(text.split()) < 3:
        return (
            "Please enter at least 3 words "
            "for better language detection accuracy."
        )

    try:
        language_code = detect(text)
        language_name = LANGUAGES.get(
            language_code,
            f"Other language (code: {language_code})"
        )

        return (
            "\n--- Detection Result ---\n"
            f"Detected Language: {language_name}\n"
            f"Language Code: {language_code}\n"
            "------------------------"
        )

    except LangDetectException:
        return (
            "Unable to detect the language. "
            "Please enter a longer text."
        )


def main():
    print("=" * 40)
    print("      LANGUAGE DETECTION TOOL")
    print("=" * 40)
    print("Enter a sentence to identify its language.")
    print("Type 'exit' to close the program.")

    while True:
        try:
            text = input("\nEnter text: ")

            if text.strip().lower() == "exit":
                print("\nThank you for using the tool!")
                break

            result = detect_language(text)
            print(result)

        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram closed. Goodbye!")
            break


if __name__ == "__main__":
    main()
