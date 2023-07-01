import streamlit as sl
import pandas

# sl.set_page_config(layout="wide")

# about me
col1, col2 = sl.columns(2)

with col1:
    sl.image("/Users/sanjheegupta/PycharmProjects/portfolioWebsite/images/me.jpg")

with col2:
    sl.title("Sanjhee Gupta")
    abt_me = "Hello! I am Sajhee, a sophomore studying Computer Science and Data Science at Pudrdue University"
    sl.info(abt_me)

# apps
sl.write("below are some of the apps I've created!")
cols3, empty_col, cols4 = sl.columns([1.5, 0.5, 1.5])
data = pandas.read_csv("/Users/sanjheegupta/PycharmProjects/portfolioWebsite/data.csv", sep=";")

with cols3:
    for index, row in data[:10].iterrows():
        sl.subheader(row["title"])
        sl.write(row["description"])
        # todo: add images for all projects
        #sl.image(row["image"])
        # todo: add links for all projects
        sl.write(f"[source code]({row['url']})")

with cols4:
    for index, row in data[10:].iterrows():
         sl.subheader(row["title"])
         sl.write(row["description"])
         # todo: add images for all projects
         #sl.image(row["image"])
         # todo: add links for all projects
         sl.write("[source code](https://pythonhow.com)")
