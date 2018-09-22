import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input,Output,State

#Importing our Serching Modules
from SearchQuery import SearchQuery

####################### GLOBAL VARIABLES #################################

external_scripts = [
    {
        'src' : "https://code.jquery.com/jquery-3.3.1.slim.min.js",
        'integrity' : "sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo",
        'crossorigin' : "anonymous"
    },
    {
        'src' : "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js",
        'integrity' : "sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49",
        'crossorigin' : "anonymous"
    },
    {
        'src' : "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js",
        'integrity' : "sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy",
        'crossorigin' : "anonymous"
    }
]

external_stylesheets = [
    {
        'href' : 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel' : 'stylesheet',
        'integrity' : 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin' : 'anonymous'
    }
]

app = dash.Dash(__name__, external_scripts=external_scripts, external_stylesheets=external_stylesheets)

####################### DASH DESIGNING ###################################

app.layout = html.Div(children=[
    ######### SEARCH BAR DESIGN ########
    html.Nav(className='navbar navbar-dark', children=[
        html.Div(className='container-fluid', children=[
            html.Div(id='search_box_container', className='row justify-content-md-center', children=[
                html.Div(className='input-group col-9', children=[
                    ### Ading input box for query input
                    dcc.Input(id='search_box', className='form-control', value='',placeholder='Enter Text',type='text'),
                    html.Div(className='input-group-append', children=[
                        ### Adding the search button
                        html.Button(id='search_button', className='btn btn-primary',children='Search',n_clicks=0)
                    ])
                ])
            ])
        ])
    ]),

    ######## RESULT DISPLAY ###########
    html.Div(children=[
        #Linear rank Table display
        html.Table(id='linear_rank',style={'width':'50%','margin-left':'5px'}),

        #2-Dimensional rank Scatter Plot(interactive)
        dcc.Graph(id='2D_rank',style={'width':'50%','margin-left':'5px'})
    ],
    style={'width':'100%',
            'display':'inline-block'}
    ),

    ######## SEARCH DISPLAY ###########
    html.Div(children=[
        ### Adding the dispay label for the selected document
        html.Label(id='display_box',children='',style={'width':'70%'}),
        ### Adding the button to go the the specified link
        html.Button(id='go_to_link',children='Go to Link',style={'width':'20%','margin-left':'5px'})
    ],
    style={'width':'100%',
            'display':'inline-block'}
    )
])

##################### CALLBACKS for ELEMENTS #########################
@app.callback(
    Output(component_id='linear_rank',component_property='children'),
    [Input(component_id='search_button',component_property='n_clicks')],
    [State(component_id='search_box',component_property='value')]
)
def search_and_display_linear_ranking(dummy,query):
    '''
    This function will take the query from the search-box after pressing the
    submit button, then this will query the tf-idf vector and display linear
    ranking in Table.
    '''

    # test_result=[('name1','https://community.plot.ly/t/hyperlink-in-label/8224'),
    #             ('name2','https://github.com/plotly/dash-html-components/issues/16')]

    #Querying our tf_idf ranking system to get the relevant document
    searchObject = SearchQuery()
    ranked_result = searchObject.search(query)

    table_list=[]
    #Creating the table with the correspondin hyperlink
    table_list=[html.Tr([
        html.Td(html.A(result[0],href=result[1],target='_blank'))
    ])for result in ranked_result]

    return table_list


#################### SERVING THE APP ################################
if __name__=='__main__':
    app.run_server(debug=True)
