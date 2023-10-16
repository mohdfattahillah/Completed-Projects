# Project Overview

My friend wants to create a new company in the field of mobile phones and he wants to compete with well-known mobile phone brands such as Samsung, Vivo, Oppo, Xiaomi, etc.

The problem was, he didn't know how to estimate the price of the cellphone his company would make. Because competition from popular brands is very competitive, he didn't want to just assume. Therefore, he collected cellphone sales data from several companies.

My friend wants to find out the relationship between the features of a cellphone and its selling price. But a new problem arose, he was not good at machine learning, so he needed my help to solve this problem.

# Main Objective

The main goal of this project is to create a Classification Model that is able to predict the price range of a cellphone based on the size, features and performance of the cellphone.

# Exploratory Data Analysis

![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/b7ca265f-550d-47af-8045-da6c5bc93e16)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/0830441b-cd4a-4272-befd-fe15a6f504fe)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/3c9f1bd7-0eb5-4235-a10e-9791f97171be)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/71a40545-a47a-4225-85e3-7b51ee4b7fbf)

# Model Analysis

**K-Nearest Neighbors (KNN):** The KNN model shows low accuracy and a fairly good F1 Score, indicating reasonable classification ability. However, there is still room for improvement in predictions.

**Decision Tree:** The Decision Tree model has good performance with high accuracy and a balanced F1 Score. This is a worthy choice for the price class classification of the phone.

**Random Forest:** The Random Forest model also shows good performance with high accuracy and an AUC Score that is close to 1. This is a strong model in predicting cellphone price classes.

**AdaBoost:** The AdaBoost model has lower performance compared to other models. A low F1 Score indicates that this model may need to be improvised or a different model option needs to be considered when it comes to predicting mobile phone price classes.

**Support Vector Machine (SVM):** The optimized SVM model with hyperparameter tuning shows excellent performance. High accuracy, AUC Score close to 1, and high F1 Score indicate that SVM is the best model in predicting cellphone price classes.

In conclusion, a well-tuned SVM model is the best choice for predicting phone price classes, with excellent accuracy, AUC Score and F1 Score. Decision Tree and Random Forest models also have good performance. The KNN model needs further improvement, while the AdaBoost model needs significant improvements in its performance. Choosing the right model depends on how high accuracy and reliability you want in predicting cellphone prices, and in this project I decided to use the SVM model.

![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/da43c159-edf4-4ce3-9d98-2f71bd000009)
![image](https://github.com/mohdfattahillah/Completed-Projects/assets/36840127/b17b18af-0b33-45e7-9485-9031d56ac3fb)

# Conclusion

In this project, the main goal is to build a classification model that can predict the price range of cellphones based on a number of relevant features and specifications. The background of this project is a company that wants to compete in the highly competitive mobile phone industry. They don't want to just rely on assumptions but want to have a solid understanding of what factors influence the price of a phone.

To achieve this goal, I have carried out a series of steps such as, data exploration, data preprocessing, feature selection, hyperparameter tuning, selecting the best machine learning model, and model evaluation. The results of the model evaluation show that the SVM model with hyperparameter tuning has excellent performance in predicting cellphone price ranges, with high accuracy, AUC Score, F1 Score, and good confusion matrix.

Thus, the overall conclusion of this project is that I have succeeded in building a model that can provide accurate predictions of cellphone price ranges based on certain features and specifications. These results will be very useful for new companies in making strategic decisions regarding the pricing of their products. Apart from that, this project also shows how important machine learning is in helping companies make decisions based on relevant data. With this model, companies can compete more effectively in a competitive market.

# Further Improvement

**Collection of More and Recent Data**: Try to collect more data or more complete current data. More complete and up-to-date data can help improve model performance by providing deeper insight into the factors that influence phone prices.

**More Advanced Feature Engineering**: Do more experiments with feature engineering. Try to create new features that may be more relevant or have a stronger correlation with the price of the phone. This can improve the accuracy of the model.

**Model Tuning**: Try different types of machine learning models such as logistic regression, XGBoost, or neural networks. Sometimes, a different model can provide better results for a particular problem.

**More Hyperparameter Optimization**: Run more hyperparameter tuning experiments for the models used. There may be better combinations of hyperparameters that have not yet been explored.

**More Comprehensive Cross-Validation**: Perform more comprehensive cross-validation, including layered cross-validation or other specialized cross-validation techniques.

**Model Interpretation**: Describes the factors that most influence the model's phone price predictions. This can provide valuable insights to companies for decision making.

**Model Monitoring**: Once a model is deployed in production, it is important to monitor its performance periodically. Can implement monitoring mechanisms to ensure that models remain accurate over time.

**Expansion to Production Platforms**: If a company decides to use this model in daily decision making, it will need to consider how to integrate it into the company's production platform safely and efficiently.

**Consider Other Business Aspects**: Apart from technical factors, consider other business aspects such as marketing strategy, pricing strategy and market reaction to the price of a new phone. These are factors that can have a significant impact on product success.

**Internal Team Training**: If the company has a larger internal team, consider providing that team with training or a deeper understanding of machine learning. This can help them understand and apply project results better.

Continuing to develop and improve this model is an important step to achieving success in the mobile phone business. Don't hesitate to continue experimenting and collaborating with the business team to ensure the model provides maximum value for the company.

# Deployment

[Huggingface](https://huggingface.co/spaces/mohdfattahillah/Mobile-Price-Category-Application)
