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
            return {
                "Filiale": list(grouped["Gesamtpreis"].keys()),
                "Gesamtpreis": list(grouped["Gesamtpreis"].values)
            }
        else:
            grouped = SortData.df.groupby(["month", "Filiale"]).sum()
            grouped = SortData.df[SortData.df["month"] == month]
            return {
                "Filiale": list(grouped["Gesamtpreis"].keys()),
                "Gesamtpreis": list(grouped["Gesamtpreis"].values)
            }
    
    @staticmethod
    def umsatz_nach_geschlecht(month : int):
        if month == 0:
            grouped = SortData.df.groupby(["Geschlecht"]).sum()
            res = pd.DataFrame(grouped["Gesamtpreis"])
            return res
        else:
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
    def urzeit_umsatz_produktlinie(month : int):
        if month == 0:
            grouped = SortData.df.groupby(["Stunde", "Produktlinie"]).sum()
        else:
            loced = SortData.df[SortData.df["month"] == str(month)]
            grouped = loced.groupby(["Zeit", "Produktlinie"]).sum()
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
    def produktlienie_und_bewertungen(month : int):
        if month == 0:
            grouped = SortData.df.groupby(["Produktlinie"]).mean()
            res = pd.DataFrame(grouped["Bewertung"])
            o = {
                "Produktlinie": list(res["Bewertung"].keys()),
                "Bewertung": list(res["Bewertung"].values)
            }
            return o
        else:
            grouped = SortData.df.groupby(["month", "Produktlinie"]).mean()
            grouped = SortData.df[SortData.df["month"] == month]
            res = pd.DataFrame(grouped["Bewertung"])
            return res

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
            summe = str(grouped["Gesamtpreis"][mohnat])
            s = summe.split(".")
            t = s[0] + "." + s[1][0] + s[1][1]
            return t

def test_mining():
    SortData.init_dataframe()
    print("0 umsatz_nach_filialen ", SortData.umsatz_nach_filialen(0))
    print("0 umsatz_nach_geschlecht ", SortData.umsatz_nach_geschlecht(0))
    print("0 urzeit_umsatz_produktlinie ", SortData.urzeit_umsatz_produktlinie(0))
    print("0 produktlienie_und_bewertungen ", SortData.produktlienie_und_bewertungen(0))
    print("get_gesamtumsatz ", SortData.get_gesamtumsatz())
    print("0 get_umsatz_im_mohnat ", SortData.get_umsatz_im_mohnat(0))
    print("1 umsatz_nach_filialen ", SortData.umsatz_nach_filialen(1))
    print("1 umsatz_nach_geschlecht ", SortData.umsatz_nach_geschlecht(1))
    print("1 urzeit_umsatz_produktlinie ", SortData.urzeit_umsatz_produktlinie(1))
    print("1 produktlienie_und_bewertungen ", SortData.produktlienie_und_bewertungen(1))
    print("1 get_umsatz_im_mohnat ", SortData.get_umsatz_im_mohnat(1))