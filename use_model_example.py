# Import the libraries needed
import tensorflow as tf
import pandas as pd
import numpy as np

# Configure Tensorflow to use 6 CPU threads
tf.config.threading.set_inter_op_parallelism_threads(6)

# Import the model via the load_model function
model = tf.keras.models.load_model('./model/settings')

# Declaration of class names
CLASS_NAMES = {'Junior Network Administrator',
               'Junior Programmer', 'Junior Web Programmer'}

#
sample = {
    "iq": 139,
    "interest_outside_school": "Art",
    "interest_outside_school_2": "Economics",
    "interest_outside_school_3": "Sport",
    "interest_outside_school_4": "",
    "favorite_subject_it": "Desain web",
    "favorite_subject_it_2": "Pemrograman Web",
    "favorite_subject_it_3": "Komputer Animasi",
    "favorite_subject_it_4": "",
    "name": "Dina Berliana Br Sitohang",
    "hobbies": "Sport",
    "hobbies_2": "Read books",
    "hobbies_3": "Movies",
    "hobbies_4": "Social Media",
    "hobbies_5": "''",
    "hobbies_6": "''",
    "hobbies_7": "''",
    "hobbies_8": "''",
    "hobbies_9": "''",
    "junior_network_administrator": 82.8,
    "junior_web_programmer": 76.42,
    "junior_programmer": 80.7,
}

input_dict = {name: tf.convert_to_tensor(
    [value]) for name, value in sample.items()}
predictions = np.argmax(model.predict(input_dict))
predictions = pd.DataFrame(CLASS_NAMES)[0][predictions]
print(predictions)
