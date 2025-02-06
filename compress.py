import glob
import subprocess
from pathlib import Path

wav_files = list(glob.glob("*.WAV"))

for wav in wav_files:
    
