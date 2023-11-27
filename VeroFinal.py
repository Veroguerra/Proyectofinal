
import pandas as pd

info_hopital = pd.read_csv('/content/drive/MyDrive/Hospital/BaseDatosVeroFinal22.csv', encoding='ISO-8859-1', sep=';')

link: https://colab.research.google.com/drive/1-wq1skHaqs-HmQJ0wUvOxIBvzdwJrgKK?usp=sharing

from google.colab import drive
drive.mount('/content/drive')

info_hopital.shape

list(info_hopital['Hospital'].drop_duplicates().tail(5))

list(info_hopital['Edad'].drop_duplicates())

list(info_hopital['Tomamedicamentos'].drop_duplicates())

