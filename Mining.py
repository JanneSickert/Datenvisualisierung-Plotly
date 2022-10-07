import pandas as pd

class SortData:
    CSV_PATH = "supermarket_sales.csv"
    df = None

    @staticmethod
    def init_dataframe():
        SortData.df = pd.read_csv(SortData.CSV_PATH, sep=',')
        month = []
        monthAsString = []
        for e in SortData.df["Datum"]:
            r = e.split("/")[0]
            if r == "1":
                monthAsString.append("Jan")
            elif r == "2":
                monthAsString.append("Feb")
            elif r == "3":
                monthAsString.append("Mär")
            else:
                print("Error: Mehr als drei Mohnate")
            month.append(r)
        SortData.df["month"] = month
        SortData.df["Month"] = monthAsString
    
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
        res = pd.DataFrame(grouped["Gesamtpreis"].keys(), grouped["Gesamtpreis"].values)
        return res
    
    @staticmethod
    def produktlienie_und_bewertungen():
        grouped = SortData.df.groupby(["Produktlinie"]).mean()
        res = pd.DataFrame(grouped["Bewertung"])
        return res
    
    @staticmethod
    def get_gesamtumsatz() -> str:
        return "100"

    @staticmethod
    def get_umsatz_im_mohnat(mohnat : int) -> str:
        return "100"