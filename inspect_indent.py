from pathlib import Path
p = Path(r'c:/Users/Yash Rajput/OneDrive/Desktop/OCR PLATFORM/ocr-readiness-platform/app.py')
lines = p.read_text(encoding='utf-8').splitlines()
for idx in range(400, 430):
    line = lines[idx]
    print(idx+1, repr(line), 'indent=', len(line) - len(line.lstrip(' ')))
