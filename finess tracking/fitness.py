import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the extended fitness dataset
extended_fitness_df = pd.read_csv("extended_fitness_data.csv")

# Define custom color palettes
scatter_palette = px.colors.qualitative.Plotly
bar_palette = px.colors.qualitative.Set1
hist_palette = px.colors.qualitative.Set2
paired_palette = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a']

# Initialize the Dash app
app = dash.Dash(__name__, title="Dashboarding_Project")

# Define the layout of the dashboard
app.layout = html.Div(style={'backgroundColor': '#1E1E1E', 'color': '#FFFFFF', 'fontFamily': 'Arial, sans-serif'}, children=[
    html.H1(children='Fitness Dashboard - Centurion University', style={'textAlign': 'center', 'color': '#61dafb'}),

    html.Div(children='''
        A comprehensive view of fitness data.
    ''', style={'textAlign': 'center', 'color': '#61dafb'}),

    # Scatter plot of BMI vs Workout Hours
    dcc.Graph(
        id='scatter-bmi-vs-hours',
        figure=px.scatter(
            extended_fitness_df,
            x='Workout_Hours',
            y='BMI',
            color='Gender',
            size='Calories_Burned',
            labels={'BMI': 'Body Mass Index', 'Workout_Hours': 'Workout Hours'},
            title='BMI vs Workout Hours',
            color_discrete_sequence=scatter_palette,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),

    # Bar chart of Average Workout Hours by Gender
    dcc.Graph(
        id='bar-average-hours',
        figure=px.bar(
            extended_fitness_df,
            x='Gender',
            y='Workout_Hours',
            color='Gender',
            labels={'Workout_Hours': 'Average Workout Hours'},
            title='Average Workout Hours by Gender',
            color_discrete_sequence=bar_palette,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),

    # Histogram of Age Distribution
    dcc.Graph(
        id='hist-age-distribution',
        figure=px.histogram(
            extended_fitness_df,
            x='Age',
            color='Gender',
            marginal='rug',
            labels={'Age': 'Age Distribution'},
            title='Age Distribution',
            color_discrete_sequence=hist_palette,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),

    # Box plot of Calories Burned by Gender
    dcc.Graph(
        id='box-calories-burned',
        figure=px.box(
            extended_fitness_df,
            x='Gender',
            y='Calories_Burned',
            color='Gender',
            labels={'Calories_Burned': 'Calories Burned'},
            title='Calories Burned Distribution by Gender',
            color_discrete_sequence=px.colors.qualitative.Set3,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),

    # Pie chart of Gender distribution
    dcc.Graph(
        id='pie-gender-distribution',
        figure=px.pie(
            extended_fitness_df,
            names='Gender',
            title='Gender Distribution',
            color_discrete_sequence=paired_palette,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),

    # Violin plot of BMI by Gender
    dcc.Graph(
        id='violin-bmi-gender',
        figure=px.violin(
            extended_fitness_df,
            x='Gender',
            y='BMI',
            color='Gender',
            labels={'BMI': 'Body Mass Index'},
            title='BMI Distribution by Gender',
            color_discrete_sequence=px.colors.qualitative.Dark24,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),

    # 3D Scatter plot of BMI, Age, and Workout Hours
    dcc.Graph(
        id='scatter-3d-bmi-age-hours',
        figure=px.scatter_3d(
            extended_fitness_df,
            x='Workout_Hours',
            y='Age',
            z='BMI',
            color='Gender',
            size='Calories_Burned',
            labels={'BMI': 'Body Mass Index', 'Workout_Hours': 'Workout Hours', 'Age': 'Age'},
            title='3D Scatter Plot of BMI, Age, and Workout Hours',
            color_discrete_sequence=px.colors.qualitative.T10,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),

    # Area chart of Calories Burned
    dcc.Graph(
    id='area-calories-over-time',
    figure=px.area(
        extended_fitness_df,
        y='Calories_Burned',
        color='Gender',
        labels={'Calories_Burned': 'Calories Burned'},
        title='Calories Burned Over Time',
        color_discrete_sequence=px.colors.qualitative.Vivid,
    ).update_layout(
        template='plotly_dark',
        margin=dict(l=0, r=0, t=30, b=30),
    )
),

    # Bubble chart of BMI vs Age with Calories Burned as size
    dcc.Graph(
        id='bubble-bmi-age-calories',
        figure=px.scatter(
            extended_fitness_df,
            x='Age',
            y='BMI',
            color='Gender',
            size='Calories_Burned',
            labels={'BMI': 'Body Mass Index', 'Age': 'Age'},
            title='BMI vs Age with Calories Burned',
            color_discrete_sequence=px.colors.qualitative.Plotly,
        ).update_layout(
            template='plotly_dark',
            margin=dict(l=0, r=0, t=30, b=30),
        )
    ),
])

# ... (your existing code)

# Footer section with project details
footer = html.Div(
    style={'backgroundColor': '#1E1E1E', 'color': '#FFFFFF', 'padding': '10px','line-height':'20px', 'width': '100%','text-align':'center'},
    children=[
        html.P("Project by:", style={'margin': '0'}),
        html.P("V. Supreethi - 211801380036", style={'margin': '0'}),
        html.P("N. Venkata Akhil - 211801370093", style={'margin': '0'}),
        html.P("R. Raju - 211801370081", style={'margin': '0'}),
        html.P("K. Nikhil - 211801370111", style={'margin': '0'}),
        html.P("N. V. Sai Sreekar - 211801380032", style={'margin': '0'}),
    ]
)

# Add the footer to the layout
app.layout.children.append(footer)

# Run the app
if __name__ == '_main_':
    app.run_server(debug=True)