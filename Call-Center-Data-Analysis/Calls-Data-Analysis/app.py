import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ------------------------------------------------------------------------------------------------------

colors = ["#264653","#006d77","#277da1","#90be6d","#f9c74f","#f9844a","#f94144","#ee964b","#5f0f40","#81c3d7",
          "#8fb339","#bf4342","#949c81","#3e503c"]
# --------------------------------------------------------------------------------------------------------

temp = """
<div style="background-color:{};padding:0.1px;border-radius:5px;">
<h4 style="color:{};text-align:center;display:in-line">{}</h6>
</div>
"""
# --------------------------------------Helper Functions------------------------------------------------

# for better dataframe ui
def get_chart(data):
    fig = go.Figure( data = [go.Table ( columnwidth=[2,2,2,2,2,2,2,2,2,2,2,2,2,2],header = dict(values = list(data.columns),
                               font=dict(size=12, color = 'white'),fill_color = '#264653',line_color = 'rgba(255,255,255,0.2)',
                               align = ['left','center'],height=40)
                           ,cells = dict(values = [data[K].tolist() for K in data.columns],font=dict(size=12 , color = "black"),
                                align = ['left','center'],line_color = 'rgba(255,255,255,0.2)',height=30))])
    fig.update_layout(title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=900 , width=1200)
    return fig

# Pre-processing data to count the occurrences of reports per month
def pre_process_data(frame):
    data = pd.DataFrame(frame.groupby("Month").value_counts())
    data.reset_index(inplace=True)
    data.columns = ["Month","Year","Count"]
    data = data.sort_values(by=['Month'], key=lambda x: x.map(month_order)).reset_index().drop(["index"],axis=1)
    return data

# Extracting out data by selected years
def refine_data(df,keys):
    for i in keys:
        df = df[df.Year!=i]
    return df

# line plot for trend analysis
def get_lineplot(data,X,Y,Z,labels_dict,order,xaxis,yaxis,legendTitle,width=None):
    fig = px.line(data_frame=data,x=X,y=Y,color=Z,labels=labels_dict,category_orders=order)
    fig.update_layout(legend_title=legendTitle,xaxis_title=xaxis,yaxis_title=yaxis,hovermode="x unified",
                      hoverlabel = dict(bgcolor="white",font_size=12,font_family="Rockwell"))
    return fig

month_order = {'January': 1, 'February': 2, 'March': 3,"April":4,"May":5,"June":6,"July":7,'August':8,
               "September":9,"October":10,"November":11,"December":12,"UN-specified":0}

months = ["January","February","March","April","May","June","July","August","September","October","November",
          "December"]
# --------------------------------GETTING DATA---------------------------------------------
data = pd.read_csv("Calls_Data.csv")


#------------------------------------------PAGE CONFIG-------------------------------------

st.set_page_config(page_title="NOPD Calls Analysis", layout="wide", page_icon="📈")

reduce_header_height_style = """
    <style>
        div.block-container {padding:1rem;overflow-x:hidden;}
        header {visibility:hidden;}
        body{width:100vw}
        div.plotly{align-items:centre;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)




# ---------------------------------------MAIN TITLE----------------------------------------
st.markdown(temp.format('#66999B','white' , "NOPD Calls for Service 2011-2022"),unsafe_allow_html=True)

years_list = [2011, 2012, 2013, 2014,2015,2016,2017,2018,2019,2020,2021,2022]

report_type = st.sidebar.selectbox(options = list(data.TypeText.unique()),label="Select Report Type")
options = st.sidebar.multiselect('Select Year',years_list,years_list)

# c1,c2 = st.columns((1,1))
# with c1:
#     # Report type select option
#     report_type = st.selectbox(options = list(data.TypeText.unique()),label="Select Report Type")
# with c2:
#     # Years select list
#     options = st.multiselect('Select Year',years_list,years_list)

frame = data[data.TypeText==report_type]
frame = frame.drop("TypeText",axis=1)
df = pre_process_data(frame)



keys = [i for i in years_list + options if i not in years_list or i not in options]
#----------------------------------------------------------------------------
data_set = refine_data(df,keys)

plot1 = go.Figure()
for i in options:
    plot1.add_trace(go.Scatter(x=months,y=df[df.Year==i].Count,mode="lines",legendgroup='group1',
                             showlegend=False,marker = {'color' : colors[years_list.index(i)]},name=i))

plot2 = go.Figure()
for i in options:
    y_vals=df[df.Year==i].sort_values(by=['Month'], key=lambda x: x.map(month_order))["Count"].cumsum(axis=0)
    plot2.add_trace(go.Scatter(x=months,y=y_vals,mode="lines",name=i,marker = {'color' : colors[years_list.index(i)]}))

matrix = data_set.pivot(index='Month', columns='Year', values='Count')
matrix.sort_index(key=lambda x: x.map(month_order),inplace=True)
matrix.reset_index(inplace=True)
plot3 = get_chart(matrix)

fig = make_subplots(rows=2, cols=2,shared_xaxes=True,vertical_spacing=0.17,
                     specs=[[{}, {}],[{"colspan": 2,"type":"table"}, None]],
                     subplot_titles=("Records per month(count per each month)", "Total Records per month(Cumulative)","Matrix View of Data"))


for t in plot1.data:
    fig.append_trace(t, row=1, col=1)
for t in plot2.data:
    fig.append_trace(t,row=1,col=2)
for t in plot3.data:
    fig.append_trace(t,row=2,col=1)
fig.update_layout(width=1000,autosize=False,height=800,legend_title="Year",hovermode="x unified",
                  hoverlabel = dict(bgcolor="white",font_size=8,font_family="Rockwell"))

st.plotly_chart(fig,use_container_width=True)
