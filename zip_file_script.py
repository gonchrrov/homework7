import os
from zipfile import ZipFile


# Пути к файлам
pdf_file = 'tmp2/Locators_table.pdf'
xls_file = 'tmp2/Book1xls.xls'
csv_file = 'tmp2/Book2csv.csv'

# Проверка, что тестовые файлы в папке tmp2
assert os.path.exists(pdf_file), f"{pdf_file} не существует."
assert os.path.exists(xls_file), f"{xls_file} не существует."
assert os.path.exists(csv_file), f"{csv_file} не существует."

# Путь к папке для сохранения ZIP-архива
zip_folder = '/Users/goncharov/QAGURU/homework7/tmp'

# Создадим папку, если она не существует
if not os.path.exists(zip_folder):
    os.makedirs(zip_folder)

# Путь к ZIP-архиву
zip_file_path = os.path.join(zip_folder, 'some_files.zip')

# Создадим ZIP-архив и добавим в него файлы
with ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(pdf_file, os.path.basename(pdf_file))
    zipf.write(xls_file, os.path.basename(xls_file))
    zipf.write(csv_file, os.path.basename(csv_file))

print(f'Файлы успешно запакованы в {zip_file_path}')
