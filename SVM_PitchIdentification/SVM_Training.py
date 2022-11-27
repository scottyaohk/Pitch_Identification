import librosa
import numpy as np
from sklearn import svm
import joblib


# load the WAV file of a note, transform it onto the pitch spectrum and label it with y
def load_labeled_data(path,y):
    x, sr = librosa.load(path)
    fmin = librosa.midi_to_hz(36)
    hop_length = 512
    C = librosa.cqt(x, sr=sr, fmin=fmin, n_bins=72, hop_length=hop_length)
    logC = librosa.amplitude_to_db(np.abs(C))
    logCx=np.average(logC,axis=1)
    standardizedlogCx=(logCx-min(logCx))/max(logCx-min(logCx))*50
    standardizedlogCx=np.expand_dims(np.append(standardizedlogCx**2/50,y),axis=0)
    return standardizedlogCx


# load labeled datasets, prepare the training data
training_data=np.empty(shape=(0,73))
for dataset_num in range(1,21):  # use dataset1 to dataset20 to form the training data
    for i in range(1,22):
        data=load_labeled_data(f"./datasets/dataset{dataset_num}/{dataset_num}-{i}.WAV",i)
        training_data=np.append(training_data, data, axis=0)
x_train, y_train = np.split(training_data, (72,), axis=1)

# train
clf = svm.SVC(C=1, kernel='linear', gamma=1, decision_function_shape='ovo')
clf.fit(x_train, y_train.ravel())

# download the model
joblib.dump(clf, "SVM_PI.m")