import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

cars = pd.read_excel(
    'C:/Users/Mati/Desktop/PROGRAMOWANIE/NAUKA/DASH_PLOTLY/dash_tutorial/03_dash_core/cars.xlsx')

cars = cars.transpose()

cars.reset_index(inplace=True)

cars = px.bar(cars, x='index', y=0, title='Number of cars in Poland in 1999-2020',
              labels={'index': 'Years', '0': 'Number of cars'})

car_accf = pd.read_excel(
    'C:/Users/Mati/Desktop/PROGRAMOWANIE/NAUKA/DASH_PLOTLY/dash_tutorial/03_dash_core/wypadki.xlsx')

population_pl = px.bar(car_accf, x='Rok', y='Ludnosc', title='Number of people in Poland in 1999-2020',
                       labels={'Rok': 'Year', 'Ludnosc': 'Number of people'})

car_acc = px.bar(car_accf, x='Rok', y='wypadki', title='Number of car accidents in Poland in 1999-2020',
                 labels={'Rok': 'Year', 'wypadki': 'Number of car accidents'})

car_acc_df = pd.read_excel(
    'C:/Users/Mati/Desktop/PROGRAMOWANIE/NAUKA/DASH_PLOTLY/dash_tutorial/03_dash_core/smiertelne.xlsx')

car_acc_d = px.bar(car_acc_df, x='Rok', y='wypadki', title='Number of death car accidents in Poland in 1999-2020',
                   labels={'Rok': 'Year', 'wypadki': 'Number of death car accidents'})

car_acc_join = car_accf.merge(car_acc_df, on='Rok')
car_acc_join['death_percent [%]'] = car_acc_join['wypadki_y'] / \
    car_acc_join['wypadki_x']*100

death_percent = px.line(car_acc_join, x='Rok', y='death_percent [%]', title='Number of percent of death car accidents in Poland in 1999-2020', labels={
                        'Rok': 'Year', 'death_percent [%]': 'Death car accidents / Car accidents [%]'})

app.layout = html.Div([

    dcc.Graph(
        figure=population_pl),
    dcc.Graph(
        figure=cars),
    dcc.Graph(
        figure=car_acc),
    dcc.Graph(
        figure=car_acc_d),
    dcc.Graph(
        figure=death_percent),
])


if __name__ == '__main__':
    app.run_server(debug=True)
