import os
import csv
from zipfile import ZipFile
from pypdf import PdfReader
from xlrd import open_workbook
from io import BytesIO

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
RESOURCES_DIR = os.path.join(CURRENT_DIR, 'resources')
ZIP_FILE_PATH = os.path.join(RESOURCES_DIR, 'some_files.zip')

PDF_FILE = os.path.join(RESOURCES_DIR, 'Locators_table.pdf')
XLS_FILE = os.path.join(RESOURCES_DIR, 'Book1xls.xls')
CSV_FILE = os.path.join(RESOURCES_DIR, 'Book2csv.csv')


def test_create_zip_with_files():
    assert os.path.exists(PDF_FILE), f"{PDF_FILE} не существует."
    assert os.path.exists(XLS_FILE), f"{XLS_FILE} не существует."
    assert os.path.exists(CSV_FILE), f"{CSV_FILE} не существует."

    if not os.path.exists(RESOURCES_DIR):
        os.makedirs(RESOURCES_DIR)

    with ZipFile(ZIP_FILE_PATH, 'w') as zipf:
        zipf.write(PDF_FILE, os.path.basename(PDF_FILE))
        zipf.write(XLS_FILE, os.path.basename(XLS_FILE))
        zipf.write(CSV_FILE, os.path.basename(CSV_FILE))

    assert os.path.exists(ZIP_FILE_PATH), f"ZIP файл не был создан: {ZIP_FILE_PATH}"

    with ZipFile(ZIP_FILE_PATH, 'r') as zipf:
        files_in_zip = zipf.namelist()
        assert os.path.basename(PDF_FILE) in files_in_zip, f"{os.path.basename(PDF_FILE)} не найден в архиве"
        assert os.path.basename(XLS_FILE) in files_in_zip, f"{os.path.basename(XLS_FILE)} не найден в архиве"
        assert os.path.basename(CSV_FILE) in files_in_zip, f"{os.path.basename(CSV_FILE)} не найден в архиве"
        print(f'Файлы успешно запакованы в {ZIP_FILE_PATH}')


def test_read_zip():
    with ZipFile(ZIP_FILE_PATH, 'r') as zipf:
        files_in_zip = zipf.namelist()
    assert files_in_zip == ['Locators_table.pdf', 'Book1xls.xls', 'Book2csv.csv']


def test_read_pdf():
    with ZipFile(ZIP_FILE_PATH, 'r') as zipf:
        with zipf.open('Locators_table.pdf') as file:
            pdf_data = BytesIO(file.read())
            reader = PdfReader(pdf_data)
            text = reader.pages[0].extract_text()
            assert 'General Whole web page xpath=/html css=html document.documentElement NA' in text


def test_read_xls():
    with ZipFile(ZIP_FILE_PATH, 'r') as zipf:
        with zipf.open('Book1xls.xls') as file:
            xls_data = BytesIO(file.read())
            workbook = open_workbook(file_contents=xls_data.read())
            sheet = workbook.sheet_by_index(0)
            cell_value = sheet.cell_value(1, 0)
            rows_number = sheet.nrows
            assert sheet.nrows > 0, "XLS файл пустой!"
            assert cell_value == 'Ilya', f"Ожидаемое значение 'Ilya', но найдено '{cell_value}'"
            assert rows_number == 13, f"Ожидаемое значение '13', но найдено '{rows_number}'"


def test_read_csv():
    with ZipFile(ZIP_FILE_PATH, 'r') as zipf:
        with zipf.open('Book2csv.csv') as file:
            content = file.read().decode('utf-8-sig')
            csvreader = list(csv.reader(content.splitlines(), delimiter=';'))
            last_row = csvreader[-1]  # Проверяем последнюю строку
            expected_last_row = ['Artur', 'Che', '25', 'Archer']
            assert last_row == expected_last_row, f"Ожидаемое значение {expected_last_row}, но найдено {last_row}"
