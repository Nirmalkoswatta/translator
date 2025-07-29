# Sample Test Files

This folder contains sample files for testing the KOSA Document & Image Translator.

## Sample Files

### Images
- Place test images with text here
- Supported formats: JPG, PNG, WebP, BMP, TIFF
- For best OCR results, use high-resolution images with clear text

### PDFs
- Place test PDF documents here
- Make sure PDFs are not password protected
- Both text-based and image-based PDFs are supported

## Testing Tips

1. **Image Quality**: Use images with:
   - High contrast between text and background
   - Clear, readable fonts
   - Minimal skew or rotation
   - Good lighting and resolution

2. **PDF Files**: Test with:
   - Simple text documents
   - Scanned documents (will use OCR)
   - Multi-page documents
   - Documents with mixed languages

3. **Languages**: Try files containing:
   - English text
   - Sinhala text
   - Mixed language content
   - Different scripts and fonts

## Example Test Cases

1. Upload an English document → Should translate to Sinhala
2. Upload a Sinhala image → Should translate to English
3. Upload a multi-page PDF → Should extract all text
4. Test with low-quality images → Adjust OCR confidence threshold

Happy testing! 🚀
