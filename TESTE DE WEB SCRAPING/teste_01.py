import os
import requests
from bs4 import BeautifulSoup
import zipfile

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

os.makedirs('pdfs', exist_ok=True)

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].lower().endswith('.pdf')]

anexos = [link for link in pdf_links if 'Anexo I' in link or 'Anexo II' in link]

anexos = [link if link.startswith('http') else requests.compat.urljoin(url, link) for link in anexos]

baixados = []
for link in anexos:
    nome_arquivo = os.path.join('pdfs', os.path.basename(link))
    print(f'Baixando {nome_arquivo}...')
    r = requests.get(link, stream=True)
    with open(nome_arquivo, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    baixados.append(nome_arquivo)

zip_filename = 'anexos.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for arquivo in baixados:
        zipf.write(arquivo, os.path.basename(arquivo))

print(f'Arquivos compactados em: {zip_filename}')
