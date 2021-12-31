import streamlit as st

st.title("Hello World My First Streamlit Project is Up")
st.header("This is the first header")
st.text("Hello Darkness my dear friend")
st.text_area(label="Input Log File")

st.markdown("### This is a streamlit markdown")


st.success('Successful')
st.info("Information Provided")
st.warning("Warning Heeded")
st.error("Error caught")
st.help(range)

########## Streamlit Widgets Tutorials #############

# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
	st.success("You are Active")
else:
	st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","DataScientist","Doctor","Businessman"])
st.write("You selected this option ",occupation)


# MultiSelect
location = st.multiselect("Where do you work?",("London","New York","Accra","Kiev","Nepal"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)


# Buttons
st.button("Simple Button")

if st.button("About"):
	st.text("Streamlit is Cool")

######################################

# Receiving User Text Input
firstname = st.text_input("Enter Your Firstname","Type Here..")
if st.button("Submit"):
	result = firstname.title()
	st.success(result)


# Text Area
message = st.text_area("Enter Your message","Type Here..")
if st.button("Submit Data"):
	result = message.title()
	st.success(result)

# Date Input
import datetime
today = st.date_input("Today is",datetime.datetime.now())
st.success(today)


# Time
the_time = st.time_input("The time is",datetime.time())

st.write(range(10))

# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")
st.sidebar.write("Hello Side bar can we write you")

if st.sidebar.button("Sidebar Button"):
    st.success("We can see the success of sidebar button")

# Displaying JSON
st.text("Display JSON")
st.json({'name': "Jesse", 'gender': "male"})

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting .."):
     time.sleep(5)
     st.success("Finished!")

# Balloons
st.balloons()




