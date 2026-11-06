import streamlit as st

st.title("my first page")
st.write("this is my first page in python")


import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page content
st.title("Student Performance Dashboard")
st.write("This dashboard shows sample data about student marks.")

# Create sample data
# Marks of 5 students over 3 tests

data = {
    "Test 1": [65, 70, 80, 75, 90],
    "Test 2": [68, 72, 78, 80, 92],
    "Test 3": [70, 75, 82, 85, 95]
}

# Convert data into a DataFrame
df = pd.DataFrame(
    data,
    index=[
        "Student A",
        "Student B",
        "Student C",
        "Student D",
        "Student E"
    ]
)

# Display the DataFrame
st.subheader("Marks Data")
st.dataframe(df)

# Display a line chart
st.subheader("Performance Trend (Line Chart)")
st.line_chart(df.T)


import streamlit as st

st.title("Student Performance Dashboard")
st.success("Data loaded successfully.")
st.warning("Some records contain missing values.")
st.error("Failed to connect to the database.")
st.info("Analysis is in progress.")



import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Media Files Demo",
    page_icon="🎬",
    layout="wide"
)

# Application Title
st.title("🎬 Display Elements – Media Files")

st.write(
    "This application demonstrates how to display and interact "
    "with images, audio, and video files using Streamlit."
)

st.divider()

# ------------------------------------------------
# 1. Display Image using st.image()
# ------------------------------------------------

st.header("1. Display Image")

st.image(
    "https://picsum.photos/800/400",
    caption="Sample Image",
    use_container_width=True
)

st.divider()

# ------------------------------------------------
# 2. Display Multiple Images
# ------------------------------------------------

st.header("2. Display Multiple Images")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://picsum.photos/id/1015/300/200",
        caption="Mountain"
    )

with col2:
    st.image(
        "https://picsum.photos/id/1016/300/200",
        caption="Forest"
    )

with col3:
    st.image(
        "https://picsum.photos/id/1018/300/200",
        caption="Nature"
    )

st.divider()

# ------------------------------------------------
# 3. Play Audio using st.audio()
# ------------------------------------------------

st.header("3. Play Audio")

audio_url = (
    "https://www.soundhelix.com/examples/mp3/"
    "SoundHelix-Song-1.mp3"
)

st.audio(audio_url, format="audio/mp3")

st.divider()

# ------------------------------------------------
# 4. Play Video using st.video()
# ------------------------------------------------

st.header("4. Play Video")

video_url = (
    "https://www.w3schools.com/html/"
    "mov_bbb.mp4"
)

st.video(video_url)

st.divider()

# ------------------------------------------------
# 5. Display Media from URLs
# ------------------------------------------------

st.header("5. Media from URLs")

st.subheader("Display Image from URL")

image_url = st.text_input(
    "Enter Image URL:",
    "https://picsum.photos/600/300"
)

if image_url:
    st.image(image_url, caption="Image from URL")

st.subheader("Play Audio from URL")

audio_input = st.text_input(
    "Enter Audio URL:",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
)

if audio_input:
    st.audio(audio_input)

st.subheader("Play Video from URL")

video_input = st.text_input(
    "Enter Video URL:",
    "https://www.w3schools.com/html/mov_bbb.mp4"
)

if video_input:
    st.video(video_input)

st.success("Media Files Demonstration Completed!")


import streamlit as st
import pandas as pd
from datetime import date, time

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Streamlit Widgets Demo",
    page_icon="🎯",
    layout="wide"
)

st.title("Streamlit Widgets Demonstration")
st.write("Learn different input, action, and display widgets in Streamlit.")

st.divider()


# ==========================================
# PART 1: TEXT AND INPUT WIDGETS
# ==========================================

st.header("1. Text and Input Widgets")

# 1. Text Input
st.subheader("1. st.text_input()")

name = st.text_input("Enter your name:")

st.write("Your Name:", name)


# 2. Text Area
st.subheader("2. st.text_area()")

description = st.text_area("Enter your description:")

st.write("Description:", description)


# 3. Number Input
st.subheader("3. st.number_input()")

age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=100,
    value=25
)

st.write("Your Age:", age)


# 4. Date Input
st.subheader("4. st.date_input()")

selected_date = st.date_input(
    "Select your date:",
    value=date.today()
)

st.write("Selected Date:", selected_date)


# 5. Time Input
st.subheader("5. st.time_input()")

selected_time = st.time_input(
    "Select your time:",
    value=time(10, 30)
)

st.write("Selected Time:", selected_time)


st.divider()


# ==========================================
# PART 2: ACTION WIDGETS
# ==========================================

st.header("2. Action Widgets")


# 1. Button
st.subheader("1. st.button()")

if st.button("Click Me"):
    st.success("Button Clicked Successfully!")


# 2. Slider
st.subheader("2. st.slider()")

marks = st.slider(
    "Select your marks:",
    min_value=0,
    max_value=100,
    value=50
)

st.write("Your Marks:", marks)


# 3. Select Slider
st.subheader("3. st.select_slider()")

rating = st.select_slider(
    "Select your performance:",
    options=["Poor", "Average", "Good", "Excellent"]
)

st.write("Your Performance:", rating)


# 4. Selectbox
st.subheader("4. st.selectbox()")

course = st.selectbox(
    "Select your course:",
    ["Python", "Data Science", "Artificial Intelligence", "Machine Learning"]
)

st.write("Selected Course:", course)


# 5. Radio Button
st.subheader("5. st.radio()")

gender = st.radio(
    "Select your gender:",
    ["Male", "Female", "Other"]
)

st.write("Selected Option:", gender)


# 6. Checkbox
st.subheader("6. st.checkbox()")

show_data = st.checkbox("Show Student Information")

if show_data:
    st.info("Student Name: Rahul")
    st.info("Course: Python")
    st.info("Age: 22")


# 7. Multiselect
st.subheader("7. st.multiselect()")

skills = st.multiselect(
    "Select your skills:",
    ["Python", "SQL", "Machine Learning", "Deep Learning", "Power BI"]
)

st.write("Selected Skills:", skills)


st.divider()


# ==========================================
# PART 3: DATA DISPLAY WIDGETS
# ==========================================

st.header("3. Data Display Widgets")


# Sample Dataset
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohit"],
    "Age": [22, 23, 24, 21, 25],
    "Course": ["Python", "AI", "ML", "Data Science", "Python"],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)


# 1. Dataframe
st.subheader("1. st.dataframe()")

st.write("Interactive Dataset:")

st.dataframe(df, use_container_width=True)


# 2. Table
st.subheader("2. st.table()")

st.write("Static Dataset:")

st.table(df)


# 3. Metric
st.subheader("3. st.metric()")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Total Students",
    value=5
)

col2.metric(
    label="Average Marks",
    value="87.2"
)

col3.metric(
    label="Highest Marks",
    value="95"
)


# 4. JSON
st.subheader("4. st.json()")

student = {
    "Name": "Rahul",
    "Age": 22,
    "Course": "Artificial Intelligence",
    "Skills": ["Python", "SQL", "Machine Learning"],
    "Passed": True
}

st.json(student)


# 5. Write
st.subheader("5. st.write()")

st.write("Welcome to Streamlit!")

st.write("Student Dataset:", df)

st.write("Student Names:", df["Name"])

st.write("Average Marks:", df["Marks"].mean())


st.divider()

st.success("All Streamlit Widgets Demonstrated Successfully!")




import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page content
st.title("Student Performance Dashboard")
st.write("This dashboard shows sample data about student marks.")

# Create sample data
# Marks of 5 students over 3 tests

data = {
    "Test 1": [65, 70, 80, 75, 90],
    "Test 2": [68, 72, 78, 80, 92],
    "Test 3": [70, 75, 82, 85, 95]
}

# Convert data into a DataFrame
df = pd.DataFrame(
    data,
    index=[
        "Student A",
        "Student B",
        "Student C",
        "Student D",
        "Student E"
    ]
)

# Display the DataFrame
st.subheader("Marks Data")
st.dataframe(df)

# Display a line chart
st.subheader("Performance Trend (bar Chart)")
st.bar_chart(df.T)






import streamlit as st
import matplotlib.pyplot as plt

# Page Title
st.title("Student Performance Dashboard")

st.header("Scatterplot Chart")

st.write("Student Performance vs. Study Hours")

# Sample Data
study_hours = [1, 2, 2.5, 3, 3.5, 4, 5, 6, 6.5, 7]

exam_scores = [40, 50, 55, 60, 62, 65, 70, 78, 80, 85]

# Create the Plot
fig, ax = plt.subplots()

ax.scatter(
    study_hours,
    exam_scores,
    color='green'
)

# Chart Title
ax.set_title("Study Hours vs Exam Score")

# X-axis Label
ax.set_xlabel("Study Hours")

# Y-axis Label
ax.set_ylabel("Exam Score (%)")

# Display Chart in Streamlit
st.pyplot(fig)





import streamlit as st
import matplotlib.pyplot as plt

# Page Title
st.title("Student Performance Dashboard")

st.header("Scatterplot Chart")

st.write("Student Performance vs. Study Hours")

# Sample Data
study_hours = [1, 2, 2.5, 3, 3.5, 4, 5, 6, 6.5, 7]

exam_scores = [40, 50, 55, 60, 62, 65, 70, 78, 80, 85]

# Create the Plot
fig, ax = plt.subplots()

ax.scatter(
    study_hours,
    exam_scores,
    color='green'
)

# Chart Title
ax.set_title("Study Hours vs Exam Score")

# X-axis Label
ax.set_xlabel("Study Hours")

# Y-axis Label
ax.set_ylabel("Exam Score (%)")

# Display Chart in Streamlit
st.pyplot(fig)





import streamlit as st
import matplotlib.pyplot as plt

# Page Title
st.title("Student Performance Dashboard")

st.header("Scatterplot Chart")

st.write("Student Performance vs. Study Hours")

# Sample Data
study_hours = [1, 2, 2.5, 3, 3.5, 4, 5, 6, 6.5, 7]

exam_scores = [40, 50, 55, 60, 62, 65, 70, 78, 80, 85]

# Create the Plot
fig, ax = plt.subplots()

# Scatter Plot
ax.scatter(
    study_hours,
    exam_scores,
    color='green',
    label='Student Scores'
)

# Add Trend Line
ax.plot(
    study_hours,
    exam_scores,
    color='red',
    linestyle='-',
    marker='',
    label='Grade Line'
)

# Chart Title
ax.set_title("Study Hours vs Exam Score")

# X-axis Label
ax.set_xlabel("Study Hours")

# Y-axis Label
ax.set_ylabel("Exam Score (%)")

# Show Legend
ax.legend()

# Display Chart in Streamlit
st.pyplot(fig)





#lab 1. interactive lris Flower Classification Interface
 #create file app.py

        #Import Libraries 
import streamlit as st 
import pandas as pd 
from sklearn.datasets import load_iris 
from sklearn.linear_model import LogisticRegression 
      # Load Dataset 
iris = load_iris() 
X = iris.data 
y = iris.target 

#  Train the Model 
model = LogisticRegression(max_iter=200) 
model.fit(X, y) 
# Create User Interface 
st.title("Iris Flower Classification") 
st.write("Enter the flower measurements:") 
#  Add Input Widgets 
# Text Inputs 
sepal_length = st.text_input("Sepal Length (cm)", "5.1") 
sepal_width = st.text_input("Sepal Width (cm)", "3.5") 
# Selection Widgets (Dropdown / Slider) 
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4) 
petal_width = st.selectbox("Petal Width (cm)", [0.1, 0.2, 0.5, 1.0, 1.5, 2.0]) 
#  Prepare Input Data 
input_data = pd.DataFrame({ 
"sepal length (cm)": [float(sepal_length)], 
"sepal width (cm)": [float(sepal_width)], 
"petal length (cm)": [petal_length], 
"petal width (cm)": [petal_width] 
}) 
# Make Prediction 
prediction = model.predict(input_data) 
species = iris.target_names[prediction[0]] 
# Display Output 
st.subheader("Prediction Result") 
st.success(f"The predicted flower species is: {species}")






#lab 2. predictive interface for Housing Price Estimation
#create app.py file
# Import Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load Dataset
data = pd.read_csv("Bengaluru_House_Data.csv")

# Data Preprocessing

# Drop missing values
data = data.dropna()

# Convert total_sqft to numeric
def convert_sqft(x):
    try:
        if '-' in str(x):
            nums = x.split('-')
            return (float(nums[0]) + float(nums[1])) / 2
        return float(x)
    except:
        return None

data['total_sqft'] = data['total_sqft'].apply(convert_sqft)
data = data.dropna()

# Extract BHK from size column
data['bhk'] = data['size'].str.extract(r'(\d+)').astype(int)

# Select relevant features
data = data[['total_sqft', 'bath', 'bhk', 'price']]
data.columns = ['Area', 'Bathrooms', 'Bedrooms', 'Price']

# Prepare Data
X = data[['Area', 'Bedrooms', 'Bathrooms']]
y = data['Price']

# Train Regression Model
model = LinearRegression()
model.fit(X, y)

# Create User Interface
st.title("Bengaluru Housing Price Prediction")
st.write("Enter property details to estimate price.")

# Input Widgets
area = st.number_input("Area (sq. ft)", 500, 10000, 1000)

bedrooms = st.selectbox(
    "Bedrooms (BHK)",
    [1, 2, 3, 4, 5]
)

bathrooms = st.selectbox(
    "Bathrooms",
    [1, 2, 3, 4]
)

# Prediction
input_data = pd.DataFrame(
    [[area, bedrooms, bathrooms]],
    columns=['Area', 'Bedrooms', 'Bathrooms']
)

prediction = model.predict(input_data)[0]

# Display Result
st.subheader("Predicted Price")
st.success(f"Estimated Price: ₹ {prediction:.2f} Lakhs")

# Visualization
st.subheader("Prediction Visualization")

fig, ax = plt.subplots()
ax.bar(["Predicted Price"], [prediction])
ax.set_ylabel("Price (Lakhs)")
st.pyplot(fig)





#lab 3. interactive Visualization and Analysis of Covid-19 Data
#create app.py file
# Import Libraries
# Import Libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Load Dataset
data = pd.read_csv("covid_19_india.csv")
st.write("Dataset Preview", data.head())

# Data Preprocessing

# Convert Date column
data['Date'] = pd.to_datetime(
    data['Date'],
    format='%Y/%m/%d',
    errors='coerce'
)

# Rename columns for easy use
data = data.rename(columns={
    'State/UT': 'State',
    'State/UnionTerritory': 'State',
    'Cured': 'Recovered'
})

# Drop missing values
data = data.dropna(subset=['Date', 'State'])

# Calculate Active cases if not present
if 'Active' not in data.columns:
    data['Active'] = (
        data['Confirmed'] -
        data['Recovered'] -
        data['Deaths']
    )

# Create Interactive UI
st.title("COVID-19 India Dashboard")

# State Filter
states = sorted(data['State'].unique())

selected_state = st.selectbox(
    "Select State/UT",
    states
)

# Date Filter
start_date = st.date_input(
    "Start Date",
    data['Date'].min().date()
)

end_date = st.date_input(
    "End Date",
    data['Date'].max().date()
)

# Filter Data
filtered_data = data[
    (data['State'] == selected_state) &
    (data['Date'] >= pd.to_datetime(start_date)) &
    (data['Date'] <= pd.to_datetime(end_date))
].sort_values('Date')

# Check Data
if filtered_data.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# Line Chart (Trend Analysis)
fig = px.line(
    filtered_data,
    x='Date',
    y=['Confirmed', 'Active', 'Recovered', 'Deaths'],
    title=f"COVID-19 Trends in {selected_state}"
)

st.plotly_chart(fig)

# Bar Chart (Latest Status)
latest_data = filtered_data.iloc[-1]

fig_bar = px.bar(
    x=['Confirmed', 'Active', 'Recovered', 'Deaths'],
    y=[
        latest_data['Confirmed'],
        latest_data['Active'],
        latest_data['Recovered'],
        latest_data['Deaths']
    ],
    title="Latest COVID-19 Status"
)

st.plotly_chart(fig_bar)

# Display Key Metrics
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Confirmed",
        int(latest_data['Confirmed'])
    )

with col2:
    st.metric(
        "Active",
        int(latest_data['Active'])
    )

with col3:
    st.metric(
        "Recovered",
        int(latest_data['Recovered'])
    )

with col4:
    st.metric(
        "Deaths",
        int(latest_data['Deaths'])
    )

# Calculate Recovery and Mortality Rates
confirmed = latest_data['Confirmed']

if confirmed > 0:
    recovery_rate = (
        latest_data['Recovered'] / confirmed
    ) * 100

    mortality_rate = (
        latest_data['Deaths'] / confirmed
    ) * 100
else:
    recovery_rate = 0
    mortality_rate = 0

st.metric(
    "Recovery Rate (%)",
    round(recovery_rate, 2)
)

st.metric(
    "Mortality Rate (%)",
    round(mortality_rate, 2)
)






