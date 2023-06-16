import plotly.express as px
import plotly.graph_objects as go

colors = ["#264653","#2a9d8f","#77c1b7","#83c5be","#9fe5dd","#c7dce6","#57cc99","#006d77","#f4a261","#feeafa","#a4c3b2","#dee2ff","#949c81","#3e503c"]


def charts_update_layout(fig,xaxis=None,yaxis=None):
    fig.update_layout(
        hovermode="x unified" , yaxis_title = yaxis , xaxis_title = xaxis,
        hoverlabel = dict(bgcolor="black",font_size=16,font_family="Rockwell")
    )
    return fig


def get_speed_bracket_ratio(division_df):
    fig = px.pie(data_frame=division_df,
                 names= "Nature" ,values="Accidents Count",
                 color_discrete_sequence=["#006d77","#f4a261","#feeafa","#a4c3b2"]
                 )
    fig.update_layout(legend_title = "Speed Bracket")
    fig = charts_update_layout(fig)
    return fig


def get_SpeedBracket_analysis_plot(data):
    fig = go.Figure(data=[
        go.Bar(name="Accidents", y=data.Accidents, x=data.index ,
               marker_color=colors[0]),
        go.Bar(name="Casualities", y=data.Number_of_Casualties, x=data.index ,
               marker_color=colors[1])
    ])
    fig.update_layout(barmode='group')
    fig = charts_update_layout(fig,yaxis="Accidents",xaxis="Speed Bracket")
    return fig


def get_accidents_wrt_area_chart(division_df):
    fig = px.pie(data_frame=division_df,
                 names= "Area" ,values="Accidents Count",
                 color_discrete_sequence=["#006d77","#f4a261","#feeafa","#a4c3b2"]
                 )
    fig.update_layout(legend_title = "Area")
    fig = charts_update_layout(fig)
    fig.update_layout(width=500)
    return fig


def get_accidents_over_time_graph(df):
    fig = px.line(y = df["Accidents Count"],x = df["Date"],labels= {"y":"Accidents","x":"Date"},
                  color_discrete_sequence = ["#006d77","#f4a261","#feeafa","#a4c3b2"])
    fig = charts_update_layout(fig,"Time","Accidents")
    fig.update_layout(width=1200)
    return fig


def get_loc_based_accidents_info(df):
    fig = px.scatter_geo(df,lat="Latitude",lon="Longitude",hover_name="City",color = "Accidents")
    fig.update_geos(
        # center=dict(lon=df.Longitude.mean(), lat=df.Latitude.mean()),
        fitbounds="locations")
    fig.update_layout(height=500,width=600, margin={"r":0,"t":0,"l":0,"b":0},title="England Map")
    # fig.update_layout(width=500)
    return fig


def get_AreaNature_analysis_plot(data):
    fig = go.Figure(data=[
        go.Bar(name="Accidents", y=data.Accidents, x=data.index ,
               marker_color=colors[0]),
        go.Bar(name="Casualities", y=data.Number_of_Casualties, x=data.index ,
               marker_color=colors[1])
    ])
    fig.update_layout(barmode='group')
    fig = charts_update_layout(fig,yaxis="Accidents",xaxis="Area")
    fig.update_layout(width=600)
    return fig


def get_yearly_animation(df):
    fig = px.scatter(df, x="Casualities", y="Accidents",
                     animation_frame="Year",color_discrete_sequence=colors,
                     size="Vehicles", color="Casualities",
                     hover_name="City",
                     log_x=True,
                     )
    fig = charts_update_layout(fig,xaxis="Casualities",yaxis="Accidents")
    fig.update_layout(width=1200)
    return fig


def get_hours_days_comparison(df):
    fig = go.Figure(data=go.Heatmap(z=df.Accidents,y=df.Day,x=df.Hour,
                                    text=df.Accident_Severity,colorscale='viridis'))
    fig = charts_update_layout(fig,xaxis="Hour",yaxis="Day")
    fig.update_layout(width=600,height=500,legend_title="Accidents")
    return fig


def get_Accidents_bar_plot(data):
    fig = go.Figure(data=[
        go.Bar(name="Accidents", y=data.Accidents, x=data.index ,
               marker_color=colors[0]),
        go.Bar(name="Casualities", y=data.Number_of_Casualties, x=data.index ,
               marker_color=colors[1])
    ])
    fig.update_layout(barmode='group')
    fig.update_layout(width=1200)
    fig = charts_update_layout(fig,yaxis="Accidents",xaxis="Time")
    return fig


def get_accidents_severity_ratio(division_df):
    fig = px.pie(data_frame=division_df,
                 names= "Nature" ,values="Accidents Count",
                 color_discrete_sequence=["#006d77","#f4a261","#feeafa","#a4c3b2"]
                 )
    fig.update_layout(legend_title = "Nature")
    fig.update_layout(width=500)
    fig = charts_update_layout(fig)
    return fig


def get_road_type_ratio(division_df):
    fig = px.pie(data_frame=division_df,
                 names= "Nature" ,values="Accidents Count",
                 color_discrete_sequence=["#006d77","#f4a261","#feeafa","#a4c3b2"]
                 )
    fig.update_layout(legend_title = "Road Type")
    fig = charts_update_layout(fig)
    fig.update_layout(width=500)
    return fig


def get_RoadSurface_analysis_plot(data):
    fig = go.Figure(data=[
        go.Bar(name="Accidents", y=data.Accidents, x=data.index ,
               marker_color=colors[0]),
        go.Bar(name="Casualities", y=data.Number_of_Casualties, x=data.index ,
               marker_color=colors[1])
    ])
    fig.update_layout(barmode='group')
    fig.update_layout(width=600)
    fig = charts_update_layout(fig,yaxis="Accidents",xaxis="Road Surface")
    return fig


def get_weather_condition_ratio(division_df):
    fig = px.pie(data_frame=division_df,
                 names= "Nature" ,values="Accidents Count",
                 color_discrete_sequence=["#006d77","#f4a261","#feeafa","#a4c3b2"]
                 )
    fig.update_layout(legend_title = "Weather Condition")
    fig = charts_update_layout(fig)
    fig.update_layout(width=500)
    return fig


def get_WeatherCondition_analysis_plot(data):
    fig = go.Figure(data=[
        go.Bar(name="Accidents", y=data.Accidents, x=data.index ,
               marker_color=colors[0]),
        go.Bar(name="Casualities", y=data.Number_of_Casualties, x=data.index ,
               marker_color=colors[1])
    ])
    fig.update_layout(barmode='group')
    fig.update_layout(width=600)
    fig = charts_update_layout(fig,yaxis="Accidents",xaxis="Weather Conditions")
    return fig


def get_light_condition_ratio(division_df):
    fig = px.pie(data_frame=division_df,
                 names= "Nature" ,values="Accidents Count",
                 color_discrete_sequence=["#006d77","#f4a261","#feeafa","#a4c3b2"]
                 )
    fig.update_layout(legend_title = "Light Conditions")
    fig = charts_update_layout(fig)
    fig.update_layout(width=500)
    return fig


def get_LightCondition_analysis_plot(data):
    fig = go.Figure(data=[
        go.Bar(name="Accidents", y=data.Accidents, x=data.index ,
               marker_color=colors[0]),
        go.Bar(name="Casualities", y=data.Number_of_Casualties, x=data.index ,
               marker_color=colors[1])
    ])
    fig.update_layout(barmode='group')
    fig.update_layout(width=600)
    fig = charts_update_layout(fig,yaxis="Accidents",xaxis="Light Conditions")
    return fig


def get_speed_bracket_ratio(division_df):
    fig = px.pie(data_frame=division_df,
                 names= "Nature" ,values="Accidents Count",
                 color_discrete_sequence=["#006d77","#f4a261","#feeafa","#a4c3b2"]
                 )
    fig.update_layout(legend_title = "Speed Bracket")
    fig = charts_update_layout(fig)
    fig.update_layout(width=500)
    return fig


def get_SpeedBracket_analysis_plot(data):
    fig = go.Figure(data=[
        go.Bar(name="Accidents", y=data.Accidents, x=data.index ,
               marker_color=colors[0]),
        go.Bar(name="Casualities", y=data.Number_of_Casualties, x=data.index ,
               marker_color=colors[1])
    ])
    fig.update_layout(barmode='group')
    fig.update_layout(width=600)
    fig = charts_update_layout(fig,yaxis="Accidents",xaxis="Speed Bracket")
    return fig

