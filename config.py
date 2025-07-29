# KOSA Translator Configuration

# Application Settings
APP_TITLE = "KOSA Document & Image Translator"
APP_DESCRIPTION = "Translate documents and images to Sinhala and English"
CREATOR = "KOSA"

# OCR Settings
DEFAULT_OCR_LANGUAGES = ['en']
AVAILABLE_OCR_LANGUAGES = ['en', 'si', 'ta', 'hi', 'fr', 'de', 'es', 'ar']
DEFAULT_CONFIDENCE_THRESHOLD = 0.5

# Translation Settings
SUPPORTED_TRANSLATION_LANGUAGES = {
    'English': 'en',
    'Sinhala': 'si',
    'Tamil': 'ta',
    'Hindi': 'hi',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Arabic': 'ar'
}

# File Upload Settings
MAX_FILE_SIZE_MB = 50
SUPPORTED_IMAGE_FORMATS = ["jpg", "jpeg", "png", "webp", "bmp", "tiff"]
SUPPORTED_DOCUMENT_FORMATS = ["pdf"]

# UI Settings
PRIMARY_COLOR = "#667eea"
SECONDARY_COLOR = "#764ba2"
SUCCESS_COLOR = "#4ecdc4"
WARNING_COLOR = "#ff6b6b"

# Export Settings
ENABLE_TXT_EXPORT = True
ENABLE_PDF_EXPORT = True
PDF_PAGE_SIZE = "A4"

# Performance Settings
USE_GPU_FOR_OCR = False  # Set to True if you have CUDA GPU
OCR_BATCH_SIZE = 1
TRANSLATION_CHUNK_SIZE = 5000  # Characters per translation request
