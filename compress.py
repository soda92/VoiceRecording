import glob
import subprocess
from pathlib import Path
import tqdm

wav_files = list(glob.glob("*.WAV"))


for wav in tqdm.tqdm(wav_files):
    # wav = wav_files[i]
    wav_path = Path(wav)
    f_7z = wav_path.parent.joinpath(wav_path.stem + ".7z")
    if f_7z.exists():
        continue

    subprocess.run(["7z", "a", f_7z, wav_path], check=True)
