# KOSA Document & Image Translator

A powerful web application that extracts text from images and PDFs, then translates them to Sinhala and English. Built with Streamlit and featuring a mobile-friendly design.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

## 🌟 Live Demo

Try it live: [KOSA Translator on Streamlit Cloud](https://your-app-url.streamlit.app)

## ✨ Features

- 📸 **Image OCR**: Extract text from images using EasyOCR
- 📄 **PDF Text Extraction**: Extract text from PDF documents
- 🌐 **Multi-language Translation**: Translate to Sinhala and English
- 📱 **Mobile-Friendly Design**: Responsive layout for all devices
- 💾 **Export Options**: Download translations as TXT or PDF
- ⚙️ **Customizable Settings**: Adjust OCR languages and confidence thresholds
- 🎨 **Beautiful UI**: Modern gradient design with KOSA branding

## 🚀 Quick Start

### Option 1: Run Online (Recommended)
Visit our [Streamlit Cloud deployment](https://your-app-url.streamlit.app) - no installation required!

### Option 2: Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/kosa-translator.git
   cd kosa-translator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

### Option 3: Windows Quick Start
- Double-click `launcher.bat` for an interactive menu
- Or run `install.bat` followed by `run_app.bat`

## 📖 How to Use

1. **Upload a File**: Choose an image (JPG, PNG, WebP, BMP, TIFF) or PDF
2. **Text Extraction**: 
   - Images: OCR automatically extracts text
   - PDFs: Text is extracted directly
3. **Translation**: Click "Translate" to get Sinhala and English translations
4. **Download**: Export results as TXT or formatted PDF

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **OCR**: EasyOCR
- **Translation**: Google Translate API
- **PDF Processing**: PyMuPDF
- **PDF Generation**: ReportLab
- **Image Processing**: Pillow

## 📦 Installation

### Requirements
- Python 3.8+
- pip package manager

### Dependencies
```bash
pip install streamlit>=1.28.0
pip install easyocr>=1.7.0
pip install googletrans==4.0.0-rc1
pip install PyMuPDF>=1.23.0
pip install Pillow>=9.5.0
pip install reportlab>=4.0.0
```

### Full Installation
```bash
# Clone the repository
git clone https://github.com/your-username/kosa-translator.git
cd kosa-translator

# Install all dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 🔧 Configuration

Edit `config.py` to customize:
- UI colors and branding
- Supported languages
- File upload limits
- OCR settings

## 📱 Mobile Support

The application is fully responsive and optimized for:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Desktop computers
- 🖥️ Large screens

## 🌍 Language Support

### OCR Languages
- English (en)
- Sinhala (si)
- Tamil (ta)
- Hindi (hi)

### Translation Languages
- English ↔ Sinhala
- Auto-detect source language
- Expandable to more languages

## 📁 Project Structure

```
kosa-translator/
│
├── app.py                 # Main Streamlit application
├── app_basic.py          # Basic version (minimal dependencies)
├── requirements.txt      # Python dependencies
├── config.py            # Configuration settings
├── README.md            # This file
├── .streamlit/           # Streamlit configuration
│   └── config.toml
├── .github/              # GitHub workflows
│   └── workflows/
│       └── deploy.yml
├── scripts/              # Utility scripts
│   ├── install.bat
│   ├── launcher.bat
│   └── run_app.bat
└── sample_files/         # Sample files for testing
    └── README.md
```

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. **Fork this repository** to your GitHub account
2. **Visit** [share.streamlit.io](https://share.streamlit.io)
3. **Connect your GitHub** account
4. **Deploy** by selecting your forked repository
5. **Choose** `app.py` as the main file

### Deploy to Heroku

1. **Create a Heroku app**
2. **Connect to GitHub** repository
3. **Enable automatic deploys** from main branch
4. **Add buildpacks**: Python
5. **Deploy**

### Deploy to Railway

1. **Connect GitHub** repository to Railway
2. **Set start command**: `streamlit run app.py`
3. **Deploy**

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/kosa-translator.git
cd kosa-translator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
streamlit run app.py
```

## 🐛 Issues & Support

- **Bug Reports**: [Create an issue](https://github.com/your-username/kosa-translator/issues)
- **Feature Requests**: [Create an issue](https://github.com/your-username/kosa-translator/issues)
- **Documentation**: Check our [Wiki](https://github.com/your-username/kosa-translator/wiki)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for excellent OCR capabilities
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Google Translate](https://translate.google.com/) for translation services
- The open-source community for inspiration and tools

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/your-username/kosa-translator?style=social)
![GitHub forks](https://img.shields.io/github/forks/your-username/kosa-translator?style=social)
![GitHub issues](https://img.shields.io/github/issues/your-username/kosa-translator)
![GitHub license](https://img.shields.io/github/license/your-username/kosa-translator)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/kosa-translator&type=Date)](https://star-history.com/#your-username/kosa-translator&Date)

---

<div align="center">

**🌍 Built with ❤️ by KOSA**

[Website](https://kosa.dev) • [GitHub](https://github.com/kosa-dev) • [Support](mailto:support@kosa.dev)

</div>
