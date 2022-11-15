import numpy as np
import librosa
import librosa.display
import soundfile as sf
import scipy as sp
import matplotlib.pyplot as plt

plt.switch_backend('agg')

# trim the sound
def trimming(path):
    y, sr = librosa.load(path)
    y_trimmed, _ = librosa.effects.trim(y,top_db=30)
    return y_trimmed, sr

# Turn the relative scale to the pitch
def convertToPitch(num):       
    standard=np.array([50,47,45,42,40,38,35,33,30,28,26,23,21,18,16,14,11,9,6,4,2])
    deviation=abs(num-standard)
    lisdeviation=list(deviation)
    indexmin=lisdeviation.index(min(lisdeviation))
    return indexmin+1

def deriveRawFeatureModified(filename,picpath):
    x, sr = trimming(filename)
    fmin = librosa.midi_to_hz(36)
    hop_length = 512
    C = librosa.cqt(x, sr=sr, fmin=fmin, n_bins=72, hop_length=hop_length)     # Compute the constant-Q transform of an audio signal

    # changing the scale
    logC = librosa.amplitude_to_db(np.abs(C))
    logCx=np.average(logC,axis=1)
    standardizedlogCx=(logCx-min(logCx))/max(logCx-min(logCx))*50
    standardizedlogCx=standardizedlogCx**2/50

    # detect the leftmost peak with a high prominence
    result=sp.signal.find_peaks(standardizedlogCx,prominence=13)[0][0]
    pitch=convertToPitch(result)

    # draw pitch spectrum
    plt.plot(standardizedlogCx)
    plt.title(f"Note {pitch}")
    plt.xlabel("Pitch in relative scale")
    plt.ylabel("Amplitude in relative scale")
    plt.savefig(picpath)
    plt.close()

    return pitch

def pitchidentification(wavfile,picpath):
    return deriveRawFeatureModified(wavfile,picpath)



