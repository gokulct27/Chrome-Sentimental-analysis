# Chrome_Review_Sentiment_Analyzer
### About Project Processing
   #### Business Problem
    
   There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating. 
   Your goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. 
   
   ### PreProcessing
   
   As the part before give data to the Model first we need to do some preprocessing to make data best fit for model. Beacouse it is Natural Language Processing 
   problem and we get the data in Text formate so we need to do preprocessing of the avilable text.
   In preprocessing I did some manipulation 
        1.Removing all other charecter accept a-z and A-Z
        2.Remove all spacial Charecter 
        3.Segmentation
        4.All text convert into lower case 
        5.Limetization
        6.Tockenization
        7.Feature Extraction
        8.Vectorizer 
        9.Word Cloud formation
        10.Also remove the unwanted columns which is not use during model building process like:
             review=review.drop(['ID','Review URL','Thumbs Up','User Name','Developer Reply','Developer Reply','version',Review Date','App ID'],axis=1)

   ### Model Bulding Part
   In order to bild the model we use Linear Support Vector Classifier which is a classification model present in Sklearn library.
   I use is beacouse after using several model like DecisionTree, RandomForest, Naive Bayes I come up with that SVC giving me the good accuracy 
   of 69% which is decent for the NLP classification model.
   After applying SVC model I save it as a Pickle file for the deployment purpose.
   Then I prdict the value of sentiment and add to the excesting data with a new column name "Pridicted Review" in order to complete the Business requrement
   to display only those reviews for which the sentiment of review is not mach with the given Star.
   In order to full fill this requriment I apply the condition which check the odd review condition and display them and after that I save that file to the CSV file 
   to save it to the external memory.
   
   ### Deployment
   
   For deployment I use Streamlit.
   In order to use this app user first going to browse the csv file for which they want the review analization and after that the backend work of model start
   i.e. preprocessing and model analization after done all the work model give the output which you can download as a CSV file.
   

   
   
   Q.Ranking Data - Understanding the co-relation between keyword rankings with description or any other attribute.
      Q1.Is there any co-relation between short description, long description and ranking? Does the placement of keyword (for example - using a keyword in the first 10       words - have any co-relation with the ranking)?
      A. Yes, their is a co-relation between the short and long description that in the long description the comment start with bullet and the comment in the short           description have some what same values. And the ranking has no co-relation with both the description.
      
   Q2.Does APP ID (Also known as package name) play any role in ranking?  
   A.Yes, it tell us that the ranking w.r.t to which app. Ranking is directly proposnal to App ID.
   
   1. Write a regex to extract all the numbers with orange color background from the below text in italics.

    {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},     {"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
    
   A. (?<=:)\d+
      
