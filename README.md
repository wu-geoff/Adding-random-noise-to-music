# Adding random noise to music

A Python script for adding random noises to a MP3 file, using a [CSPRNG](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator).

## How to run

`python3 add_noise_to_music.py <path to MP3 file>`

## Dependencies 
 - Python3+
 - [numpy](https://numpy.org/)
 - [pydub](https://www.pydub.com/) 
     - Note: pydub will requrie either [ffmpeg](https://ffmpeg.org/) or [libav](http://libav.org/) to work with MP3 files; I personally chose ffmpeg.

## Origins 

This whole Python script was partially inspired by "Guess The Song" (Chinese: 估歌仔), a game from the *Super Trio series*, a variety show series from TVB. 

Simply put, a non-Cantonese or Mandarin speaking foreigner will do their best to sing well-known Cantonese or Mandarin songs, and the guests will try to figure out the song's name. Since the foreigners don't know Cantonese or Mandarin, it's inevitable that their best-effort approximations will be (unintentionally) hilarious to a Chinese auidence. 

Being an IT worker myself, I started to wonder: *Can this task be automated away?* 🤔 (First rule of IT: if a task can be automated away, it __should__. ✌️)

## The answer

The answer turned out the both a yes *and* no.

To put a long story short, even though it was *technically* feasible to add a bunch of random noises to a soundtrack (thus making it almost indiscernible), the fact that it was done electronically also made the soundtrack __absolutely unbearable__ to a human auidence - to the point a lawyer might suggest it constituted "[cruel and unusual punishment](https://en.wikipedia.org/wiki/Cruel_and_unusual_punishment)". 🤣

## Acknowlegements

This weird experiment of mine won't be possible without the help of the following:
 - [Generating White Noise in Python: A Step-by-Step Guide](https://www.brownnoiseradio.com/resources/generating-white-noise-in-python%3A-a-step-by-step-guide) by Brown Noise Radio
 - Google's AI overview on the matter

## License

[MIT](https://choosealicense.com/licenses/mit/)






