# Project Overview

How does the credit card system work?

Every month, you receive a bill (X) that reflects your credit card spending.
You make payment (Y), usually the minimum amount due, on the due date stated on the billing statement.

The next month's bill includes the remaining balance from the previous month (X - Y) plus any new costs (X') incurred in that month.

You make another payment (Y') to cover part of the new bill.
This cycle repeats itself, with each month's bill combining previous balances, new expenses, and reduced payments.
Missing the minimum payment due date results in late payments, often accompanied by late fees. Additionally, persistent delays can result in payment default

What is a defaulter?

A person is considered a defaulter by the bank when they fail to make the required payments on their credit card or loan according to agreed terms. In the context of credit cards, default usually occurs when the cardholder misses the minimum payment on the due date specified in the statement.

source: https://www.investopedia.com/how-do-credit-card-payments-work-5069924

# Main Objective

The main aim of this project is to find out what factors influence whether a client will be called a defaulter or will fail to pay next month. After knowing the factors that significantly influence this, later I will create a machine learning model that can predict whether someone will default next month using the machine learning model Logistic Regression, Support Vector Machine Classifier, and K Nearest Neighbors.

# Exploratory Data Analysis

![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/e772ea22-863a-4489-83ed-fa4ba9060918)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/ec85ca72-a6a6-4f2e-8039-43b4bb004175)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/36aeb251-2560-4dc4-9d85-1c0d130d7c2d)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/12ec19a9-623c-49c9-bdcf-22d3ef696a97)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/200a5faa-74a8-495d-a83c-732395dff6ee)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/e908dc83-5659-4756-a1d3-7e537894f870)

# Model Analysis

**1. LOGISTIC REGRESSION MODEL:**

Excess:
- *Simple and easy to interpret. The coefficient value can provide insight into the factors that influence the likelihood of default.*
- *Logistic regression results can be interpreted as a probability of default, so they can be used to classify risks more clearly.*

Lack:
- *Not able to handle non-linear relationships between predictor variables and target variables.*
- *Less flexible in handling outliers compared to some other models such as SVC or KNN.*
- *Requires the assumption of independence between predictor variables, which may not always be met in banking data.*

**2. SUPPORT VECTOR CLASSIFIER (SVC) MODEL:**

Excess:
- *Can handle non-linear data through the use of kernels, such as the RBF kernel.*
- *Tends to be more tolerant of outliers compared to Logistic Regression.*
- *Able to separate potentially overlapping classes in a higher feature space.*

Lack:
- *SVC performance may be affected by the choice of kernel parameters and other hyperparameters.*
- *Does not provide a direct interpretation of the factors that influence predictions, so it is less intuitive to understand.*

**3. K-NEAREST NEIGHBORS (KNN) MODEL:**

Excess:
- *Does not require certain assumptions about data distribution.*
- *Easy to implement and understand.*
- *Can handle data that is not linear and has the potential for different clusters.*

Lack:
- *Vulnerable to scale changes and variations in attributes due to using distance metrics.*
- *KNN can be computationally heavy, especially with large amounts of data.*
- *Choosing the right K value (number of nearest neighbors) can influence the prediction results.*

To obtain optimal results in credit card default modeling, we can consider conducting experiments with all these three models and performing parameter tuning accordingly. Additionally, ensemble learning and other methods such as Decision Trees or Random Forests can also be explored to improve model performance.

# Conclusion

In this project I used Variance Threshold and SelectKBest to find the best features that can be used to predict whether a client will default on their credit card next month. In the feature selection, I found that the significant factors that influence credit card payment failure are the feature columns: pay_sept, pay_aug, pay_jul, pay_jun, pay_may, pay_apr. This feature column contains historical data that shows whether the client paid on time or was in arrears, and how many months in arrears.

In this project I also use hyperparameter tuning techniques to find the best hyperparameters that the model can use on this data. This technique really helps increase the efficiency of project work and provides better results.

As a conclusion and to answer the main objective of this project, namely: creating a machine learning model to predict whether a client will default on their credit card in the next month and analyzing the data to identify significant factors that influence the probability of credit card default, it can be concluded that the Logistic model Regression, SVM Classifier, and K Nearest Neighbors can be used well to predict which clients will default on their credit cards next month. However, of the three models, the best model is the SVM Classifier.

# Further Improvement

To perfect this project, further development can be carried out by using a pipeline mechanism for feature engineering processes to model training. The pipeline mechanism can shorten time, streamline coding syntax, and there is no need to repeat steps to be carried out. Apart from that, the pay_sept - pay_apr feature column can be encoded using an ordinal encoder because this column contains historical data on payments and payment arrears. The more months in arrears means it will have a direct effect on the model's predictions later, and if it has been encoded using an ordinal encoder, later we can determine predictions more accurately.

# Deployment

[Huggingface](https://huggingface.co/spaces/mohdfattahillah/Credit-Card-Defaulter-ML-Prediction)
