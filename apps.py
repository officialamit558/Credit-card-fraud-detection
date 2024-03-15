import streamlit as st
import numpy as np
import pickle

# Load the model from disk
filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))

def predict(message):
    message = [float(x) for x in message.split()]
    vect = np.array(message).reshape(1, -1)
    prediction = clf.predict(vect)
    return prediction

def main():
    st.title('Prediction App')
    st.write('Enter your message below:')

    message = st.text_input('Message')

    if st.button('Predict'):
        if message:
            prediction = predict(message)
            st.write(f'Prediction: {prediction}')
        else:
            st.write('Please enter a message.')

if __name__ == '__main__':
    main()
