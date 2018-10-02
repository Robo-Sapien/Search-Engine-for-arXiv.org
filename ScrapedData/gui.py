import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input,Output,State

#For PCA importing the sklearn
from sklearn.decomposition import PCA as sklearnPCA
import numpy as np
sklearn_pca=sklearnPCA(n_components=2)#Projecting to two dimension

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
searchObject = SearchQuery()

####################### DASH DESIGNING ###################################

app.layout = html.Div(children=[
    ######### SEARCH BAR DESIGN ########
    html.Nav(className='navbar navbar-dark bg-dark', children=[
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
    html.Div(id='result_container', className='container-fluid', children=[
        html.Div(className='row justify-content-md-center', children=[
            #Table Display
            html.Div(id='link_box', className='col-6 add_padding', children=[
                #Name of the Section
                html.H2(children='Linear Search Result',
                        style=dict(textAlign='center')),

                #Linear rank Table display
                html.Ul(id='doc_list', className='list-group list-group-flush')
                #Adding the slider to get variable output
            ]),

            ######## SEARCH DISPLAY ###########
            html.Div(id='graph_box', className='col-6', children=[
                #Name of the Section
                html.H2(children='Interactive Search Result',
                        style=dict(textAlign='center')),

                #Adding the DropDown Box for the choosing between Domain or ranked
                html.Label('Group Search By: '),
                dcc.Dropdown(
                    options=[
                        {'label':'Rank','value':'rank'},
                        {'label':'Document Domain','value':'domain'},
                    ],
                    value='rank'
                ),
                #2-Dimensional rank Scatter Plot(interactive)
                dcc.Graph(id='2D_rank'),

                #Adding the HyperLink area for the clicked data
                html.Div(id='click_div',children=[
                    html.Label('Hyperlink: Clicked Search Result'),
                    html.Label(id='clickdata_hyperlink')
                ])
            ])
        ])
    ])
])

    # ### Adding the dispay label for the selected document
    # html.Label(id='display_box',children='',style={'width':'70%'}),
    # ### Adding the button to go the the specified link
    # html.Button(id='go_to_link',children='Go to Link',style={'width':'20%','margin-left':'5px'})

##################### CALLBACKS for ELEMENTS #########################
#Callback for 1D linear ranking in table format
@app.callback(
    Output(component_id='doc_list',component_property='children'),
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

    doc_list=[]

    if len(ranked_result) == 0:
        doc_list=[
            html.Li(className='list-group-item', children=[
                html.A(href='#',target='_blank', children=[
                    'No results found'
                ])
            ])
        ]
        return doc_list
    #Creating the table with the correspondin hyperlink
    doc_list=[
        html.Li(className='list-group-item', children=[
            html.A(href=result[1],target='_blank', children=[
                result[0],
                html.Br(),
                html.Span(className='badge badge-light', children=[result[1]])
            ])
        ])
    for result in ranked_result]

    return doc_list

#Callback for displaying the 2D ranking
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
    rankList=searchObject.search(query,search_length=5000,return_rank_list=True)
    print ('Length of result:',len(rankList))
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
    for docIndex in rankList[0:10]:
        x_pcomp.append(tfidfProjection[docIndex,0])
        y_pcomp.append(tfidfProjection[docIndex,1])
        #doc_title.append(searchObject.titleList[docIndex])
        doc_url.append(searchObject.urlList[docIndex])
        doc_title.append(searchObject.titleList[docIndex]+'<br>'+doc_url[-1])

    #Crating the trace of the plot
    trace_good=go.Scatter(
        x=x_pcomp,
        y=y_pcomp,
        mode='markers',
        text=doc_title,
        marker=dict(size=10,
                    color='rgba(192, 0, 0, .8)',
                    line=dict(width=2)),
        name='top_10'
    )

    #Creating the trace for the lower ranking than the first 10
    bx_pcomp=[]     #Initializing the x-p_component of the bad docs
    by_pcomp=[]     #Initlaizing the y-p_component of the bad docs
    doc_title=[]
    doc_url=[]
    for docIndex in rankList[10:]:
        bx_pcomp.append(tfidfProjection[docIndex,0])
        by_pcomp.append(tfidfProjection[docIndex,1])
        doc_url.append(searchObject.urlList[docIndex])
        doc_title.append(searchObject.titleList[docIndex]+'<br>'+doc_url[-1])

    #Crating the trace of the plot
    trace_bad=go.Scatter(
        x=bx_pcomp,
        y=by_pcomp,
        mode='markers',
        text=doc_title,
        marker=dict(size=5,
                    color='rgba(205, 182, 253, .9)',
                    line=dict(width=2)),
        name='below_10'
    )

    #Creating a trace for the query vector
    trace_query=go.Scatter(
        x=[0,],
        y=[0,],
        mode='markers',
        text='Query',
        marker=dict(size=15,
                    color='rgb(0,0,0)',
                    symbol='star',),
        name='Query Vector',
    )


    #Finally Creating the graph object and returning it
    graph={
        'data':[trace_good,trace_bad,trace_query],
        'layout':go.Layout(
                title='2D Visualization of Result',
                xaxis={'title':'( <-- Machine Learning )    First Principle Component    ( Physics --> )','range':[-10,10]},
                yaxis={'title':'Second Principle Component',
                        'range':[-10,10]},
                hovermode='closest',
                shapes=[
                    {
                        'type':'rect',
                        'xref':'x',
                        'yref':'y',
                        'x0':0,
                        'y0':-10,
                        'x1':10,
                        'y1':10,
                        'fillcolor':'#d3d3d3',
                        'opacity':0.2,
                        'line':{
                            'width':0,
                        }
                    }
                ]
            )
    }
    return graph

#Callback for displaying the clicked search result
@app.callback(
    Output(component_id='clickdata_hyperlink',component_property='children'),
    [Input(component_id='2D_rank',component_property='clickData')]
)
def create_clicked_hyperlink(clickData):
    #print (clickData)
    doc_name_url=clickData['points'][0]['text']
    doc_name,doc_url=doc_name_url.split('<br>')
    #print (doc_name)
    hyperlink=html.A(href=doc_url,target='_blank',children=[
                        doc_name,
                    ])
    return hyperlink


#################### SERVING THE APP ################################
if __name__=='__main__':
    app.run_server(debug=True)
