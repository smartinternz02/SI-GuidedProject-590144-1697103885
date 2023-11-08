import pickle
import numpy as np
print(np.__version__)
model=pickle.load(open('svm.pkl','rb'))
print(model.predict(np.array([[1,2,3,4]])))