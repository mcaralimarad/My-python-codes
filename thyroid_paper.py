# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 11:47:25 2023

@author: Aralimarad
"""

import pandas as pd
"""import express"""
import matplotlib.pyplot as plt
import numpy as py
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
from sklearn.impute import KNNImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score
import warnings
warnings.filterwarnings("ignore")
"""from tensorflow.keras.utils import to_categorical"""
from sklearn.metrics import accuracy_score
def new_func():
    data=pd.read_csv('E:\Koli\hypothyroid.csv')
    return data

def new_func1(new_func):
    data = new_func()
    return data

data = new_func1(new_func)
data=data.replace('?',None)
data=data.replace('P',1)
data=data.replace('N',0)
data.dropna(inplace=True)
data.reset_index(drop = True, inplace = True)
k=data[['TSH','T3','T4U',"Outcome"]].copy()

k=k.astype(float)
x=0
for i in k['TSH']:
    if k.iloc[x,0]>=7:
        k.iloc[x,0]=7
    if k.iloc[x,0]<=0:
        k.iloc[x,0]=0
    x=x+1

k.to_csv('s.csv',index=False)
print(k)

p=k.copy()


x=0
tmin={}
tmax={}
y={}
for i in p:
    tmin[p.columns[x]]=(min(p[i]))
    tmax[p.columns[x]]=(max(p[i]))
    x=x+1
y['min']=tmin.values()
y['max']=tmax.values()
py=pd.DataFrame(y)
py.to_csv('minmax.csv')
tpp=p.copy()
if 1==1:
    for i in p.columns[:-1]:
        x=0
        for ii in p[i]:
            tpp[i][x]=int(((p[i][x]-tmin[i])/(tmax[i]-tmin[i]))*100)
            if tpp[i][x]>100 or tpp[i][x]<0:
                print(str(i)+'=='+str(ii)+'=='+str(tmin[i])+'=='+str(tmax[i])+'=='+str(p[i][x]))
            x=x+1
    p=tpp.copy()
    print(p)
    
    p.to_csv('Normalized.csv')
    p0=p.copy()
    PPP=p.copy()



   



   




ff={}
fk={}
negmax=[]

for ik in range(3):
    print('ik-'+str(ik))
    k=ik
    k1=p.iloc[:,k]
    k2=p.columns[k]

    l1=[]
    l2=[]
   
    x1=0
    x2=0
    x=0
    for ii in k1:
        if p.iloc[x,-1]==1:
            l1.append(ii)
            x1=x1+1
        else:
            l2.append(ii)
            x2=x2+1
        x=x+1
 
    l1min=min(l1)
    l1max=max(l1)
    l1count=x1-1
    l2min=min(l2)
    l2max=max(l2)
    negmax.append(l2max)
    l2count=x2-1

    s1=str(l1min)+'-'+str(l1max)+'-'+str(l1count)
    s2=str(l2min)+'-'+str(l2max)+'-'+str(l2count)

    print(s1)
    print(s2)
    plt.scatter(l1,l1,marker='+',label='Positive')
    plt.ylabel(k2)
    plt.xlabel(k2)
    h=((max(k1)-min(k1))/10)
    n=[min(k1)]
    n1=min(k1)
    for i in range(10):
        n1=n1+h
        n.append(int(n1))
    n.append(max(k1))
    print(len(n))
    print(n)

    #plt.xticks(n)
    #plt.yticks(n)
    plt.legend()
    s=str(k2)+'-1-Distribution of Positive Disease'
    plt.title(s)
    #plt.show()
    #plt.savefig(s,bbox_inches = 'tight')
    plt.close()
    









    plt.scatter(l2,l2,c='red',marker='_',label='Negative')
    plt.ylabel(k2)
    plt.xlabel(k2)
    #plt.xticks(n)
    #plt.yticks(n)
    plt.legend()
    s= str(k2)+'-2-Distribution  of Negative Disease'
    plt.title(s)
    #plt.savefig(s,bbox_inches = 'tight')
    #plt.show()
    plt.close()
       
       
    t1={}
    for i in l1:
        t1[i]=0
    
    for i in l1:
        t1[i]=t1[i]+1
    t1=dict(sorted(t1.items()))
    print(t1)

    t2={}
    for i in l2:
        t2[i]=0
    
    for i in l2:
        t2[i]=t2[i]+1
    t2=dict(sorted(t2.items()))
    print(t2)

    plt.scatter(t1.keys(),t1.values(),c='red',marker='+',label='Positive')
    plt.scatter(t2.keys(),t2.values(),c='blue',marker='_',label='Negative')
    plt.xlabel(k2)
    plt.ylabel('Frequency')
    #plt.xticks(n)
    
    plt.legend()
    s=str(k2)+'-1-Distribution ' 
    plt.title(s)
    plt.savefig(s,bbox_inches = 'tight')
    plt.show()
    plt.close()


    z=min(k1)
    tcount={}
    fcount={}
    acc={}

    print('k1-------------------')
    print(k1)
    z=min(k1)
    while z<=max(k1):
        tcount[z]=0
        fcount[z]=0
        acc[z]=0


        x=0
        s1=0
        for i in p.iloc[:,-1]:
            if k1[x]==z:
                if i==1:
                    tcount[z]+=1
                if i==0:
                    fcount[z]+=1
                s1=s1+1
            
            x=x+1

        if (fcount[z]+tcount[z])>0:
            acc[z]=((tcount[z]-fcount[z])/(fcount[z]+tcount[z])*100)
        
        z=z+1
    
    print('accuracy')
    print(acc)

    d1=min(acc)-1
    d2=max(acc)+1
    for i in acc.keys():
        if acc[i]>d1:
            d1=acc[i]
            m1=i
    ff[ik] =list(acc.values())
    fk[ik]=list(acc.keys())

plt.scatter(fk[0],ff[0],color='red',marker='x',label='Confidence of TSH')
plt.scatter(fk[1],ff[1],color='green',marker='_',label='Confidence of T3')
plt.scatter(fk[2],ff[2],color='blue',marker='+',label='Confidence of T4')
plt.xlabel('Normalized Values of Features')
plt.ylabel('Confidence Values')
plt.legend()
plt.title('Confidence Values of TSH, T3 and T4 Hormones' )
plt.savefig("confidence Values",bbox_inches = 'tight')
plt.show()








print(ff)
fp=pd.DataFrame(ff)  
fp.to_csv('accuracy.csv',index=False)
print(fp) 
print(p)
result={}
c1={}
c2={}

x1=0
th=0
for i in p0.iloc[:,0]:
    l=[]
    l1=[]
    x2=0
    
  
    for ii in p0.iloc[0,:-1]:
        
        l.append(fp.iloc[int(p.iloc[x1,x2]),x2])
        x2=x2+1
   

    if p0.iloc[x1,-1]==1:

        c1[x1]=int(sum(l))
      
    else:
        c2[x1]=int(sum(l))

    
    result[x1]=int(sum(l))
    
    x1=x1+1

print(x1)
print(x2)

print(result)





plt.scatter(c1.values(),c1.values(),c='red',marker='+',label='positive')
plt.scatter(c2.values(),c2.values(),c='blue',marker='_',label='Negative')


plt.legend()
#plt.xticks(rotation=90)
s='Combined Frequency Values of Attributes'
plt.title(s)
plt.savefig(s,bbox_inches = 'tight')
plt.show()
plt.close()


sc1={}
sc2={}
sc11={}
sc21={}
for i in range(min(result.values()),max(result.values())+1):
    c1count=0
    c2count=0
    for ii in c1.values():
        if ii ==i:
            c1count=c1count+1
    if c1count!=0:
        sc1[i]=c1count
        sc11[i]=c1count
    else:
        sc11[i]=0

    for ii in c2.values():
        if ii ==i:
            c2count=c2count+1
    if c2count!=0:
        sc2[i]=c2count
        sc21[i]=c2count
    else:
        sc21[i]=0
    

t={}
t['PositiveKeys']=sc11.keys()
t['PositiveValues']=sc11.values()
t['NegativeKeys']=sc21.keys()
t['NegativeValues']=sc21.values()
tp=pd.DataFrame(t)
tp.to_csv('result.csv',index=False)

plt.scatter(sc1.keys(),sc1.values(),c='red',marker='+',label='Positive')
plt.scatter(sc2.keys(),sc2.values(),c='blue',marker='_',label='Negative')
#plt.plot([67,67],[min(sc2),max(sc2)],c='Orange',label='Separator')

plt.legend()
#plt.xticks(rotation=90)
plt.xlabel('Fuzzy Function Values')
plt.ylabel('Frequency of Fuzzy Function Values')
s='Distribution of Results with Fuzzy Frequencies'
plt.title(s)
plt.savefig(s,bbox_inches = 'tight')
plt.show()
plt.close()

print('result----------------')
print(result)
if 1==1:
    z=min(result.values())
    tcount={}
    fcount={}
    acc={}

    z=min(result.values())
    while z<=max(result.values()):
        tcount[z]=0
        fcount[z]=0
        acc[z]=0


        x=0
        t=0
        for i in p.iloc[:,-1]:
            if result[x]!=0:
                if i==1:
                    if result[x]>=z:
                        tcount[z]+=1
                    else:
                        fcount[z]+=1
                if i==0:
                    if result[x]<z:
                        tcount[z]+=1
                    else:
                        fcount[z]+=1
                t=t+1

            x=x+1

        acc[z]=((tcount[z])/t)*100
        z=z+1
    d=0
    for i in acc.keys():
        if acc[i]>d:
            d=acc[i]
            m=i
    print(str(d)+'==='+str(m)+'==='+str(min(result.values()))+'==='+str(max(result.values())))
    print(t)


    





    z=min(result.values())
    flag=0
    c=0
    while z<=max(result.values()):
        if flag==0:
            x=0
            t=0
        
            for i in p.iloc[:,-1]:
                if result[x]<=z:
                    if i==1:
                        flag=1
                        c=z
                    t=t+1

                x=x+1
        z=z+1

           
    print(str(c)+'mmmmm'+str(t))






   








if 1==1:
    s={}
    x=0
    for i in result.values():
        if i >=137:
            s[x]=1
        else:
            s[x]=0
        x=x+1
   
    print(accuracy_score(list(s.values()),PPP.iloc[:,-1]))
    print(f1_score(list(s.values()),PPP.iloc[:,-1]))
    print(precision_score(list(s.values()),PPP.iloc[:,-1]))
    print(recall_score(list(s.values()),PPP.iloc[:,-1]))
   
    confusion_matrix = pd.crosstab(p.iloc[:,-1],s,rownames=['Actual'], colnames=['Predicted'])
    print (confusion_matrix)

    X_train=p.iloc[:,0:-1]
    Y_train=PPP.iloc[:,-1]
    X_test=p.iloc[:,0:-1]
    Y_test=PPP.iloc[:,-1]

    model = linear_model.LinearRegression()
    model.fit(X_train,Y_train)
    predictions = model.predict(X_test)
    x=0
    #print(predictions)
    for i in predictions:
        predictions[x]=int(i)
        x=x+1
    print("Accuracy for Linear Model Classifier is : ",accuracy_score(predictions,Y_test))
    print(accuracy_score(predictions,Y_test))
    print(f1_score(predictions,Y_test))
    print(precision_score(predictions,Y_test))
    print(recall_score(predictions,Y_test))

    confusion_matrix = pd.crosstab(predictions,Y_test,rownames=['Actual'], colnames=['Predicted'])
    print (confusion_matrix)
    #Predict_KNN(X_train,Y_train,X_test,Y_test):
    # K values are in range of 1 to 100 only considering the odd numbers
    k_values = [k for k in range(1,100,2)]
    
    model = KNeighborsClassifier()
    param_grid = dict(n_neighbors=k_values)

    # defining parameter range
    grid = GridSearchCV(model, param_grid, cv=10, scoring='accuracy', return_train_score=False,verbose=1,n_jobs=-1)

    # fitting the model for grid search
    grid_search=grid.fit(X_train, Y_train)

    print(grid_search.best_params_)
    predictions = grid.predict(X_test)
    print("Accuracy for KNN is : ",accuracy_score(predictions,Y_test))
    print(accuracy_score(predictions,Y_test))
    print(f1_score(predictions,Y_test))
    print(precision_score(predictions,Y_test))
    print(recall_score(predictions,Y_test))
  
    confusion_matrix = pd.crosstab(predictions,Y_test,rownames=['Actual'], colnames=['Predicted'])
    print (confusion_matrix)


    #Predict_GaussianNB(X_train,Y_train,X_test,Y_test):
    Bayes_Model = GaussianNB()
    Bayes_Model.fit(X_train,Y_train)
    predictions = Bayes_Model.predict(X_test)
    print("Accuracy for Naive Beyes is : ",accuracy_score(predictions,Y_test))
    print(accuracy_score(predictions,Y_test))
    print(accuracy_score(predictions,Y_test))
    print(f1_score(predictions,Y_test))
    print(precision_score(predictions,Y_test))
    print(recall_score(predictions,Y_test))
    confusion_matrix = pd.crosstab(predictions,Y_test,rownames=['Actual'], colnames=['Predicted'])
    print (confusion_matrix)

    #Predict_RandomForest(X_train,Y_train,X_test,Y_test):
    model = RandomForestClassifier()
    model.fit(X_train,Y_train)
    predictions = model.predict(X_test)
    print("Accuracy for Random Forest Classifier is : ",accuracy_score(predictions,Y_test))
    print(accuracy_score(predictions,Y_test))
    print(accuracy_score(predictions,Y_test))
    print(f1_score(predictions,Y_test))
    print(precision_score(predictions,Y_test))
    print(recall_score(predictions,Y_test))
    confusion_matrix = pd.crosstab(predictions,Y_test,rownames=['Actual'], colnames=['Predicted'])
    print (confusion_matrix)



    