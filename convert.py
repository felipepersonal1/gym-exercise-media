# Baixe essa biblioteca para rodar o comando: python -m pip install moviepy imageio imageio-ffmpeg

# Converte .gif para .mp4 pois fica mais leve
import os
from moviepy import VideoFileClip


INPUT_DIR = "gifs"
OUTPUT_DIR = "mp4"

# cria pasta de saída se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".gif")]

print(f"Encontrados {len(files)} GIFs para converter...")

for i, file in enumerate(files, start=1):
    gif_path = os.path.join(INPUT_DIR, file)
    mp4_path = os.path.join(
        OUTPUT_DIR,
        file.replace(".gif", ".mp4")
    )

    try:
        clip = VideoFileClip(gif_path)

        clip.write_videofile(
            mp4_path,
            codec="libx264",
            fps=clip.fps or 24,
            audio=False,
            preset="medium",
            threads=4,
            logger=None
        )

        clip.close()
        print(f"[{i}/{len(files)}] Convertido: {file}")

    except Exception as e:
        print(f"[ERRO] {file}: {e}")

print("Conversão finalizada 🚀")