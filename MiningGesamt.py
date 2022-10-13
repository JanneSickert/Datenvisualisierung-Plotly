import pandas as pd

class SortData:
    CSV_PATH = "supermarket_sales.csv"
    df = None

    @staticmethod
    def init_dataframe():
        SortData.df = pd.read_csv(SortData.CSV_PATH, sep=',')
    
    @staticmethod
    def umsatz_nach_filialen():
        grouped = SortData.df.groupby(["Filiale"]).sum()
        return {
            "Filiale": list(grouped["Gesamtpreis"].keys()),
            "Gesamtpreis": list(grouped["Gesamtpreis"].values)
        }
    
    @staticmethod
    def umsatz_nach_geschlecht():
        grouped = SortData.df.groupby(["Geschlecht"]).sum()
        res = pd.DataFrame(grouped["Gesamtpreis"])
        print(res)
        return res
    
    @staticmethod
    def urzeit_umsatz_produktlinie():
        zeit = SortData.df["Zeit"]
        i = 0
        while i < len(zeit):
            zeit[i] = str(zeit[i]).split(":")[0]
            i += 1
        SortData.df["Stunde"] = zeit
        grouped = SortData.df.groupby(["Stunde", "Produktlinie"]).sum()
        print(grouped)
        res = {
            "stunde": [], 
            "Produktlinie": [],
            "values": list(grouped["Gesamtpreis"].values)
        }
        for e in grouped["Gesamtpreis"].keys():
            res["stunde"].append(e[0])
            res["Produktlinie"].append(e[1])
        return res
    
    @staticmethod
    def produktlienie_und_bewertungen():
        grouped = SortData.df.groupby(["Produktlinie"]).mean()
        res = pd.DataFrame(grouped["Bewertung"])
        o = {
            "Produktlinie": list(res["Bewertung"].keys()),
            "Bewertung": list(res["Bewertung"].values)
        }
        return o