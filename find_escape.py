from pathlib import Path
p=Path(r'c:/Users/Yash Rajput/OneDrive/Desktop/OCR PLATFORM/ocr-readiness-platform/app.py')
for i,l in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
    if '//' in l or '\\' in l:
        print(i, l)
