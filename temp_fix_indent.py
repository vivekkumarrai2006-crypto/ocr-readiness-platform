from pathlib import Path
p = Path(r'c:/Users/Yash Rajput/OneDrive/Desktop/OCR PLATFORM/ocr-readiness-platform/app.py')
lines = p.read_text(encoding='utf-8').splitlines()
start = next(i for i, line in enumerate(lines) if '# STEP 1 — Select Analysis Region' in line)
end = next(i for i, line in enumerate(lines) if 'elif "📊 History" in nav:' in line)
for i in range(start, end):
    if lines[i].strip():
        lines[i] = '    ' + lines[i]
    else:
        lines[i] = ''
p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'Indented lines {start+1} through {end}')
