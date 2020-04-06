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
#salviamo i dati nella variabile data
data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    fromdate=datetime.datetime(2015, 1, 1),
    todate=datetime.datetime(2018, 12, 31),
    reverse=False)
#aggiungiamo i ns dati a cerebro
cerebro.adddata(data)

class Cross_Medie(bt.Strategy):
    #definiamo la media veloce e lenta
    params = (('Med_vel', 50), ('Med_len', 100))
    
    #inizializziamo le due medie
    def __init__ (self):
        self.sma_vel = btind.SMA(period=self.p.Med_vel)
        self.sma_len = btind.SMA(period=self.p.Med_len)
    
    #definiamo il segnale di acquisto/vendita
        self.buysig = btind.CrossOver(self.sma_vel, self.sma_len)
    
        #salviamo i dati di closing
        self.dataclose = self.datas[0].close
def next(self):    
   if self.position.size:
      if self.buysig < 0:
          self.close()
          self.sell()
      elif self.buysig > 0:
          self.close()
          self.buy()
   else:
      if self.buysig > 0:
          self.buy()
      elif self.buysig < 0:
        self.sell()
def stampa(self, txt, dt=None):
        #funzione di stampa per capire cosa sta accadendo
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
           #ordine acquisto/vendita accettato
          return
        #verifica se ordine completato
        if order.status in [order.Completed]:
           if order.isbuy():
          #stampiamo dettaglio quantità, prezzo e commissioni
               self.stampa(
                   'ACQ ESEGUITO, QTY: %.2f, PREZZO: %.2f, COSTO: %.2f, COMM: %.2f' %
                   (order.executed.size,
                    order.executed.price,
                    order.executed.value,
                    order.executed.comm
                    ))
               self.buyprice = order.executed.price
               self.buycomm = order.executed.comm
           else: #vendita
               self.stampa('VEND ESEGUITA, QTY: %.2f, PREZZO: %.2f, COSTO: %.2f, COMM %.2f' %
                    (order.executed.size,
                     order.executed.price,
                     order.executed.value,
                     order.executed.comm
                     ))
           self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
               self.stampa('Ordine cancellato')
        self.order = None
def notify_trade(self, trade):
    if not trade.isclosed:
        return
    self.stampa('PROFITTO OPERAZIONE, LORDO %.2f, NETTO %.2f' %
                (trade.pnl, trade.pnlcomm))

if __name__ == '__main__':
    #inizializziamo istanza Cerebro
    cerebro = bt.Cerebro()

    #aggiungiamo una strategia
    cerebro.addstrategy(Cross_Medie)

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
    


           
        
 


