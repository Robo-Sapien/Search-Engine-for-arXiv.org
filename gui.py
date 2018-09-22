import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input,Output,State

#Importing our Serching Modules
from ScrapedData.SearchQuery import SearchQuery

####################### GLOBAL VARIABLES #################################
app=dash.Dash()
chotu_searcher=SearchQuery()

####################### DASH DESIGNING ###################################
app.layout=html.Div(children=[
    ######### SEARCH BAR DESIGN ########
    html.Div(children=[
        ### Ading input box for query input
        dcc.Input(id='search_box',value='Dont B*ng,just Search!!',type='text',style={'width':'70%'}),
        ### Adding the search button
        html.Button(id='search_button',children='Search',n_clicks=0,style={'width':'20%','margin-left':'5px'})
    ],
    style={'width':'100%',
            'display':'inline-block'}
    ),

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
    ranked_results=chotu_searcher.search(query)

    #Creating the table with the correspondin hyperlink
    table_list=[html.Tr([
        html.Td(html.A(result[0],href=result[1],target='_blank'))
    ])for result in ranked_result]

    return table_list


#################### SERVING THE APP ################################
if __name__=='__main__':
    app.run_server(debug=True)
