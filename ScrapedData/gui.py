import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input,Output,State

#For PCA importing the sklearn
from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca=sklearnPCA(components=2)#Projecting to two dimension

#Importing our Serching Modules
from SearchQuery import SearchQuery

####################### GLOBAL VARIABLES #################################
app = dash.Dash()
searchObject = SearchQuery()

####################### DASH DESIGNING ###################################
app.layout=html.Div(children=[
    ######### SEARCH BAR DESIGN ########
    html.Div(children=[
        ### Ading input box for query input
        dcc.Input(id='search_box',value='Andy',type='text',style={'width':'70%'}),
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

        #Adding the slider to get variable output
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
#Callback for 1D linear ranking in table format
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
    ranked_result = searchObject.search(query)

    table_list=[]
    #Creating the table with the correspondin hyperlink
    table_list=[html.Tr([
        html.Td(html.A(result[0],href=result[1],target='_blank'))
    ])for result in ranked_result]

    return table_list

#Call back for displaying the 2D ranking
@app.callback(
    Output(component_id='2D_rank',component_property='figure'),
    [Input(component_id='search_button',component_property='n_clicks')],
    [State(component_id='search_box',component_property='value')]
)
def search_and_display_2D_ranking(dummy,query):
    '''
    This function will perform the PCA on the query and the document vector
    and then display the resuld in 2D graph.
    '''
    #Creating the query vector
    rankList=searchObject.search(query,search_length=10,return_rank_list=True)
    #Taking the tfidfMatrix
    tfidfMatrix=np.copy(searchObject.tfidfMatrix).T
    queryVector=np.copy(searchObject.queryVector).T

    #Now subtracting the query with the document to get a diff matrix
    tfidfMatrix=tfidfMatrix-queryVector

    #Now we could scale the difference matrix here later

    #Now applying the principle component analysis
    tfidfProjection=sklearn_pca.fit_transform(tfidfMatrix)

    #Now retreiving the principle component which top cosine scores
    x_pcomp=[]
    y_pcomp=[]
    doc_title=[]
    doc_url=[]
    for docIndex in rankList:
        x_pcomp.append(tfidfProjection[docIndex,0])
        y_pcomp.append(tfidfProjection[docIndex,1])
        doc_title.append(searchObject.titleList[docIndex])
        doc_url.append(searchObject.urlList[docIndex])

    #Crating the trace of the plot
    trace=go.Scatter(
        x=x_pcomp,
        y=y_pcomp,
        mode='markers',
        name=doc_title,
    )
    return trace

#################### SERVING THE APP ################################
if __name__=='__main__':
    app.run_server(debug=True)
