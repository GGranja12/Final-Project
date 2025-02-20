# SecondGear Consulting - Your Trusted Co-Pilot in the UK Used-Car Market! 🚗🤝

![image](https://github.com/user-attachments/assets/3fa6745d-d2a4-4f8e-8ff4-22fcaa8ec988)

## *Project Overview* 📝

#### Welcome to my Ironhack's Final Project!

This final project was developed during Ironhack's Data Analytics course to showcase and solidify the knowledge acquired over the past months. It focuses on applying data visualization (Tableau), Python programming, exploratory data analysis (EDA), and machine learning techniques.

I present myself as a used-car market consultant at SecondGear Consulting, a British company dedicated to helping future data analysts who may consider settling in the UK. Our goal is to provide a comprehensive overview of the UK’s used-car market and offer a predictive price tool to support data-driven buying decisions.

## *The Dataset* 🗃

The data was retrieved from 9 different brand .csv files (brand.csv) which can be downloaded by accessing this [Kaggle page](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes?select=toyota.csv) The used-car listings were originally webscrapped by the author presumably in 2020.

The provided .csv files present one listing price (in pounds £) column and 8 attributes as follows:

- **model**: listed car model
- **year**: listed car registration year
- **transmission**: listed car gearbox type (Automatic/Manual)
- **mileage**: listed car's mileage 
- **fuelType**: listed car's fuel type 
- **tax**: annual car's tax in pounds (£)
- **mpg**: miles per gallon - how far the car can travel for every gallon (or 4.55 litres) of fuel it uses
- **engineSize**: listed car's engine size in litres

## *Project Development* 🛠️

This [Trello board](https://trello.com/b/5rpwY1yF/ironhack-final-project) provides access to the project's workflow, detailing all tasks developed.

#### *Tableau dashboards* 📊

After applying data preparation and cleaning techniques in a Python notebook, I developed a [Tableau dashboard](https://public.tableau.com/app/profile/guilherme.granja/viz/Tableau_FinalProject_17400007171180/Painel1?publish=yes) to provide the audience with a clear and straighforward overview of insightful aspects related to our UK's used-car market dataset. 

#### *Exploratory Data Analysis* 

The EDA process included the following key tasks:

- Correlation Analysis: An overview of relationships between continuous variables, supported by heatmap and scatterplot visualizations;
- Categorical Variable Insights: Chi-square tests and interpretation of Cramér's V results to evaluate relationships between categorical variables;
- Hypothesis Testing: Assessing assumptions and drawing conclusions about the data through ANOVA and two sample t-test;
- Distribution and Outlier Analysis: Examining numerical variable distributions and identifying potential outliers.

#### *Supervised Machine Learning - Random Forest Model* 🦾 📈

Keeping in mind that our target feature is listing price, the machine learning process involved transforming categorical variables using One Hot Encoding (for brand, transmission, and fuel type) and Label Encoding (for car model) to prepare the data for training and testing with a Random Forest Regression model.

As a final step, I evaluated the model’s performance using four key metrics: R², RMSE, MSE, and MAE, assessing its fitness and predictive accuracy. Additionally, I analyzed the feature importances derived from the Random Forest model to understand the impact of each variable on price predictions.

##### *Predictive Pricing Tool* 🤖🚗

After saving my ML model, I developed an auxiliary Python script (app.py) to showcase a web application supported by Streamlit interface and components. In this app the user is able to provide inputs like car brand an model, transmission and fuel type, registration year and mileage (kms) and get a predictive price that will support their buying decisions.

In this repo you will find all the necessary files to set up and run the project yourself
  - Start by installing the environment dependencies in your own virtual environment using *pip install -r requirements.txt*;
  - Run the jupyter notebook so that you can save the ML model in a .pkl format; 
  - With your chosen environment activated run the following command in your terminal *streamlit run app.py*;
  - When you are done, stop the app by going back to your terminal and pressing Ctrl + C.

#### *Presentation* 🎬

For a summarized overview of the project feel free to access the [Canva presentation](https://www.canva.com/design/DAGflnRBCuw/ZdCaucLnamxxhLuo3DQS2w/edit?utm_content=DAGflnRBCuw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

## *Final Remarks* ✏

Special thanks to my teachers, Isidre and Nicolas, for all the support and feedback.
