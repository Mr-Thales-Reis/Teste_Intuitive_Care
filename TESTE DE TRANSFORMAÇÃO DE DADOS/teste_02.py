import pandas as pd
import tabula
import zipfile
import os

# Nome do arquivo PDF do Anexo I (deve estar na mesma pasta ou com o caminho correto)
pdf_path = 'Anexo_I.pdf'

tabelas = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

df = tabelas[0]
df.rename(columns={'OD': 'Outras Despesas', 'AMB': 'Ambulatorial'}, inplace=True)

csv_filename = 'dados_transformados.csv'
df.to_csv(csv_filename, index=False)

zip_filename = 'Teste_seu_nome.zip'  
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(csv_filename, os.path.basename(csv_filename))

print(f'CSV extraído e compactado em: {zip_filename}')
