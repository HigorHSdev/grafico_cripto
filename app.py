import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import json
import plotly.express as px
from streamlit import columns
from yfinance import Ticker

with open("data.json", "r") as _json:
    data_string = _json.read()

obj = json.loads(data_string)

crypto_names = obj["crypto_names"]
crypto_symbols = obj["crypto_symbols"]

crypto_dict = dict(zip(crypto_names, crypto_symbols))


crypto_selected = st.selectbox(label = 'Selecione sua moeda',
             options = crypto_dict.keys())

#st.write(f'A crypto selecionada foi: **{crypto_selected}**')

_symbol = crypto_dict[crypto_selected]+ '-USD'

Ticker = yf.Ticker(_symbol)

df = Ticker.history(interval='1d', period='2y')

col1, col2 = st.columns(2)

with col1:
    columns_selected = st.multiselect(label = 'Selecione as colunas do grafico:',
                                     options = df.columns)

with col2:
    #change_coin = st.selectbox(label='Selecione seu câmbio:',
    #                              options= [])
    st.header(f'Criptomoeda: **{crypto_selected}**')

fig = px.line(df,
              x = df.index,
              y = columns_selected,
              title=f'Valores de {crypto_selected}')

st.plotly_chart(fig)
