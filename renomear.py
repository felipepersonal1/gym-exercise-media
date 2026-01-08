import os

def renomear_videos(pasta, prefixo="video"):
    arquivos = [
        f for f in os.listdir(pasta)
        if f.lower().endswith(".mp4")
    ]

    arquivos.sort()  # mantém ordem previsível

    for i, nome in enumerate(arquivos, start=1):
        antigo = os.path.join(pasta, nome)
        novo = os.path.join(pasta, f"{prefixo}{i}.mp4")

        if antigo == novo:
            continue

        os.rename(antigo, novo)

    print(f"{len(arquivos)} vídeos renomeados com sucesso 🎬")

if __name__ == "__main__":
    caminho_pasta = input("Digite o caminho da pasta dos vídeos: ").strip()
    renomear_videos(caminho_pasta)
