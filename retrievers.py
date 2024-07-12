from llama_index.core import VectorStoreIndex
# from llama_index.core.readers.json import JSONReader
from llama_index.core import Document
import pandas as pd
import numpy as np
import datetime
import streamlit as st


def return_vals(df,c):
    if isinstance(df[c].iloc[0], (int, float, complex)):
        return {'max_value':max(df[c]),'min_value': min(df[c]), 'mean_value':np.mean(df[c])}
    elif(isinstance(df[c].iloc[0],datetime.datetime)):
        return {str(max(df[c])), str(min(df[c])), str(np.mean(df[c]))}
    else:
        return {'top_10_values':df[c].value_counts()[:10], 'total_categoy_count':len(df[c].unique())}
    
def correct_num(df,c):
    try:
        df[c] = df[c].fillna('0').str.replace(',','').astype(float)
        return df[c]
    except:
        return df[c]




def make_data(df, desc):
    dict_ = {}


        
    for c in df.columns:
        if df[c].isnull().all():
            df[c] = 'Null'
        df[c] = correct_num(df,c)
        
        # type = type(df[c])
        dict_[c] = {'column_name':c,'type':str(type(df[c].iloc[0])), 'column_information':return_vals(df,c)}
    dict_['Description'] = desc
    return dict_




styling_instructions =[
    Document(text="""
        Dont ignore any of these instructions.
        For a line chart always use plotly_white template, reduce x axes & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label and try to use multiple colors if more than one line
        Annotate the min and max of the line
        Display numbers in thousand(K) or Million(M) if larger than 1000/100000 
        Show percentages in 2 decimal points with '%' sign
        Default size of chart should be height =1200 and width =1000
        
        """
        )
   , Document(text="""
        Dont ignore any of these instructions.
        For a bar chart always use plotly_white template, reduce x axes & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label 
        Always display numbers in thousand(K) or Million(M) if larger than 1000/100000. 
        Annotate the values of the bar chart
        If variable is a percentage show in 2 decimal points with '%' sign.
        Default size of chart should be height =1200 and width =1000
        """)
        ,
Document(text=
          """
        For a histogram chart choose a bin_size of 50
        Do not ignore any of these instructions
        always use plotly_white template, reduce x & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label 
        Always display numbers in thousand(K) or Million(M) if larger than 1000/100000. Add annotations x values
        If variable is a percentage show in 2 decimal points with '%'
        Default size of chart should be height =1200 and width =1000
        """),

Document(text=
          """
        For a pie chart only show top 10 categories, bundle rest as others
        Do not ignore any of these instructions
        always use plotly_white template, reduce x & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label 
        Always display numbers in thousand(K) or Million(M) if larger than 1000/100000. Add annotations x values
        If variable is a percentage show in 2 decimal points with '%'
        Default size of chart should be height =1200 and width =1000
        """),
Document(text=
          """
        Do not ignore any of these instructions
        always use plotly_white template, reduce x & y axes line to 0.2 & x & y grid width to 1. 
        Always give a title and make bold using html tag axis label 
        Always display numbers in thousand(K) or Million(M) if larger than 1000/100000. Add annotations x values
        Don't add K/M if number already in , or value is not a number
        If variable is a percentage show in 2 decimal points with '%'
        Default size of chart should be height =1200 and width =1000
        """),
Document(text="""
    For a heat map
    Use the 'plotly_white' template for a clean, white background. 
    Set a chart title 
    Style the X-axis with a black line color, 0.2 line width, 1 grid width, format 1000/1000000 as K/M
    Do not format non-numerical numbers 
    .style the Y-axis with a black line color, 0.2 line width, 1 grid width format 1000/1000000 as K/M
    Do not format non-numerical numbers 

    . Set the figure dimensions to a height of 1200 pixels and a width of 1000 pixels.
"""),
Document(text="""
    For a Histogram, used for returns/distribution plotting
    Use the 'plotly_white' template for a clean, white background. 
    Set a chart title 
    Style the X-axis  1 grid width, format 1000/1000000 as K/M
    Do not format non-numerical numbers 
    .style the Y-axis, 1 grid width format 1000/1000000 as K/M
    Do not format non-numerical numbers 
    
    Use an opacity of 0.75

     Set the figure dimensions to a height of 1200 pixels and a width of 1000 pixels.
""")
       
         ]






