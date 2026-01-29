import google.generativeai as genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
client = genai.GenerativeModel(model_name="gemini-3-flash-preview")
st.title("TranscriptSummarizer")


prompt = """Summarize the transcript below using the following structure:

1. Main Topic
2. Key Points
3. Important Examples
4. Final Takeaways

Be concise, accurate, and easy to scan. """
st.markdown("""## 📄 How to Use the Video Transcript Summarizer

This tool helps you turn long video transcripts into **clear, easy-to-read summaries** using AI.

### 🧩 Steps
1. **Copy the video transcript** (from YouTube, lectures, podcasts, etc.)
2. **Remove timestamps** like `00:12`, `1:05:30`, or `[00:45]`  
   *(This improves summary quality)*
3. Paste the cleaned transcript into the text box
4. Click **Summarize**
5. Wait a few seconds and read your summary ✨

---

### ⚠️ Important Notes
- Please paste **text only** (no captions metadata or timestamps)
- Very long transcripts may take a bit longer to process
- Repeated clicks may be rate-limited

---

### ⏱️ Usage Limits
To keep the app running smoothly for everyone:
- **Max 5 summaries per minute**
- Requests beyond this may fail temporarily
- Token usage resets automatically every minute

---

### 💡 Tips for Best Results
- Shorter, cleaner transcripts = better summaries
- Educational and structured content works best
- Try summarizing in sections for very long videos

---

*This app is intended for personal and educational use.*
""")
transcript = st.text_area("ENTER YOUR TRANSCRIPT HERE")

response = client.generate_content(
    contents = prompt + transcript
)

if st.button("Enter"):
    st.markdown(response.text)

