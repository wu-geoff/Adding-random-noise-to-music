from pydub import AudioSegment
import numpy as np
import sys, os
from secrets import randbelow

if len(sys.argv) > 1:
    file_path = str(sys.argv[1])
    file_name = os.path.basename(file_path)
    audio = AudioSegment.from_mp3(file_path)

    samples = np.array(audio.get_array_of_samples())

    # Generate noises with a CSPRNG
    noises = [randbelow(np.iinfo(samples.dtype).max) for _ in range(len(samples))]

    noisy_samples = samples + noises

    # Ensure samples are within the valid range for the audio format
    noisy_samples = noisy_samples.astype(samples.dtype)

    # Export the noisy result as MP3
    noisy_audio = AudioSegment(
        noisy_samples.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=audio.sample_width,
        channels=audio.channels
    )
    noisy_audio.export(f"{file_name}_noisy.mp3", format="mp3")
else:
    print("Please provide a file name.")

