import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 

@st.cache_data
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_eda_app():
	st.subheader("EDA Section")
	df = load_data("data/diabetes.csv")

	submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		
		st.dataframe(df)

		with st.expander("Data Types Summary"):
			st.dataframe(df.dtypes)

		with st.expander("Descriptive Summary"):
			st.dataframe(df.describe())

		with st.expander("Diabetes Distribution"):
			st.dataframe(df['Pregnancies'].value_counts())

		with st.expander("Class Distribution"):
			st.dataframe(df['Outcome'].value_counts())
	else:
		st.subheader("Plots")

		# Layouts
		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Dist Plot of Diabetes"):
				# fig = plt.figure()
				# sns.countplot(df['Diabetes'])
				# st.pyplot(fig)

				gen_df = df['Outcome'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Diabetes Type','Counts']
				# st.dataframe(gen_df)
				p01 = px.pie(gen_df,names='Diabetes Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

			with st.expander("Dist Plot of Class"):
				fig = plt.figure()
				sns.histplot(df['Pregnancies'])
				st.pyplot(fig)





		with col2:
			with st.expander("Diabetes Distribution"):
				st.dataframe(df['Outcome'].value_counts())

			with st.expander("Class Distribution"):
				st.dataframe(df['Glucose'].value_counts())
			

		with st.expander("Frequency Dist Plot of Age"):
			# fig,ax = plt.subplots()
			# ax.bar(df['Age'],df['count'])
			# plt.ylabel('Counts')
			# plt.title('Frequency Count of Age')
			# plt.xticks(rotation=45)
			# st.pyplot(fig)

			p = px.bar(df,x='Age',y='Outcome')
			st.plotly_chart(p)

			p2 = px.scatter(df,x='Age',y='Insulin')
			st.plotly_chart(p2)

		with st.expander("Outlier Detection Plot"):
			# outlier_df = 
			fig = plt.figure()
			sns.boxplot(df['Age'])
			st.pyplot(fig)

			p3 = px.box(df,x='Age',color='Outcome')
			st.plotly_chart(p3)

		with st.expander("Correlation Plot"):
			corr_matrix = df.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)

			p3 = px.imshow(corr_matrix)
			st.plotly_chart(p3)


	



