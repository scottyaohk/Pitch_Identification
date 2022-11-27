import joblib
import librosa
import numpy as np

# load the WAV file of a note and transform it onto the pitch spectrum
def loaddata(path):
    x, sr = librosa.load(path)
    fmin = librosa.midi_to_hz(36)
    hop_length = 512
    C = librosa.cqt(x, sr=sr, fmin=fmin, n_bins=72, hop_length=hop_length)
    logC = librosa.amplitude_to_db(np.abs(C))
    logCx=np.average(logC,axis=1)
    standardizedlogCx=(logCx-min(logCx))/max(logCx-min(logCx))*50
    standardizedlogCx=np.expand_dims(standardizedlogCx**2/50, axis=0)
    return standardizedlogCx

# load the trained model
clf = joblib.load("SVM_PI.m")

# test it with dataset{num}
num=25 # you can change this number between 21 and 25, so that it doesn't overlap with the training data
for i in range(1,22):
    test_X = loaddata(f"./datasets/dataset{num}/{num}-{i}.wav")
    print(clf.predict(test_X))