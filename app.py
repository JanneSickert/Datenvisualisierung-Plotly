import pandas as pd
import plotly.express as px

class SortData:
    CSV_PATH = "supermarket_sales.csv"
    df = None

    @staticmethod
    def init_dataframe():
        SortData.df = pd.read_csv(SortData.CSV_PATH, sep=',')
    
    @staticmethod
    def umsatz_nach_filialen():
        grouped = SortData.df.groupby(["Filiale"]).sum()
        res = pd.DataFrame(grouped["Gesamtpreis"])
        return res
    
    @staticmethod
    def umsatz_nach_geschlecht():
        grouped = SortData.df.groupby(["Geschlecht"]).sum()
        res = pd.DataFrame(grouped["Gesamtpreis"])
        return res
    
    @staticmethod
    def urzeit_umsatz_produktlinie():
        zeit = SortData.df["Zeit"]
        i = 0
        while i < len(zeit):
            zeit[i] = str(zeit[i]).split(":")[0]
            i += 1
        SortData.df["Zeit"] = zeit
        grouped = SortData.df.groupby(["Zeit", "Produktlinie"]).sum()
        res = pd.DataFrame(grouped["Gesamtpreis"])
        return res
    
    @staticmethod
    def produktlienie_und_bewertungen():
        grouped = SortData.df.groupby(["Produktlinie"]).mean()
        res = pd.DataFrame(grouped["Bewertung"])
        return res

SortData.init_dataframe()
print(SortData.urzeit_umsatz_produktlinie())