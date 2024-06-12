import os

from pypdf import PdfReader

reader = PdfReader('tmp/Python Testing with Pytest (Brian Okken).pdf')

print(reader.pages)
print(len(reader.pages))
assert len(reader.pages) == 256

print(reader.pages[1].extract_text())
assert 'the individual' in reader.pages[1].extract_text()
assert 3035139 == os.path.getsize('tmp/Python Testing with Pytest (Brian Okken).pdf')