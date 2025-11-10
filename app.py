import streamlit as st 
import pickle
import pandas as pd

# Add at the top of your app
st.set_page_config(
    page_title="Health Score Analyzer",
    page_icon="🏃‍♂️",
    layout="wide"
)

# Main header with columns for better layout
col1, col2 = st.columns([2, 1])  # Fixed the variable name and syntax
with col1:
    st.title("🌱 Your Daily Wellness Companion")
    st.markdown("### Your Personalized Lifestyle Assessment")
    st.markdown("---")
# # with col2:
#     st.image("🏋️‍♂️", width=100)  # Optional: Add an image or icon

# Create expandable sections
with st.expander("👤 Demographic Profile", expanded=True):
    st.markdown("### Personal Information")
    
    # Row 1: Basic Info
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "**Age**",
            min_value=18,
            max_value=100,
            value=30,
            help="Your current age in years"
        )
    
    with col2:
        gender = st.selectbox(
            "**Gender**",
            options=["Male", "Female", "Other", "Prefer not to say"],
            index=0,
            help="For personalized health calculations"
        )
    
    st.markdown("---")
    st.markdown("### Body Composition")
    
    # Row 2: Height and Weight
    col3, col4 = st.columns(2)
    
    with col3:
        height = st.number_input(
            "**Height (cm)**",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.1,
            format="%.1f"
        )
    
    with col4:
        weight = st.number_input(
            "**Weight (kg)**",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.1,
            format="%.1f"
        )
    
    # Auto-calculate BMI
    if height > 0:
        bmi = weight / ((height/100) ** 2)
        bmi_col1, bmi_col2 = st.columns([1, 2])
        
        with bmi_col1:
            st.metric("**Calculated BMI**", f"{bmi:.1f}")
        
        with bmi_col2:
            # BMI category
            if bmi < 18.5:
                st.warning("Underweight ⚠️")
            elif bmi < 25:
                st.success("Healthy weight ✅")
            elif bmi < 30:
                st.warning("Overweight 📈")
            else:
                st.error("Obese 🚨")
    
    st.markdown("---")
    st.markdown("### Advanced Metrics")
    
    # Row 3: Body Fat Percentage
    col5, col6 = st.columns([2, 1])
    
    with col5:
        fat_percentage = st.slider(
            "**Body Fat Percentage**",
            min_value=5.0,
            max_value=50.0,
            value=20.0,
            step=0.1,
            help="Estimated body fat percentage"
        )
    
    with col6:
        # Visual feedback for body fat
        st.write("**Status:**")
        if fat_percentage < 14:
            st.success("Athletic 🏃‍♂️")
        elif fat_percentage < 24:
            st.info("Healthy 💪")
        elif fat_percentage < 32:
            st.warning("High 📊")
        else:
            st.error("Very High ⚠️")  

with st.expander("💪 Exercise & Activity", expanded=True):
    st.markdown("### Daily Workout Information")
    
    # Row 1: Workout Frequency and Duration
    col1, col2 = st.columns(2)
    
    with col1:
        workout_frequency = st.slider(
            "**Workout Frequency**",
            min_value=0,
            max_value=7,
            value=3,
            help="How many days per week do you typically exercise?"
        )
        st.metric("Days/Week", workout_frequency)
    
    with col2:
        session_duration = st.number_input(
            "**Session Duration**",
            min_value=0.0,
            max_value=4.0,
            value=1.0,
            step=0.25,
            format="%.2f",
            help="Average duration of each workout session in hours"
        )
        st.metric("Hours/Session", f"{session_duration:.2f}")
    
    st.markdown("---")
    st.markdown("### Today's Activity")
    
    # Row 2: Calories and Experience Level
    col3, col4 = st.columns(2)
    
    with col3:
        calories_burned = st.number_input(
            "**Calories Burned**",
            min_value=0,
            max_value=2000,
            value=350,
            step=50,
            help="Estimated calories burned in today's workout"
        )
        
        # Visual feedback for calories
        if calories_burned < 200:
            st.caption("Light activity 🚶‍♂️")
        elif calories_burned < 500:
            st.caption("Moderate workout 💪")
        else:
            st.caption("Intense session 🔥")
    
    with col4:
        experience_level = st.slider(
            "**Experience Level**",
            min_value=1,
            max_value=5,
            value=3,  # Changed from 0.5 to a value between 1-5
            help="Your current fitness experience level"
        )
        
        # Experience level indicators
        if experience_level < 2:
            st.success("🎯 Great start!")
        elif experience_level >= 2 and experience_level < 3:
            st.info("📈 Making progress!")
        elif experience_level >= 3 and experience_level < 4:
            st.warning("🏆 High performance!")
        elif experience_level >= 4 and experience_level < 5:
            st.error("🏆 Elite level!")
        else:
            st.error("🔥 Elite level!")
            
        # Sclae All the experience_level between 1 and 3
        experience_level = ((experience_level - 1) / 4) * 2 + 1
    
    # Row 3: Weekly Summary
    st.markdown("---")
    st.markdown("### Weekly Summary")
    
    total_weekly_hours = workout_frequency * session_duration
    estimated_weekly_calories = workout_frequency * calories_burned
    
    summary_col1, summary_col2 = st.columns(2)
    
    with summary_col1:
        st.metric("Total Weekly Hours", f"{total_weekly_hours:.1f}h")
    
    with summary_col2:
        st.metric("Estimated Weekly Calories", f"{estimated_weekly_calories} cal")
        
with st.expander("🍎 Smart Nutrition Analysis", expanded=True):
    st.markdown("### Personalized Calorie Calculator")
    
    # Get user data from session state or inputs
    if 'user_data' in st.session_state:
        age = st.session_state.user_data.get('age', 30)
        weight = st.session_state.user_data.get('weight', 70)
        height = st.session_state.user_data.get('height', 170)
        bmi = st.session_state.user_data.get('bmi', 22)
        experience_level = st.session_state.user_data.get('experience_level', 2)
        calories_burned = st.session_state.user_data.get('calories_burned', 300)
    else:
        age = 30
        weight = 70
        height = 170
        bmi = 22
        experience_level = 2
        calories_burned = 300
    
    # Calculate Basal Metabolic Rate (BMR) and TDEE
    def calculate_calorie_needs(age, weight, height, activity_level, goal='maintain'):
        # Mifflin-St Jeor Equation for BMR
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
        
        # Activity multipliers
        activity_multipliers = {
            'Beginner': 1.2,
            'Intermediate': 1.375,
            'Advanced': 1.55,
            'Athlete': 1.725
        }
        
        # Goal adjustments
        goal_adjustments = {
            'lose': -500,
            'maintain': 0,
            'gain': 300
        }
        
        tdee = bmr * activity_multipliers.get(experience_level, 1.375)
        target_calories = tdee + goal_adjustments.get(goal, 0) + calories_burned
        
        return {
            'bmr': bmr,
            'tdee': tdee,
            'target_calories': target_calories,
            'maintenance': tdee
        }
    
    # Row 1: Calorie Calculation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Your BMR", f"{calculate_calorie_needs(age, weight, height, experience_level)['bmr']:.0f} cal")
        st.caption("Basal Metabolic Rate")
    
    with col2:
        st.metric("Daily Need", f"{calculate_calorie_needs(age, weight, height, experience_level)['tdee']:.0f} cal")
        st.caption("Maintenance Calories")
    
    with col3:
        st.metric("Today's Burn", f"{calories_burned} cal")
        st.caption("Exercise Calories")
    
    st.markdown("---")
    st.markdown("### Today's Nutrition Intake")
    
    # Row 2: Smart Calorie Input with Recommendations
    col4, col5, col6 = st.columns(3)
    
    with col4:
        goal = st.selectbox(
            "**Your Goal**",
            ["Weight Loss", "Maintenance", "Muscle Gain"],
            index=1,
            help="Select your primary fitness goal"
        )
        
        goal_map = {'Weight Loss': 'lose', 'Maintenance': 'maintain', 'Muscle Gain': 'gain'}
        calorie_data = calculate_calorie_needs(age, weight, height, experience_level, goal_map[goal])
        
        recommended_calories = calorie_data['target_calories']
        
        st.info(f"🎯 Recommended: {recommended_calories:.0f} cal")
    
    with col5:
        calories = st.number_input(
            "**Actual Calories Consumed**",
            min_value=0,
            max_value=5000,
            value=int(recommended_calories),
            step=50,
            help=f"Based on your profile: {age}y, {weight}kg, {experience_level} level"
        )
        
        # Calorie balance
        calorie_balance = calories - recommended_calories
        if calorie_balance < -300:
            st.error("Significant deficit ⚠️")
        elif calorie_balance < -100:
            st.warning("Moderate deficit 📉")
        elif abs(calorie_balance) <= 100:
            st.success("On target ✅")
        elif calorie_balance > 300:
            st.warning("Significant surplus 📈")
        else:
            st.info("Moderate surplus 💪")
    
    with col6:
        st.metric("Calorie Balance", f"{calorie_balance:+.0f}")
        st.caption(f"Target: {recommended_calories:.0f} cal")
    
    st.markdown("---")
    st.markdown("### Macronutrient Calculator")
    
    # Row 3: Smart Macronutrient Recommendations
    col7, col8, col9 = st.columns(3)
    
    # Calculate ideal macros based on goal
    if goal == "Weight Loss":
        protein_ratio, carb_ratio, fat_ratio = 0.35, 0.40, 0.25
    elif goal == "Muscle Gain":
        protein_ratio, carb_ratio, fat_ratio = 0.30, 0.50, 0.20
    else:  # Maintenance
        protein_ratio, carb_ratio, fat_ratio = 0.25, 0.45, 0.30
    
    ideal_protein = (calories * protein_ratio) / 4
    ideal_carbs = (calories * carb_ratio) / 4
    ideal_fats = (calories * fat_ratio) / 9
    
    with col7:
        proteins = st.number_input(
            "**Protein (g)**",
            min_value=0,
            max_value=300,
            value=int(ideal_protein),
            step=5,
            help=f"Ideal: {ideal_protein:.0f}g for {goal}"
        )
        protein_adequacy = min(proteins / (weight * 1.6), 1.5)  # 1.6g/kg recommendation
        st.progress(protein_adequacy / 1.5)
        st.caption(f"{protein_adequacy*100:.0f}% of ideal")
    
    with col8:
        carbs = st.number_input(
            "**Carbs (g)**",
            min_value=0,
            max_value=500,
            value=int(ideal_carbs),
            step=5,
            help=f"Ideal: {ideal_carbs:.0f}g for {goal}"
        )
        carb_adequacy = min(carbs / ideal_carbs, 1.5)
        st.progress(carb_adequacy / 1.5)
        st.caption(f"{carb_adequacy*100:.0f}% of ideal")
    
    with col9:
        fats = st.number_input(
            "**Fats (g)**",
            min_value=0,
            max_value=200,
            value=int(ideal_fats),
            step=5,
            help=f"Ideal: {ideal_fats:.0f}g for {goal}"
        )
        fat_adequacy = min(fats / ideal_fats, 1.5)
        st.progress(fat_adequacy / 1.5)
        st.caption(f"{fat_adequacy*100:.0f}% of ideal")
    
    st.markdown("---")
    st.markdown("### Hydration & Meal Pattern")
    
    # Row 4: Additional Nutrition Factors
    col10, col11, col12 = st.columns(3)
    
    with col10:
        water_intake = st.slider(
            "**Water Intake (L)**",
            min_value=0.0,
            max_value=5.0,
            value=2.0,
            step=0.25,
            help=f"Recommended: {weight * 0.033:.1f}L based on your weight"
        )
        water_target = weight * 0.033  # 33ml per kg
        water_percent = min(water_intake / water_target, 1.5)
        st.progress(water_percent / 1.5)
        st.caption(f"{water_percent*100:.0f}% of hydration goal")
    
    with col11:
        daily_meals = st.slider(
            "**Meals per Day**",
            min_value=1,
            max_value=8,
            value=3,
            help="Optimal based on your schedule and goals"
        )
        if daily_meals < 3:
            st.warning("Consider more frequent meals")
        elif daily_meals > 5:
            st.info("Frequent feeding pattern")
        else:
            st.success("Balanced meal frequency")
    
    with col12:
        diet_type = st.selectbox(
            "**Diet Type**",
            options=['Vegan', 'Vegetarian', 'Paleo', 'Keto', 'Low-Carb', 'Balanced'],
            index=0,
            help="Your dietary pattern affects nutrient needs"
        )
    
    st.markdown("---")
    st.markdown("### Nutrition Intelligence")
    
    # Advanced Analysis
    analysis_col1, analysis_col2 = st.columns(2)
    
    with analysis_col1:
        # Macronutrient balance score
        actual_protein_pct = (proteins * 4) / calories * 100 if calories > 0 else 0
        actual_carb_pct = (carbs * 4) / calories * 100 if calories > 0 else 0
        actual_fat_pct = (fats * 9) / calories * 100 if calories > 0 else 0
        
        st.metric("Macro Balance", f"P:{actual_protein_pct:.0f}% C:{actual_carb_pct:.0f}% F:{actual_fat_pct:.0f}%")
        
        # Compare with ideal
        protein_diff = abs(actual_protein_pct - (protein_ratio * 100))
        carb_diff = abs(actual_carb_pct - (carb_ratio * 100))
        fat_diff = abs(actual_fat_pct - (fat_ratio * 100))
        
        balance_score = max(0, 100 - (protein_diff + carb_diff + fat_diff))
        st.progress(balance_score / 100)
        st.caption(f"Macro alignment: {balance_score:.0f}%")
    
    with analysis_col2:
        @st.cache_resource
        def load_model():
            try:
                with open('D:\IMP  ML  PROJECTS\Healthify Model\deploy_model.pkl', 'rb') as f:
                    model = pickle.load(f)
                return model
            
            except:
                st.warning("Model file not found. Using default model.")
                return None
        
        # Load the model
        model = load_model()
        
        if 'user_data' not in st.session_state:
            st.session_state.user_data = {}
            
        
        feature_data = {}
        
        feature_data['Age'] = age
        feature_data["Session_Duration (hours)"] = session_duration
        feature_data["Calories_Burned"] = calories_burned
        feature_data["Fat_Percentage"] = fat_percentage
        feature_data["Water_Intake (liters)"] = water_intake
        feature_data['Workout_Frequency (days/week)'] = workout_frequency
        feature_data["Experience_Level"] = experience_level
        feature_data["BMI"] = bmi
        feature_data["Daily meals frequency"] = daily_meals
        feature_data["Carbs"] = carbs
        feature_data["Proteins"] = proteins
        feature_data["Fats"] = fats
        feature_data["Calories"] = calories
        feature_data['Gender_Male'] = 1 if gender == "Male" else 0
        
        # All possible diet types (based on training)
        diet_type_columns = [
            'diet_type_Keto',
            'diet_type_Low-Carb',
            'diet_type_Paleo',
            'diet_type_Vegan',
            'diet_type_Vegetarian'
        ]

        # Initialize all as 0
        for col in diet_type_columns:
            feature_data[col] = 0

        # If user input matches any known category, set that one to 1
        matched_col = f'diet_type_{diet_type}'
        if matched_col in diet_type_columns:
            feature_data[matched_col] = 1

        
        # Make predictions
        input_df = pd.DataFrame([feature_data])
        
        if model is not None:
            predictions = model.predict(input_df)
            predictions = ((predictions[0] - 1) / 3) * 5

            #st.markdown("---")
            st.markdown("### 📊 Prediction Results")
            result_col1, result_col2= st.columns(2)
                
            with result_col1:
                st.metric("🤖 AI Overall Rating", f"{predictions:.3f}/5")  
                
            with result_col2:
                st.text("⭐" * int(predictions))