import streamlit as st 
import joblib
import os
import numpy as np

attrib_info = """
### Attribute Information:
    - Pregnancies
	- Glucose
	- BloodPressure
	- SkinThickness
	- Insulin
	- BMI
	- DiabetesPedigreeFunction
	- Age
	- Outcome
"""

["Pregnancies","Glucose","BloodPressure","SkinThickness",
 "Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"]


def get_fvalue(val):
	feature_dict = {"No":0,"Yes":1}
	for key,value in feature_dict.items():
		if val == key:
			return value 

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 



# Load ML Models
@st.cache_data
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def run_ml_app():
	st.subheader("Machine Learning Section")
	loaded_model = load_model("log_model.sav")

	with st.expander("Attributes Info"):
		st.markdown(attrib_info,unsafe_allow_html=True)

	# Layout
	col1,col2 = st.columns(2)

	with col1:
		Pregnancies = st.number_input("Pregnancies",0,20)
		Glucose = st.number_input("Glucose",0,200)
		BloodPressure = st.number_input("BloodPressure",0,150)
		SkinThickness = st.number_input("SkinThickness",0,100)
		
	
	with col2:
		Insulin = st.number_input("Insulin",0,1000)
		BMI = st.number_input("BMI",0,70)
		# DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction",min_value=0.0, max_value=3.0,step=0.01,format="%.2f")
		DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction",0,3,)
		Age = st.number_input("Age",20,90)
		
        



	with st.expander("Your Selected Options"):
		result = {
		'Pregnancies':Pregnancies,
		'Glucose':Glucose,
		'BloodPressure':BloodPressure,
		'SkinThickness':SkinThickness,
		'Insulin':Insulin,
		'BMI':BMI,
		'DiabetesPedigreeFunction':DiabetesPedigreeFunction,
		'Age':Age}
		st.write(result)
		encoded_result = []
		for i in result.values():
				encoded_result.append(i)


		# st.write(encoded_result)
	with st.expander("Prediction Results"):
		single_sample = np.array(encoded_result).reshape(1,-1)

		
		prediction = loaded_model.predict(single_sample)
		pred_prob = loaded_model.predict_proba(single_sample)
		st.write(prediction)
		if prediction == 1:
			st.warning("Positive Risk-{}".format(prediction[0]))
			pred_probability_score = {"Negative DM":pred_prob[0][0]*100,"Positive DM":pred_prob[0][1]*100}
			st.subheader("Prediction Probability Score")
			st.json(pred_probability_score)
		else:
			st.success("Negative Risk-{}".format(prediction[0]))
			pred_probability_score = {"Negative DM":pred_prob[0][0]*100,"Positive DM":pred_prob[0][1]*100}
			st.subheader("Prediction Probability Score")
			st.json(pred_probability_score)

