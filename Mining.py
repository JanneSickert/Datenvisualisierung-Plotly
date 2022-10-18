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
        zeit = SortData.df["Zeit"]
        i = 0
        while i < len(zeit):
            zeit[i] = str(zeit[i]).split(":")[0]
            i += 1
        SortData.df["Stunde"] = zeit
    
    @staticmethod
    def umsatz_nach_filialen(month : int):
        if month == 0:
            grouped = SortData.df.groupby(["Filiale"]).sum()
        else:
            selectiert = SortData.df[SortData.df["month"] == str(month)]
            grouped = selectiert.groupby(["Filiale"]).sum()
        return {
            "Filiale": list(grouped["Gesamtpreis"].keys()),
            "Gesamtpreis": list(grouped["Gesamtpreis"].values)
        }
    
    @staticmethod
    def umsatz_nach_geschlecht(month : int):
        if month == 0:
            grouped = SortData.df.groupby(["Geschlecht"]).sum()
        else:
            selectiert = SortData.df[SortData.df["month"] == str(month)]
            grouped = selectiert.groupby(["Geschlecht"]).sum()
        return {
            "Geschlecht": list(grouped["Gesamtpreis"].keys()),
            "Gesamtpreis": list(grouped["Gesamtpreis"].values)
        }
    
    @staticmethod
    def urzeit_umsatz_produktlinie(month : int):
        if month == 0:
            grouped = SortData.df.groupby(["Stunde", "Produktlinie"]).sum()
        else:
            loced = SortData.df[SortData.df["month"] == str(month)]
            grouped = loced.groupby(["Zeit", "Produktlinie"]).sum()
        res = {
            "stunde": [], 
            "Produktlinie": [],
            "Gesamtpreis": list(grouped["Gesamtpreis"].values)
        }
        for e in grouped["Gesamtpreis"].keys():
            res["stunde"].append(e[0])
            res["Produktlinie"].append(e[1])
        result_df = pd.DataFrame(res)
        return result_df
    
    @staticmethod
    def produktlienie_und_bewertungen(month : int): 
        if month == 0:
            grouped = SortData.df.groupby(["Produktlinie"]).mean()
        else:
            selectiert = SortData.df[SortData.df["month"] == str(month)]
            grouped = selectiert.groupby(["Produktlinie"]).mean()
        return {
            "Produktlinie": list(grouped["Bewertung"].keys()),
            "Bewertung": list(grouped["Bewertung"].values)
        }

    @staticmethod
    def get_umsatz_im_mohnat(mohnat : int) -> str:
        if mohnat == 0:
            r = str(sum(SortData.df["Gesamtpreis"]))
            s = r.split(".")
            t = s[0] + "." + s[1][0] + s[1][1]
            return t
        else:
            grouped = SortData.df.groupby(["month"]).sum()
            print(grouped)
            summe = str(grouped["Gesamtpreis"][mohnat - 1])
            s = summe.split(".")
            t = s[0] + "." + s[1][0] + s[1][1]
            return t