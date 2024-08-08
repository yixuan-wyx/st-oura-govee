import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import plotly.express as px

def visualize_readiness_scores(data):
    # Create a line chart for readiness scores with data points
    fig = px.line(data, x='day', y='score', title='Readiness Score Over Time', markers=True)

    fig.update_layout(
        xaxis_title='Day',
        yaxis_title='Readiness Score',
        legend_title='Metric'
    )

    return fig

def visualize_activity_log(data):
    # Count the occurrences of each activity per day
    activity_count = data.groupby(['day', 'activity']).size().unstack(fill_value=0).reset_index()

    # Melt the dataframe for easier plotting with Plotly
    activity_count_melted = activity_count.melt(id_vars=['day'], var_name='activity', value_name='count')

    # Create a bar chart for activity categories
    fig = px.bar(activity_count_melted, x='day', y='count', color='activity', title='Activity Log')

    fig.update_layout(
        xaxis_title='Day',
        yaxis_title='Count',
        legend_title='Activity'
    )

    return fig

def visualize_sleep_scores(data):
    # Create a line chart for sleep scores
    fig = px.line(data, x='day', y='score', title='Sleep Score Over Time', markers=True)

    fig.update_layout(
        xaxis_title='Day',
        yaxis_title='Sleep Score',
        legend_title='Metric'
    )

    return fig

def visualize_respiratory(data):
    # Group and average the data by day
    df = data[["day", "average_breath"]].groupby('day').mean().reset_index()
    fig = go.Figure()

    # Add a line plot for respiratory rates
    fig.add_trace(go.Scatter(
        x=df["day"],
        y=df["average_breath"],
        name='Respiratory Rate',
        mode='lines+markers',
        # line=dict(color='lightblue')
    ))

    fig.update_layout(
        title='Average Respiratory Rate',
        xaxis_title='Day',
        yaxis_title='Count/minute',
        legend_title='Metric'
    )

    return fig

def visualize_daily_heart_rate(df):
    # Convert the timestamp column to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    # Calculate the average bpm for each source for each date
    df_daily_avg = df.groupby(['date', 'source'], as_index=False).agg({'bpm': 'mean'})

    fig = px.line(df_daily_avg, x='date', y='bpm', color='source', title='Daily Average Heart Rate Chart', markers=True)
    
    return fig

def visualize_spo2(data):
    # Group and average the data by day
    df = data[["day", "spo2_percentage"]].groupby('day').mean().reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["day"],
        y=df["spo2_percentage"],
        name='Spo2',
        mode='lines+markers',
        line=dict(color='lightblue')
    ))

    fig.update_layout(
        title='Average Spo2 percentage',
        xaxis_title='Day',
        yaxis_title='Percentage',
        legend_title='Metric'
    )

    return fig

def visualize_temperature(data):
    # Group and average the data by day
    df = data[["day", "temperature_deviation"]].groupby('day').mean().reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["day"],
        y=df["temperature_deviation"],
        name='Temperature Deviation',
        mode='lines+markers',
        # line=dict(color='lightblue')
    ))

    fig.update_layout(
        title='Average temperature deviation',
        xaxis_title='Day',
        yaxis_title='Degrees Celsius',
        legend_title='Metric'
    )

    return fig

def visualize_daily_hrv(df):
    # Group and average the data by day
    data = df[["day", "average_hrv"]].groupby('day').mean().reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["day"],
        y=data["average_hrv"],
        name='Average HRV',
        mode='lines+markers',
        # line=dict(color='green')
    ))

    fig.update_layout(
        title='Daily Average HRV',
        xaxis_title='Day',
        yaxis_title='HRV',
        barmode='group',
        legend_title='Metric'
    )

    return fig

def visualize_daily_sleep_time(df):
    # Group and average the data by day
    data = df[["day", "total_sleep_duration"]].groupby('day').sum().reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["day"],
        y=data["total_sleep_duration"]/3600,
        name='Daily Total Sleep Duration',
        mode='lines+markers',
        # line=dict(color='green')
    ))

    fig.update_layout(
        title='Daily Total Sleep Duration',
        xaxis_title='Day',
        yaxis_title='Sleep Duration (Unit: hours)',
        barmode='group',
        legend_title='Metric'
    )

    return fig


def visualize_daily_lowest_hr(df):
    # Group and average the data by day
    data = df[["day", "lowest_heart_rate"]].groupby('day').min().reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["day"],
        y=data["lowest_heart_rate"],
        name='Daily Lowest Heart Rate',
        mode='lines+markers',
        # line=dict(color='green')
    ))

    fig.update_layout(
        title='Daily Lowest Heart Rate During Sleep',
        xaxis_title='Day',
        yaxis_title='Beat Per Minute',
        barmode='group',
        legend_title='Metric'
    )

    return fig

def visualize_daily_steps(df):
    # Group and average the data by day
    data = df[["day", "steps"]].groupby('day').sum().reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["day"],
        y=data["steps"],
        name='Daily Total Steps Count',
        mode='lines+markers',
        # line=dict(color='green')
    ))

    fig.update_layout(
        title='Daily Total Steps',
        xaxis_title='Day',
        yaxis_title='Steps',
        barmode='group',
        legend_title='Metric'
    )

    return fig

def visualize_heart_rate(df):
    # Group and average the data by day
    data = df[["day", "average_heart_rate", "lowest_heart_rate", "average_hrv"]].groupby('day').mean().reset_index()
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data["day"],
        y=data["average_heart_rate"],
        name='Average Heart Rate',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=data["day"],
        y=data["lowest_heart_rate"],
        name='Lowest Heart Rate',
        marker_color='lightblue'
    ))

    fig.add_trace(go.Scatter(
        x=data["day"],
        y=data["average_hrv"],
        name='Average HRV',
        mode='lines+markers',
        line=dict(color='green')
    ))

    fig.update_layout(
        title='Heart Rate Data Analysis',
        xaxis_title='Day',
        yaxis_title='Heart Rate (BPM)',
        barmode='group',
        legend_title='Metric'
    )

    return fig

def convert_to_datetime(time_str):
    return datetime.fromisoformat(time_str)

def visualize_sleep_start_end(df):
    df_start = pd.DataFrame({
        'Day': df["day"],
        'Time': df["bedtime_start"].apply(convert_to_datetime),
        'Type': 'Start'
    })

    df_end = pd.DataFrame({
        'Day': df["day"],
        'Time': df["bedtime_end"].apply(convert_to_datetime),
        'Type': 'End'
    })

    new_df = pd.concat([df_start, df_end])
    new_df['Time'] = new_df['Time'].apply(lambda t: datetime(2000, 1, 1, t.hour, t.minute, t.second))

    fig = px.scatter(new_df, x='Time', y='Day', color='Type', title='Bedtime Start and End Times')

    fig.update_xaxes(
        tickmode='array',
        tickvals=[datetime(2000, 1, 1, hour) for hour in range(24)],
        ticktext=[f'{hour:02d}:00' for hour in range(24)]
    )

    return fig

def visualize_sleep_breakdowns(data):
    # Convert durations from seconds to hours
    data["deep_sleep_duration"] = data["deep_sleep_duration"] / 3600
    data["light_sleep_duration"] = data["light_sleep_duration"] / 3600
    data["rem_sleep_duration"] = data["rem_sleep_duration"] / 3600
    data["awake_time"] = data["awake_time"] / 3600

    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data["day"],
        y=data["deep_sleep_duration"],
        name='Deep Sleep',
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=data["day"],
        y=data["light_sleep_duration"],
        name='Light Sleep',
        marker_color='lightblue'
    ))
    fig.add_trace(go.Bar(
        x=data["day"],
        y=data["rem_sleep_duration"],
        name='REM Sleep',
        marker_color='orange'
    ))
    fig.add_trace(go.Bar(
        x=data["day"],
        y=data["awake_time"],
        name='Awake Time',
        marker_color='lightgray'
    ))

    # Add secondary y-axis for sleep efficiency
    fig.update_layout(
        yaxis=dict(title='Hours'),
        yaxis2=dict(title='Sleep Efficiency', overlaying='y', side='right', range=[0, 100])
    )

    # Add line trace for sleep efficiency
    fig.add_trace(go.Scatter(
        x=data["day"],
        y=data["efficiency"],
        name='Sleep Efficiency',
        yaxis='y2',
        mode='lines+markers',
        line=dict(color='green')
    ))

    fig.update_layout(
        barmode='stack',
        title='Sleep Duration and Efficiency Breakdown',
        xaxis_title='Day',
        legend_title='Sleep Types and Efficiency'
    )

    return fig


# flowsheet visualization
def visualize_temporal_flowsheet(df):
    # Ensure the columns are of the correct type
    df["RECORDED_DAY"] = pd.to_datetime(df["RECORDED_DAY"]).dt.date
    df["MEAS_VALUE"] = pd.to_numeric(df["MEAS_VALUE"], errors='coerce')
    
    # Group by "RECORDED_DAY" and "fdgDisplayName", and aggregate "MEAS_VALUE"
    df_grouped = df.groupby(["RECORDED_DAY", "fdgDisplayName"])["MEAS_VALUE"].mean().reset_index()
    
    # Create the line chart
    fig = px.line(df_grouped, x="RECORDED_DAY", y="MEAS_VALUE", color="fdgDisplayName",
                  title="Temporal Categorical Value Changes",
                  markers=True,
                  labels={"RECORDED_DAY": "Recorded Day", "MEAS_VALUE": "Mean Measure Value", "fdgDisplayName": "Category"})
    
    # Update layout for better visualization
    fig.update_layout(xaxis_title='Day',
                      yaxis_title='Mean Measure Value',
                      legend_title_text='Category')
    
    fig.show()

def visualize_individual_temporal_flowsheet(df):
    # Ensure the columns are of the correct type
    df["RECORDED_DAY"] = pd.to_datetime(df["RECORDED_DAY"]).dt.date
    df["MEAS_VALUE"] = pd.to_numeric(df["MEAS_VALUE"], errors='coerce')
    
    # Group by "RECORDED_DAY" and "fdgDisplayName", and aggregate "MEAS_VALUE"
    df_grouped = df.groupby(["RECORDED_DAY", "fdgDisplayName"])["MEAS_VALUE"].mean().reset_index()
    
    # Get the unique categories
    categories = df_grouped["fdgDisplayName"].unique()

    # Generate a line chart for each category
    for category in categories:
        df_category = df_grouped[df_grouped["fdgDisplayName"] == category]
        
        fig = px.line(df_category, x="RECORDED_DAY", y="MEAS_VALUE",
                      title=f"Temporal Changes for {category}",
                      markers=True,
                      labels={"RECORDED_DAY": "Recorded Day", "MEAS_VALUE": "Mean Measure Value"})
        
        # Update layout for better visualization
        fig.update_layout(xaxis_title='Day',
                          yaxis_title='Mean Measure Value',
                          legend_title_text='Category')
        
        fig.show()


'''
Govee Plots
'''
def visualize_govee_temperature(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data['Timestamp'], 
        y=data['Temperature_Fahrenheit'], 
        mode='lines', 
        name='Temperature'
    ))
    fig.update_layout(
        title='Temperature Over Time',
        xaxis_title='Timestamp',
        yaxis_title='Temperature (°F)'
    )
    return fig

def visualize_govee_humidity(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data['Timestamp'], 
        y=data['Relative_Humidity'], 
        mode='lines', 
        name='Humidity'
    ))
    fig.update_layout(
        title='Relative Humidity Over Time',
        xaxis_title='Timestamp',
        yaxis_title='Humidity (%)'
    )
    return fig


def visualize_daily_average_temp_humidity(data):
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data['date'] = data['Timestamp'].dt.date

    daily_avg = data.groupby('date').agg({
        'Temperature_Fahrenheit': 'mean',
        'Relative_Humidity': 'mean'
    }).reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=daily_avg['date'], 
        y=daily_avg['Temperature_Fahrenheit'], 
        mode='lines+markers', 
        name='Temperature',
        yaxis='y1'
    ))

    # Add humidity trace
    fig.add_trace(go.Scatter(
        x=daily_avg['date'], 
        y=daily_avg['Relative_Humidity'], 
        mode='lines+markers', 
        name='Humidity',
        yaxis='y2'
    ))

    # Update layout for dual y-axes
    fig.update_layout(
        title='Daily Average Temperature and Humidity',
        xaxis_title='Date',
        yaxis=dict(
            title='Temperature (°F)',
            side='left'
        ),
        yaxis2=dict(
            title='Humidity (%)',
            overlaying='y',
            side='right'
        )
    )

    return fig


'''
NOAA Plots
'''
def visualize_noaa_temperature(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data['date'], 
        y=data['temp_min'], 
        mode='lines', 
        name='Daily Low',
        line=dict(color='lightgreen')
    ))
    fig.add_trace(go.Scatter(
        x=data['date'], 
        y=data['temp_max'], 
        mode='lines', 
        name='Daily High',
        line=dict(color='salmon')
    ))
    fig.update_layout(
        title='NYC Outdoor Temperature Over Time',
        xaxis_title='Date',
        yaxis_title='Temperature (°F)'
    )
    return fig

'''
combined
'''
def visualize_combined_temperature(govee_data, noaa_data):
    govee_data['Timestamp'] = pd.to_datetime(govee_data['Timestamp'])
    govee_data['date'] = govee_data['Timestamp'].dt.date
    noaa_data['date'] = pd.to_datetime(noaa_data['date']).dt.date

    # Calculate daily average for Govee data
    daily_avg_govee = govee_data.groupby('date').agg({
        'Temperature_Fahrenheit': 'mean'
    }).reset_index()

    fig = go.Figure()

    # Add indoor temperature trace
    fig.add_trace(go.Scatter(
        x=daily_avg_govee['date'], 
        y=daily_avg_govee['Temperature_Fahrenheit'], 
        mode='lines+markers', 
        name='Indoor Temperature',
        line=dict(color='blue')
    ))

    # Add outdoor daily low temperature trace
    fig.add_trace(go.Scatter(
        x=noaa_data['date'], 
        y=noaa_data['temp_min'], 
        mode='lines', 
        name='Outdoor Daily Low',
        line=dict(color='lightgreen')
    ))

    # Add outdoor daily high temperature trace
    fig.add_trace(go.Scatter(
        x=noaa_data['date'], 
        y=noaa_data['temp_max'], 
        mode='lines', 
        name='Outdoor Daily High',
        line=dict(color='salmon')
    ))

    fig.update_layout(
        title='Indoor vs Outdoor Temperature Over Time',
        xaxis_title='Date',
        yaxis_title='Temperature (°F)',
        legend=dict(
            x=1,
            y=1.1,
            xanchor='right',
            yanchor='top'
        ),
        margin=dict(t=100)
    )

    return fig