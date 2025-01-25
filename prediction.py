import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

model = joblib.load('output/model.pkl')
scaler = StandardScaler()
# Input data Here
data = {
  'Age' : 35,
  'BusinessTravel' : 2, 
  'DailyRate' : 804, 
  'Department' : 1, 
  'DistanceFromHome' : 3,
  'Education' : 3, 
  'EducationField' : 1, 
  'EnvironmentSatisfaction' : 1, 
  'Gender' : 1,
  'HourlyRate' : 30, 
  'JobInvolvement':3, 
  'JobLevel':5, 
  'JobRole':3,
  'JobSatisfaction':3, 
  'MaritalStatus':1, 
  'MonthlyIncome':18265, 
  'MonthlyRate':8733,
  'NumCompaniesWorked':5, 
  'OverTime':1, 
  'PercentSalaryHike':22,
  'PerformanceRating':3, 
  'RelationshipSatisfaction':3, 
  'StockOptionLevel':1,
  'TotalWorkingYears' : 25, 
  'TrainingTimesLastYear' : 2, 
  'WorkLifeBalance' : 3,
  'YearsAtCompany' : 8, 
  'YearsInCurrentRole' : 8, 
  'YearsSinceLastPromotion' : 3,
  'YearsWithCurrManager' : 8, 
  'overall_satisfaction' : 3.50, 
  'Age_Category': 2,
  'YearsWithManagerCategory' : 3
}

data_df = pd.DataFrame([data])
scaled_data = scaler.fit_transform(data_df)

output = model.predict(scaled_data)
if output == 0:
    print('Karyawan di prediksi tetap')
else:
    print('Karyawan di prediksi keluar')