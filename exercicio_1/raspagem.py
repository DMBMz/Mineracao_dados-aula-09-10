import sys
import requests
from bs4 import BeautifulSoup

# Configuração para garantir saída correta de caracteres UTF-8 no terminal Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Lista de possíveis URLs onde a página pode estar sendo servida:
# 1) Se o servidor foi iniciado na raiz do projeto (WS.9-10-26)
# 2) Se o servidor foi iniciado diretamente dentro da pasta exercicio_1
POSSIVEIS_URLS = [
    "http://127.0.0.1:8000/exercicio_1/index.html",
    "http://127.0.0.1:8000/exercicio_1/",
    "http://127.0.0.1:8000/index.html",
    "http://127.0.0.1:8000/",
]

def obter_pagina_html():
    """Tenta conectar ao servidor local nas URLs comuns e retorna a resposta."""
    for url in POSSIVEIS_URLS:
        try:
            resposta = requests.get(url, timeout=3)
            if resposta.status_code == 200 and "TechNova Academy" in resposta.text:
                return resposta, url
        except requests.exceptions.RequestException:
            continue
    return None, None

def raspar_catalogo():
    print("=" * 65)
    print("       EXERCÍCIO 1 - RASPAGEM DE CATÁLOGO DE CURSOS")
    print("=" * 65)

    resposta, url_usada = obter_pagina_html()

    if not resposta:
        print("\n[ERRO] Não foi possível conectar ao servidor HTTP local!")
        print("Antes de rodar este script, inicie o servidor local com o comando:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        print("\nVerifique se o terminal está na pasta do projeto e tente novamente.")
        sys.exit(1)

    print(f"\n[+] Conectado com sucesso em: {url_usada}")
    print("[*] Iniciando análise do DOM com BeautifulSoup...\n")

    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")

    # Localizar todos os cartões de cursos na página
    cursos = soup.find_all("article", class_="curso-card")

    if not cursos:
        print("[!] Nenhum curso encontrado na estrutura HTML.")
        return

    print(f"[+] Total de cursos localizados: {len(cursos)}")
    print("-" * 65)

    # Iterar sobre cada curso extraindo suas informações
    for i, curso in enumerate(cursos, start=1):
        # 1. Extração do nome do curso
        tag_nome = curso.find("h2", class_="curso-nome")
        nome = tag_nome.get_text(strip=True) if tag_nome else "Nome não encontrado"

        # 2. Extração da área
        tag_area = curso.find(class_="curso-area")
        area = tag_area.get_text(strip=True) if tag_area else "Área não encontrada"

        # 3. Extração da carga horária
        tag_carga = curso.find(class_="curso-carga")
        carga = tag_carga.get_text(strip=True) if tag_carga else "Carga não encontrada"

        # 4. Extração da lista de assuntos (elementos <li> dentro da tag <ul>)
        tag_ul = curso.find("ul", class_="curso-assuntos")
        assuntos = []
        if tag_ul:
            for item in tag_ul.find_all("li"):
                assuntos.append(item.get_text(strip=True))

        # Exibição organizada e formatada dos dados raspados
        print(f"\nCURSO {i}: {nome.upper()}")
        print(f"  • Área: {area}")
        print(f"  • Carga Horária: {carga}")
        print("  • Assuntos Estudados:")
        if assuntos:
            for j, assunto in enumerate(assuntos, start=1):
                print(f"     {j}. {assunto}")
        else:
            print("     (Nenhum assunto cadastrado)")
        print("-" * 65)

    print("\n[✓] Raspagem finalizada com sucesso!\n")

if __name__ == "__main__":
    raspar_catalogo()
