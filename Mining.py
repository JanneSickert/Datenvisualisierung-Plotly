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
    def umsatz_nach_filialen(month : int):
        grouped = SortData.df.groupby(["month", "Filiale"]).sum()
        grouped = SortData.df[SortData.df["month"] == month]
        return {
            "Filiale": list(grouped["Gesamtpreis"].keys()),
            "Gesamtpreis": list(grouped["Gesamtpreis"].values)
        }
    
    @staticmethod
    def umsatz_nach_geschlecht(month : int):
        grouped = SortData.df.groupby(["month", "Geschlecht"]).sum()
        res = pd.DataFrame(grouped["Gesamtpreis"])
        res = res.loc[[str(month)]]
        gender_array = []
        for e in list(res["Gesamtpreis"].keys()):
            gender_array.append(e[1])
        o = {
            "Geschlecht": gender_array,
            "Gesamtpreis": list(res["Gesamtpreis"].values)
        }
        return o
    
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
    def produktlienie_und_bewertungen(month : int):
        grouped = SortData.df.groupby(["month", "Produktlinie"]).mean()
        grouped = SortData.df[SortData.df["month"] == month]
        res = pd.DataFrame(grouped["Bewertung"])
        return res
    
    @staticmethod
    def get_gesamtumsatz() -> str:
        r = str(sum(SortData.df["Gesamtpreis"]))
        s = r.split(".")
        t = s[0] + "." + s[1][0] + s[1][1]
        return t

    @staticmethod
    def get_umsatz_im_mohnat(mohnat : int) -> str:
        grouped = SortData.df.groupby(["month"]).sum()
        print(grouped)
        summe = str(grouped["Gesamtpreis"][mohnat])
        s = summe.split(".")
        t = s[0] + "." + s[1][0] + s[1][1]
        return summe

def print_all():
    print("------------------")
    print(SortData.umsatz_nach_geschlecht(2))
    print("------------------")