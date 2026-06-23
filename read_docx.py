import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
path = Path(r'c:\Users\param\OneDrive\Desktop\drive-download-20260623T194711Z-3-001\Contest Briefing.docx')
with zipfile.ZipFile(path) as z:
    xml = z.read('word/document.xml').decode('utf-8')
root = ET.fromstring(xml)
ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
texts = [t.text for t in root.findall('.//w:t', ns) if t.text]
for i, line in enumerate(texts[:500]):
    print(f'{i+1}: {line}')
