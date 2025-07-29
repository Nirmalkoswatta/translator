import streamlit as st
from PIL import Image
import easyocr
from googletrans import Translator
import fitz  # PyMuPDF for PDF reading
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import tempfile
import os
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

# Initialize session state
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = ""
if 'sinhala_text' not in st.session_state:
    st.session_state.sinhala_text = ""
if 'english_text' not in st.session_state:
    st.session_state.english_text = ""

def create_pdf_report(original_text, sinhala_text, english_text):
    """Create a PDF report with translations"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#1e3d59',
        alignment=TA_CENTER,
        spaceAfter=30
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor='#667eea',
        spaceAfter=12
    )
    
    content = []
    
    # Title
    content.append(Paragraph("KOSA Document Translator", title_style))
    content.append(Paragraph(f"Translation Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Original text
    content.append(Paragraph("Original Text:", heading_style))
    content.append(Paragraph(original_text, styles['Normal']))
    content.append(Spacer(1, 15))
    
    # Sinhala translation
    content.append(Paragraph("Sinhala Translation:", heading_style))
    content.append(Paragraph(sinhala_text, styles['Normal']))
    content.append(Spacer(1, 15))
    
    # English translation
    content.append(Paragraph("English Translation:", heading_style))
    content.append(Paragraph(english_text, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Footer
    content.append(Paragraph("Generated by KOSA Translator", styles['Normal']))
    
    doc.build(content)
    buffer.seek(0)
    return buffer

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Language detection settings
    st.subheader("OCR Settings")
    ocr_languages = st.multiselect(
        "Select OCR Languages",
        ['en', 'si', 'ta', 'hi'],
        default=['en'],
        help="Select languages for text recognition"
    )
    
    st.subheader("Translation Settings")
    confidence_threshold = st.slider(
        "OCR Confidence Threshold",
        0.0, 1.0, 0.5,
        help="Minimum confidence for text recognition"
    )
    
    st.subheader("About")
    st.info("🚀 **KOSA Translator**\n\nUpload images or PDFs to extract and translate text to Sinhala and English.\n\n**Features:**\n- OCR for images\n- PDF text extraction\n- Multi-language translation\n- PDF export\n- Mobile-friendly design")

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
    
    extracted_text = ""
    
    # Progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # If PDF
        if file_type == "application/pdf":
            status_text.text("📖 Extracting text from PDF...")
            progress_bar.progress(25)
            
            pdf_bytes = uploaded_file.read()
            pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            
            for page_num, page in enumerate(pdf_doc):
                extracted_text += page.get_text()
                progress_bar.progress(25 + (page_num + 1) / len(pdf_doc) * 25)
            
            pdf_doc.close()
            status_text.text("✅ Text extracted from PDF successfully!")
            progress_bar.progress(50)
            
        # If Image
        else:
            with col2:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)
            
            status_text.text("🔍 Performing OCR on image...")
            progress_bar.progress(25)
            
            # Initialize OCR reader
            reader = easyocr.Reader(ocr_languages, gpu=False)
            progress_bar.progress(40)
            
            # Perform OCR
            result = reader.readtext(image)
            
            # Filter results by confidence
            filtered_results = [res for res in result if res[2] >= confidence_threshold]
            extracted_text = " ".join([res[1] for res in filtered_results])
            
            status_text.text("✅ Text extracted from image successfully!")
            progress_bar.progress(50)
        
        # Store in session state
        st.session_state.extracted_text = extracted_text
        
        # Show original text
        if extracted_text.strip():
            st.markdown('<div class="translation-box">', unsafe_allow_html=True)
            st.subheader("📝 Extracted Text:")
            st.write(extracted_text)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Translation section
            if st.button("🔄 Translate Text", type="primary"):
                status_text.text("🌐 Translating text...")
                progress_bar.progress(75)
                
                try:
                    translator = Translator()
                    
                    # Translate to Sinhala
                    sinhala_translation = translator.translate(extracted_text, dest='si')
                    st.session_state.sinhala_text = sinhala_translation.text
                    
                    # Translate to English
                    english_translation = translator.translate(extracted_text, dest='en')
                    st.session_state.english_text = english_translation.text
                    
                    status_text.text("✅ Translation completed!")
                    progress_bar.progress(100)
                    
                except Exception as e:
                    st.error(f"Translation error: {str(e)}")
                    status_text.text("❌ Translation failed")
        
        else:
            st.warning("⚠️ No text found in the uploaded file. Please try with a different file or adjust OCR settings.")
        
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        status_text.text("❌ File processing failed")

# Display translations if available
if st.session_state.sinhala_text or st.session_state.english_text:
    st.markdown("---")
    
    # Sinhala translation
    if st.session_state.sinhala_text:
        st.markdown('<div class="sinhala-box">', unsafe_allow_html=True)
        st.subheader("🇱🇰 Sinhala Translation:")
        st.write(st.session_state.sinhala_text)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # English translation
    if st.session_state.english_text:
        st.markdown('<div class="english-box">', unsafe_allow_html=True)
        st.subheader("🇺🇸 English Translation:")
        st.write(st.session_state.english_text)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Download section
    st.markdown("---")
    st.subheader("💾 Download Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Download as TXT
        if st.button("📄 Download as TXT"):
            result_text = f"""KOSA Document Translator - Translation Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Original Text:
{st.session_state.extracted_text}

Sinhala Translation:
{st.session_state.sinhala_text}

English Translation:
{st.session_state.english_text}

---
Generated by KOSA Translator
"""
            st.download_button(
                "📥 Click to Download TXT",
                result_text,
                file_name=f"translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
    
    with col2:
        # Download as PDF
        if st.button("📑 Download as PDF"):
            try:
                pdf_buffer = create_pdf_report(
                    st.session_state.extracted_text,
                    st.session_state.sinhala_text,
                    st.session_state.english_text
                )
                
                st.download_button(
                    "📥 Click to Download PDF",
                    pdf_buffer.getvalue(),
                    file_name=f"translation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"PDF generation error: {str(e)}")
    
    with col3:
        # Clear results
        if st.button("🗑️ Clear Results"):
            st.session_state.extracted_text = ""
            st.session_state.sinhala_text = ""
            st.session_state.english_text = ""
            st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <h4>🚀 KOSA Document & Image Translator</h4>
    <p>Powered by EasyOCR, Google Translate, and Streamlit</p>
    <p><strong>Created with ❤️ by KOSA</strong></p>
</div>
""", unsafe_allow_html=True)
