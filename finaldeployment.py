# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:03:10 2022

@author: Gokul ct
"""

import streamlit as st
import pandas as pd

import pickle
#cv = pickle.load(open('chrome_review_pridiction.pkl', "rb"))
st.title('Model to Check Odd ratting given by user In respect to their Star')
def convert_df(df):
   return df.to_csv().encode('utf-8')

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
p = PorterStemmer()
all_stopwords= stopwords.words('english')
all_stopwords.remove('not')

import joblib
#classifier = joblib.load('Classifier_Sentiment_Model')


def main():
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        dataset = pd.read_csv(uploaded_file,encoding='latin-1')
        st.write("filename:", uploaded_file.name)
       
        
        
        
        dataset=dataset.drop(['ID','Review URL','Thumbs Up','User Name','Developer Reply','Developer Reply','Version','Review Date','App ID'],axis=1)
        corpus=[]
        n=len(dataset)
        for i in range(0,n):
            sent = re.sub('[^a-zA-Z]', ' ',str(dataset['Text'][i]))
            sent = sent.lower()
            sent = sent.split()
            sent = [p.stem(word) for word in sent if not word in set(all_stopwords)]
            sent = ' '.join(sent)
            corpus.append(sent)
        cv = pickle.load(open('chrome_review_pridiction.pkl', "rb"))
        X_fresh = cv.transform(corpus).toarray()
        classifier = joblib.load('Classifier_Sentiment_Model')
        y_pred = classifier.predict(X_fresh)
        dataset['predicted_label'] = y_pred.tolist()
        ext=dataset[(dataset['Star']==5) & (dataset['predicted_label']==1)]
        st.write(ext)


        csv = convert_df(ext)
        
        st.download_button(
       "Click to Download",
         csv,
         "file.csv",
         "text/csv",
         key='download-csv'
         )
        


if __name__ == '__main__':
    main()