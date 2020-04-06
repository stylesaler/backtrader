# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:16:40 2020

@author: Huawei
"""


from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from mpl_finance import candlestick2_ohlc
import backtrader as bt
import backtrader.indicators as btind
import backtrader.analyzers as btanalyzers
import datetime
import os.path
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')

#inizializziamo il programma in modo standard
if __name__ == '__main__':
    cerebro = bt.Cerebro()
cerebro.run()
capitale_iniziale = 10000.0
cerebro.broker.setcash(capitale_iniziale)
cerebro.broker.getvalue()
#inizializziamo il file
modpath = os.path.basename(os.path.abspath(sys.argv[0]))
datapath = os.path.join(modpath,'C:\CODE\FCA.csv')
----------------------------------------------------------------------------------
    #Inseriamo i dati avendo cura di mettere il percorso completo del file
    modpath = os.path.basename(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath,'C:\CODE\FCA.csv')

    #salviamo i dati nella variabile data
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(2015, 1, 1),
        todate=datetime.datetime(2018, 12, 31),
        reverse=False)
    #aggiungiamo i dati a Cerebro
    cerebro.adddata(data)
    
    #impostiamo il valore iniziale del portafoglio
    cerebro.broker.setcash(100000.0)
    
    #impostiamo il numero di azione che traderemo
    cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
    
    #impostiamo il valore delle commissioni
    cerebro.broker.setcommission(commission=0.0002)
    
    #stampiamo le condizioni iniziali
    print('Valore iniziale portafoglio: %.2f' % cerebro.broker.getvalue())
    
    #lanciamo la ns strategia
    cerebro.run()
    
    #stampiamo le condizioni finali
    print('Valore finale portafoglio: %.2f' % cerebro.broker.getvalue())
    
    cerebro.plot()    
    


           
        
 


