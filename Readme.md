# 🌱 Healthify AI - Personalized Wellness Companion

**Healthify AI** is an intelligent health score prediction system that provides personalized wellness assessments based on daily lifestyle inputs.  
The application uses machine learning to analyze user data and generate comprehensive health insights.

---

## 📖 Project Overview
Healthify AI transforms raw lifestyle and health data into actionable insights, helping users understand their fitness levels and make informed wellness decisions.

---

## 🎯 Features

### 👤 Demographic Profile Analysis
- **Personal Information:** Age, gender tracking  
- **Body Composition:** Height, weight, BMI calculation with automatic categorization  
- **Advanced Metrics:** Body fat percentage with visual status indicators  
- **Real-time BMI Analysis:** Automatic classification (Underweight ⚠️, Healthy ✅, Overweight 📈, Obese 🚨)

### 💪 Exercise & Activity Tracking
- **Workout Frequency:** Days per week with visual metrics  
- **Session Duration:** Average workout hours with detailed tracking  
- **Calories Burned:** Daily energy expenditure with activity level indicators  
- **Experience Level:** 5-point scale with personalized feedback  
- **Weekly Summary:** Total hours and calories burned  

### 🍎 Smart Nutrition Analysis
- **Personalized Calorie Calculator:** BMR and TDEE using Mifflin-St Jeor equation  
- **Goal-Oriented Planning:** Weight loss, maintenance, or muscle gain targets  
- **Macronutrient Calculator:** Ideal ratios for protein, carbs, and fats  
- **Hydration Tracking:** Water intake based on body weight  
- **Meal Pattern Analysis:** Optimal meal frequency recommendations  
- **Diet Type Support:** Vegan, Vegetarian, Paleo, Keto, Low-Carb, Balanced  

### 🤖 AI-Powered Predictions
- **ML Model:** Scikit-learn based health score prediction  
- **Real-time Analysis:** Instant wellness scoring based on all inputs  
- **5-Star Rating System:** Comprehensive health assessment  
- **Personalized Feedback:** Actionable insights and recommendations  

---

## 🛠️ Technical Implementation

### 🧩 Architecture
- **Frontend:** Streamlit  
- **Backend:** Scikit-learn ML Model  
- **Data Processing:** Pandas  
- **Model Serialization:** Pickle  

### ⚙️ Key Algorithms
- Mifflin-St Jeor Equation for BMR calculation  
- Activity multipliers for TDEE estimation  
- ML model for health score prediction  
- Macronutrient ratios based on fitness goals  

### 🧾 Data Features
```python
feature_set = [
    'Age', 'Session_Duration', 'Calories_Burned', 'Fat_Percentage',
    'Water_Intake', 'Workout_Frequency', 'Experience_Level', 'BMI',
    'Daily_meals_frequency', 'Carbs', 'Proteins', 'Fats', 'Calories',
    'Gender_Male', 'diet_type_Keto', 'diet_type_Low-Carb', 
    'diet_type_Paleo', 'diet_type_Vegan', 'diet_type_Vegetarian'
]
```

## 📊 Model Details
### 🔢 Prediction Output

- Scale: 1–5 star rating system

- Normalization: Linear scaling for user-friendly display

- Real-time Updates: Instant recalculation on input changes

## 🧮 Feature Engineering

- Automatic BMI calculation from height & weight

- Experience level scaling (normalized 1–3 range)

- One-hot encoding for categorical data

- Calorie balance calculations for goal tracking

## 💡 Usage Guide
- For Users

- Start with Demographics: Enter age, gender, height, and weight

- Log Activity: Add workout frequency, duration, and calories burned

- Track Nutrition: Input daily calorie and macro data

- Get AI Insights: Receive a personalized health score and recommendations