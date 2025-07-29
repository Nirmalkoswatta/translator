import streamlit as st
from PIL import Image
import io
from datetime import datetime

# Configure page settings for mobile-friendly design
st.set_page_config(
    page_title="KOSA Translator", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/kosa-dev',
        'Report a bug': "https://github.com/kosa-dev",
        'About': "# Document & Image Translator\nCreated by **KOSA**\nTranslate documents and images to Sinhala and English"
    }
)

# Custom CSS for mobile-friendly and attractive design
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }
    
    .stTitle {
        color: #1e3d59;
        text-align: center;
        font-size: 2.5rem !important;
        margin-bottom: 2rem;
    }
    
    .creator-badge {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .translation-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #667eea;
    }
    
    .sinhala-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #ff6b6b;
    }
    
    .english-box {
        background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #4ecdc4;
    }
    
    .upload-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        color: white;
    }
    
    @media (max-width: 768px) {
        .stTitle {
            font-size: 1.8rem !important;
        }
        
        .creator-badge {
            position: relative;
            bottom: auto;
            right: auto;
            margin: 10px auto;
            display: block;
            text-align: center;
            width: fit-content;
        }
    }
</style>
""", unsafe_allow_html=True)

# Creator badge
st.markdown('<div class="creator-badge">Created by KOSA</div>', unsafe_allow_html=True)

# Title with emoji
st.markdown('<h1 class="stTitle">🌍 KOSA Document & Image Translator</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666; font-size: 1.2rem;">Translate documents and images to Sinhala and English</p>', unsafe_allow_html=True)

# Note about setup
st.info("🚀 **Demo Version**: This is a basic version. To use full OCR and translation features, please install the additional packages mentioned in the README.")

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    st.subheader("About")
    st.info("🚀 **KOSA Translator**\n\nUpload images or PDFs to extract and translate text to Sinhala and English.\n\n**Features:**\n- Image preview\n- PDF support (when PyMuPDF is installed)\n- OCR functionality (when EasyOCR is installed)\n- Translation (when googletrans is installed)\n- PDF export\n- Mobile-friendly design")

# Upload section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown("### 📁 Upload Your Document")
uploaded_file = st.file_uploader(
    "Choose an image or PDF file",
    type=["jpg", "jpeg", "png", "pdf", "webp", "bmp", "tiff"],
    help="Supported formats: JPG, PNG, PDF, WebP, BMP, TIFF"
)
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    file_type = uploaded_file.type
    
    # Create columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Uploaded File")
        
        # File info
        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**File size:** {uploaded_file.size / 1024:.1f} KB")
        st.write(f"**File type:** {file_type}")
    
    # Display image if it's an image file
    if file_type != "application/pdf":
        with col2:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)
                st.success("✅ Image loaded successfully!")
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")
    
    # Placeholder for OCR and translation
    st.markdown('<div class="translation-box">', unsafe_allow_html=True)
    st.subheader("📝 Text Extraction & Translation")
    st.write("**To enable full functionality:**")
    st.write("1. Install EasyOCR: `pip install easyocr`")
    st.write("2. Install Google Translate: `pip install googletrans==4.0.0-rc1`")
    st.write("3. Install PyMuPDF for PDF support: `pip install PyMuPDF`")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo text input for testing UI
    st.subheader("🧪 Test Translation Interface")
    demo_text = st.text_area("Enter text to see the translation interface:", value="Hello, this is a demo text.")
    
    if demo_text and st.button("🔄 Preview Translation UI"):
        # Demo translations
        st.markdown('<div class="sinhala-box">', unsafe_allow_html=True)
        st.subheader("🇱🇰 Sinhala Translation (Demo):")
        st.write("හෙලෝ, මෙය නිරූපණ පාඨයකි.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="english-box">', unsafe_allow_html=True)
        st.subheader("🇺🇸 English Translation (Demo):")
        st.write(demo_text)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Download section
        st.markdown("---")
        st.subheader("💾 Download Options")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Download as TXT
            result_text = f"""KOSA Document Translator - Translation Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Original Text:
{demo_text}

Sinhala Translation:
හෙලෝ, මෙය නිරූපණ පාඨයකි.

English Translation:
{demo_text}

---
Generated by KOSA Translator (Demo Version)
"""
            st.download_button(
                "📄 Download TXT",
                result_text,
                file_name=f"demo_translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        with col2:
            st.info("📑 PDF download available when ReportLab is fully configured")
        
        with col3:
            if st.button("🗑️ Clear Demo"):
                st.experimental_rerun()

# Installation instructions
st.markdown("---")
st.subheader("📦 Complete Installation")

st.write("**To get the full translator functionality, run these commands:**")

st.code("""
# Install OCR and translation packages
pip install easyocr googletrans==4.0.0-rc1 PyMuPDF

# For better performance (optional)
pip install torch torchvision
""", language="bash")

st.write("**Or use the batch installation script:**")
st.code("install.bat", language="batch")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <h4>🚀 KOSA Document & Image Translator</h4>
    <p>Powered by Streamlit with OCR and Translation capabilities</p>
    <p><strong>Created with ❤️ by KOSA</strong></p>
    <p>Ready to run! Install additional packages for full functionality.</p>
</div>
""", unsafe_allow_html=True)
