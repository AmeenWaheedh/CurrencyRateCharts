
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from ui_widget import Ui_Widget
import pandas as pd



class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Currency Charts")

     #   self.df = pd.read_csv(r'C:\Users\USER\Documents\scrapeData.csv', header=0)
        self.df = pd.read_csv(r'https://raw.githubusercontent.com/AmeenWaheedh/Files/main/scrapeData.csv', header=0)
        currencies = self.df['Cur'].drop_duplicates()
        self.cmb_currency.addItems(currencies)

        #set default currency category i.e buy or sell
        self.radio_Sell.setChecked(True)
        if self.radio_Sell.isChecked:
            self.currency_action = 'Sell'
        else:
            self.currency_action = 'Buy'
        self.currency_data = self.df[self.df['Cur'] == self.cmb_currency.currentText()]
        
        self.figure = Figure(figsize=(1,1))
        
        self.axes = self.figure.add_subplot(111)
        self.axes.plot(self.currency_data['Date'],self.currency_data[self.currency_action])
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layout = QVBoxLayout(self)
        
        self.layout.addWidget(self.canvas)
        self.frame_chart.setLayout(self.layout)
        

        self.cmb_currency.currentIndexChanged.connect(self.on_combo_box_changed)
        self.radio_Buy.clicked.connect(self.on_radio_buy_clicked)
        self.radio_Sell.clicked.connect(self.on_radio_sell_clicked)
    
    def on_combo_box_changed(self):
        self.currency_data = self.df[self.df['Cur'] == self.cmb_currency.currentText()]
      #  print (self.currency_data)
        self.axes.cla()
        
        self.axes.plot(self.currency_data['Date'],self.currency_data[self.currency_action])
        self.canvas.draw()

    def on_radio_buy_clicked(self):
        self.currency_action = 'Buy'
        self.axes.cla()
        self.axes.plot(self.currency_data['Date'], self.currency_data[self.currency_action])
        self.canvas.draw()
    
    def on_radio_sell_clicked(self):
        self.currency_action = 'Sell'
        self.axes.cla()
        self.axes.plot(self.currency_data['Date'], self.currency_data[self.currency_action])
        self.canvas.draw()