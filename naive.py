import pandas as pd 
import numpy as np 
from collections import defaultdict
import re
def start():
    def preprocess_string(str_arg):
        cleaned_str=re.sub('[^a-z\s]+',' ',str_arg,flags=re.IGNORECASE) #every char except alphabets is replaced
        cleaned_str=re.sub('(\s+)',' ',cleaned_str) #multiple spaces are replaced by single space
        cleaned_str=cleaned_str.lower() #converting the cleaned string to lower case
    
        return cleaned_str # returning the preprocessed string 

    class NaiveBayes:
    
        def __init__(self,unique_classes):
        
            self.classes=unique_classes # Constructor is sinply passed with unique number of classes of the training set
        

        def addToBow(self,example,dict_index):
            if isinstance(example,np.ndarray): example=example[0]
     
            for token_word in example.split(): #for every word in preprocessed example
          
                self.bow_dicts[dict_index][token_word]+=1 #increment in its count
            
        def train(self,dataset,labels):
            self.examples=dataset
            self.labels=labels
            self.bow_dicts=np.array([defaultdict(lambda:0) for index in range(self.classes.shape[0])])
        
        #only convert to numpy arrays if initially not passed as numpy arrays - else its a useless recomputation
        
            if not isinstance(self.examples,np.ndarray): self.examples=np.array(self.examples)
            if not isinstance(self.labels,np.ndarray): self.labels=np.array(self.labels)
            
        #constructing BoW for each category
            for cat_index,cat in enumerate(self.classes):
                all_cat_examples=self.examples[self.labels==cat] #filter all examples of category == cat
            
            #get examples preprocessed
            
                cleaned_examples=[preprocess_string(cat_example) for cat_example in all_cat_examples]
            
                cleaned_examples=pd.DataFrame(data=cleaned_examples)
            
            #now costruct BoW of this particular category
                np.apply_along_axis(self.addToBow,1,cleaned_examples,cat_index)
            prob_classes=np.empty(self.classes.shape[0])
            all_words=[]
            cat_word_counts=np.empty(self.classes.shape[0])
            for cat_index,cat in enumerate(self.classes):
                prob_classes[cat_index]=np.sum(self.labels==cat)/float(self.labels.shape[0]) 
            
            #Calculating total counts of all the words of each class 
                count=list(self.bow_dicts[cat_index].values())
                cat_word_counts[cat_index]=np.sum(np.array(list(self.bow_dicts[cat_index].values())))+1 # |v| is remaining to be added
            
            #get all words of this category                                
                all_words+=self.bow_dicts[cat_index].keys()
                                                     
        
        #combine all words of every category & make them unique to get vocabulary -V- of entire training set
        
            self.vocab=np.unique(np.array(all_words))
            self.vocab_length=self.vocab.shape[0]
                                  
        #computing denominator value                                      
            denoms=np.array([cat_word_counts[cat_index]+self.vocab_length+1 for cat_index,cat in enumerate(self.classes)])                                                                          
      
        
            self.cats_info=[(self.bow_dicts[cat_index],prob_classes[cat_index],denoms[cat_index]) for cat_index,cat in enumerate(self.classes)]                               
            self.cats_info=np.array(self.cats_info)                                 
                                              
                                              
        def getExampleProb(self,test_example):                                
            likelihood_prob=np.zeros(self.classes.shape[0]) #to store probability w.r.t each class
            for cat_index,cat in enumerate(self.classes): 
                for test_token in test_example.split(): #split the test example and get p of each test word
                test_token_counts=self.cats_info[cat_index][0].get(test_token,0)+1
                test_token_prob=test_token_counts/float(self.cats_info[cat_index][2])                              
                likelihood_prob[cat_index]+=np.log(test_token_prob)
            post_prob=np.empty(self.classes.shape[0])
            for cat_index,cat in enumerate(self.classes):
                post_prob[cat_index]=likelihood_prob[cat_index]+np.log(self.cats_info[cat_index][1])                                  
      
            return post_prob
    
   
        def test(self,test_set):
      
    
            predictions=[] #to store prediction of each test example
            for example in test_set: 
                                              
            #preprocess the test example the same way we did for training set exampels                                  
                cleaned_example=preprocess_string(example) 
             
            #simply get the posterior probability of every example                                  
                post_prob=self.getExampleProb(cleaned_example) #get prob of this example for both classes
            
            #simply pick the max value and map against self.classes!
                predictions.append(self.classes[np.argmax(post_prob)])
                
            return np.array(predictions) 
#############################################################################
        
    from sklearn.datasets import fetch_20newsgroups
    categories=['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med'] 
    newsgroups_train=fetch_20newsgroups(subset='train',categories=categories)

    train_data=newsgroups_train.data #getting all trainign examples
    train_labels=newsgroups_train.target #getting training labels
#print ("Total Number of Training Examples: ",len(train_data)) # Outputs -> Total Number of Training Examples:  2257
#print ("Total Number of Training Labels: ",len(train_labels)) # Outputs -> #Total Number of Training Labels:  2257

    nb=NaiveBayes(np.unique(train_labels)) #instantiate a NB class object
    print ("---------------- Training In Progress --------------------")
 
    nb.train(train_data,train_labels) #start tarining by calling the train function
    print ('----------------- Training Completed ---------------------')

    newsgroups_test=fetch_20newsgroups(subset='test',categories=categories) #loading test data
    test_data=newsgroups_test.data #get test set examples
    test_labels=newsgroups_test.target #get test set labels

    print ("Number of Test Examples: ",len(test_data)) # Output : Number of Test Examples:  1502
    print ("Number of Test Labels: ",len(test_labels)) # Output : Number of Test Labels:  1502


    pclasses=nb.test(test_data) #get predcitions for test set

#check how many predcitions actually match original test labels
    test_acc=np.sum(pclasses==test_labels)/float(test_labels.shape[0]) 

    print ("Test Set Examples: ",test_labels.shape[0]) # Outputs : Test Set Examples:  1502
    print ("Test Set Accuracy: ",test_acc*100,"%") # Outputs : Test Set Accuracy:  93.8748335553 %

    training_set=pd.read_csv('labeledTrainData.tsv',sep='\t') # reading the training data-set

#getting training set examples labels
    y_train=training_set['sentiment'].values
    x_train=training_set['review'].values
    from sklearn.model_selection import train_test_split
    train_data,test_data,train_labels,test_labels=train_test_split(x_train,y_train,shuffle=True,test_size=0.25,random_state=42,stratify=y_train)
    classes=np.unique(train_labels)

# Training phase....

    nb=NaiveBayes(classes)
    nb.train(train_data,train_labels)

# Testing phase 

    pclasses=nb.test(test_data)
    test_acc=np.sum(pclasses==test_labels)/float(test_labels.shape[0])

    print ("Test Set Accuracy: ",test_acc) # Output : Test Set Accuracy:  0.84224 :)

# Loading the my test dataset
    print ("Loading the my test dataset....")
    testfile = pd.read_csv('test.tsv',sep='\t')
    testdata = testfile.review.values

#generating predictions....
    print ("Generating predictions....")
    pclasses=nb.test(testdata) 

#writing results to csv(dataframe) 
    result_df=pd.DataFrame(data=np.column_stack([testfile["review"].values,pclasses]),columns=["Review","Sentiment"])
    result_df.to_csv("mytestdataresults.csv",index=False)
    print ('Predcitions Generated and saved to mytestdatareults.csv')
