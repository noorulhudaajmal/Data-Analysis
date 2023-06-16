import streamlit as st
import pandas as pd
import plotly.express as px
from helpers import *
import plotly.graph_objects as go
from datetime import date
# from funcs import *

# ------------------------------------------------------------------------------------------------------

colors = ["#264653","#2a9d8f","#77c1b7","#83c5be","#9fe5dd","#c7dce6","#57cc99","#006d77","#f4a261","#feeafa","#a4c3b2","#dee2ff","#949c81","#3e503c"]

# --------------------------------------------------------------------------------------------------------

temp = """
<div style="background-color:{};padding:0.5px;border-radius:5px;">
<h4 style="color:{};text-align:center;display:in-line">{}</h6>
</div>
"""


#------------------------------------------PAGE CONFIG-------------------------------------

st.set_page_config(page_title="UK Accidents Data Analysis" ,layout="wide" )

st.write("# :bar_chart: When and Where Accidents Happened in UK?")
# ------------------------------------------------------------------------------------------
# data = pd.read_csv("Accident_Information.csv",low_memory=False)
# data = data[(data.Year == 2010)  | (data.Year == 2011) | (data.Year == 2012) | (data.Year == 2013)]
# data["DateTime"] = pd.to_datetime(data.Date)
# ------------------------------------------------------------------------------------------
st.markdown(temp.format('#66999B','white' , "QUICK SNAPSHOT OF ACCIDENTS OVER TIME PER LOCATION"),unsafe_allow_html=True)
st.write("")
accidents_wrt_time = pd.read_csv("accidents_wrt_time_and_loc.csv")
fatal = accidents_wrt_time[(accidents_wrt_time.Severity == "Serious")]
st.plotly_chart(get_yearly_animation(fatal))
# ------------------------------------------------------------------------------------------

st.markdown(temp.format('#66999B','white' , "Accidents Over Time"),unsafe_allow_html=True)
st.write("")

st.plotly_chart(get_accidents_over_time_graph(pd.read_csv("Accidents_wrt_Time.csv")))

# ------------------------------------------------------------------------------------------
col1, col2 = st.columns((1,1))
with col1:
    st.markdown(temp.format('#66999B','white' , "Accidents Based on various locations across England"),unsafe_allow_html=True)
    st.write("")

    st.plotly_chart(get_loc_based_accidents_info(pd.read_csv("Accidents_wrt_Loc.csv")))

    # ------------------------------------------------------------------------------------------
with col2:
    st.markdown(temp.format('#66999B','white' , "Accidents at different hours of day vs Week Day Analysis"),unsafe_allow_html=True)
    st.write("")

    st.plotly_chart(get_hours_days_comparison(pd.read_csv("day_vs_hour_data.csv")))

    # ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------

st.markdown(temp.format('#66999B','white' , "Accidents vs. Nature of Area"),unsafe_allow_html=True)
st.write("")
area1, area2 = st.columns((1,1))
with area1:
    st.plotly_chart(get_accidents_wrt_area_chart(pd.read_csv("Geo_Nature.csv")))
with area2:
    st.plotly_chart(get_AreaNature_analysis_plot(pd.read_csv("AreaNature_vs_accidents.csv",index_col=0)))
# ------------------------------------------------------------------------------------------

st.markdown(temp.format('#66999B','white' , "Casualties in Accidents over the Years"),unsafe_allow_html=True)
st.write("")
st.plotly_chart(get_Accidents_bar_plot(pd.read_csv('Accidents_vs_Casualities.csv',index_col=0)))

#-----------------------------------------------------------------------------------------------

st.write("# :bar_chart: FACTORS ANALYSIS")

# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------

st.markdown(temp.format('#66999B','white' , "Road Surface Conditions"),unsafe_allow_html=True)
st.write("")
area1, area2 = st.columns((1,1))
with area1:
    st.plotly_chart(get_road_type_ratio(pd.read_csv("Road_Surface_Div.csv")))
with area2:
    st.plotly_chart(get_RoadSurface_analysis_plot(pd.read_csv("RoadSurface_vs_accidents.csv",index_col=0)))
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------

st.markdown(temp.format('#66999B','white' , "Weather Conditions"),unsafe_allow_html=True)
st.write("")
area1, area2 = st.columns((1,1))
with area1:
    st.plotly_chart(get_weather_condition_ratio(pd.read_csv("Weather_Div.csv")))
with area2:
    st.plotly_chart(get_WeatherCondition_analysis_plot(pd.read_csv("WeatherCondition_vs_accidents.csv",index_col=0)))
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------

st.markdown(temp.format('#66999B','white' , "Light Conditions"),unsafe_allow_html=True)
st.write("")
area1, area2 = st.columns((1,1))
with area1:
    st.plotly_chart(get_light_condition_ratio(pd.read_csv("Light_Div.csv")))
with area2:
    st.plotly_chart(get_LightCondition_analysis_plot(pd.read_csv("LightConditions_vs_accidents.csv",index_col=0)))
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------

st.markdown(temp.format('#66999B','white' , "Speed Bracket"),unsafe_allow_html=True)
st.write("")
area1, area2 = st.columns((1,1))
with area1:
    st.plotly_chart(get_speed_bracket_ratio(pd.read_csv("Speed_Div.csv")))
with area2:
    st.plotly_chart(get_SpeedBracket_analysis_plot(pd.read_csv("SpeedBracket_vs_accidents.csv",index_col=0)))
# ------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------
