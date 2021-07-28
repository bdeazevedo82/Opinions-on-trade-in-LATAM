import pandas as pd
import wbdata
import datetime
import pyreadstat

#Reading LB database in .sav format. File may be downloaded from LB web (see Latinobarometro_database.md
# file in repository)

# You will need to change code to match your target folders.
df, meta = pyreadstat.read_sav("C:/Users/bdeaz/OneDrive/Escritorio/Latinobarometro_2018_Esp_Spss_v20190303.sav", apply_value_formats=False)
df.to_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics and financial analysis/Regression/LB2018.csv")
data = pd.read_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics and financial analysis/Regression/LB2018.csv")
df = pd.DataFrame(data)

print("Number of rows ", len(df.index))

#Preparing data for Model 1 and 2
#checking for blank values in independent variables
try:
    df.dropna(subset = ["S10"], inplace=True)
except:
    pass
try:
    df.dropna(subset = ["EDAD"], inplace=True)
except:
    pass
try:
    df.dropna(subset = ["Male"], inplace=True)
except:
    pass
try:
    df.dropna(subset = ["Citizen"], inplace=True)
except:
    pass

#dropping blank values in dependent var
df.dropna(subset = ["P39ST.A"], inplace=True)

print("Number of rows ", len(df.index))

#inverting nominal dependent var
df["EcoInt"] = 0
df.loc[df['P39ST.A'] == 1, "EcoInt"] = 4
df.loc[df['P39ST.A'] == 2, "EcoInt"] = 3
df.loc[df['P39ST.A'] == 3, "EcoInt"] = 2
df.loc[df['P39ST.A'] == 4, "EcoInt"] = 1

#creating male dummy variable
df["Male"] = 1
df.loc[df.SEXO == 2, "Male"] = 0

#creating citizen dummy variable
df["Citizen"] = 1
df.loc[df.S16 == 2, "Citizen"] = 0

#creating dummy var for countries
df["Arg"] = 0
df.loc[df.IDENPA == 32, "Arg"] = 1
df["Bol"] = 0
df.loc[df.IDENPA == 68, "Bol"] = 1
df["Bra"] = 0
df.loc[df.IDENPA == 76, "Bra"] = 1
df["Chi"] = 0
df.loc[df.IDENPA == 152, "Chi"] = 1
df["Col"] = 0
df.loc[df.IDENPA == 170, "Col"] = 1
df["CostaR"] = 0
df.loc[df.IDENPA == 188, "CostaR"] = 1
df["RepDom"] = 0
df.loc[df.IDENPA == 214, "RepDom"] = 1
df["Ecu"] = 0
df.loc[df.IDENPA == 218, "Ecu"] = 1
df["ElSal"] = 0
df.loc[df.IDENPA == 222, "ElSal"] = 1
df["Gua"] = 0
df.loc[df.IDENPA == 320, "Gua"] = 1
df["Hon"] = 0
df.loc[df.IDENPA == 340, "Hon"] = 1
df["Mex"] = 0
df.loc[df.IDENPA == 484, "Mex"] = 1
df["Nic"] = 0
df.loc[df.IDENPA == 558, "Nic"] = 1
df["Pan"] = 0
df.loc[df.IDENPA == 591, "Pan"] = 1
df["Par"] = 0
df.loc[df.IDENPA == 600, "Par"] = 1
df["Per"] = 0
df.loc[df.IDENPA == 604, "Per"] = 1
df["Uru"] = 0
df.loc[df.IDENPA == 858, "Uru"] = 1
df["Ven"] = 0
df.loc[df.IDENPA == 862, "Ven"] = 1

#creating new var gdp using WB API to get GDP per capita by country in PPP, current USD
df["gdp"] = 0
df.loc[df.IDENPA == 32, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="ARG",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 68, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="BOL",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 76, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="BRA",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 152, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="CHL",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 170, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="COL",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 188, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="CRI",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 214, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="DOM",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 218, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="ECU",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 222, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="SLV",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 320, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="GTM",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 340, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="HND",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 484, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="MEX",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 558, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="NIC",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 591, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="PAN",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 600, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="PRY",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 604, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="PER",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 858, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="URY",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 862, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="VEN",
                                                 data_date=datetime.datetime(2011, 1, 1))[0].get("value"))

#saving our data to use on Model 1 and 2
df.to_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics"
          " and financial analysis/Regression/LB2018_M1.csv")

#Preparing data for Model 3
#creating new variables for social class

try:
    df.dropna(subset = ["S26"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["S1"], inplace=True)
except:
    pass

df["clase_obj"] = 0
df.loc[df.S26 == 1, "clase_obj"] = 5
df.loc[df.S26 == 2, "clase_obj"] = 4
df.loc[df.S26 == 3, "clase_obj"] = 3
df.loc[df.S26 == 4, "clase_obj"] = 2
df.loc[df.S26 == 5, "clase_obj"] = 1

df["clase_subj"] = 0
df.loc[df.S1 == 1, "clase_subj"] = 5
df.loc[df.S1 == 2, "clase_subj"] = 4
df.loc[df.S1 == 3, "clase_subj"] = 3
df.loc[df.S1 == 4, "clase_subj"] = 2
df.loc[df.S1 == 5, "clase_subj"] = 1

print("Number of rows ", len(df.index))

df.to_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics"
          " and financial analysis/Regression/LB2018_M3.csv")


#Preparing data for Model 4

data = pd.read_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics and "
                   "financial analysis/Regression/LB2018_M1.csv")

df = pd.DataFrame(data)

#creating new variables for values, knowledge of economics and cosmopolistanism

try:
    df.dropna(subset = ["S7"], inplace=True)
except:
    pass

df["migration"] = 0
df.loc[df.S7 == 1, "migration"] = 1

try:
    df.dropna(subset = ["S13C"], inplace=True)
except:
    pass

df["travel"] = 0
df.loc[df.S13C > 2, "travel"] = 1

df["op_other"] = (df["P40ST.A"] + df["P40ST.B"] + df["P40ST.C"] + df["P40ST.D"]) / 4

try:
    df.dropna(subset = ["op_other"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["P56N.D"], inplace=True)
except:
    pass

df["nationalist"] = 0
df.loc[df["P56N.D"] == 1, "nationalist"] = 1

df["polpar"] = 0
df.loc[df["P21STGBS.A"] > 100, "polpar"] = 1

df["bid"] = 0
df.loc[df["P44STA.B"] == 1, "bid"] = 1
df["caf"] = 0
df.loc[df["P44STA.C"] == 1, "caf"] = 1
df["fmi"] = 0
df.loc[df["P44STA.G"] == 1, "fmi"] = 1
df["bm"] = 0
df.loc[df["P44STA.H"] == 1, "bm"] = 1

df["ois"] = df["bid"] + df["caf"] + df["fmi"] + df["bm"]

try:
    df.dropna(subset = ["ois"], inplace=True)
except:
    pass

print("Number of rows ", len(df.index))

df.to_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics"
          " and financial analysis/Regression/LB2018_M4.csv")


#Preparing data for Model 5

data = pd.read_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics and "
                   "financial analysis/Regression/LB2018_M1.csv")

df = pd.DataFrame(data)


try:
    df.dropna(subset = ["P8STIC"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["P9STGBSC"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["S3"], inplace=True)
except:
    pass

df["unemfear"] = 0
df.loc[df["S3"] == 1, "unemfear"] = 1
df.loc[df["S3"] == 2, "unemfear"] = 1

print("Number of rows ", len(df.index))

df.to_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics"
          " and financial analysis/Regression/LB2018_M5.csv")


#Preparing data for Model 6, summary model

data = pd.read_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics and financial analysis/Regression/LB2018.csv")

df = pd.DataFrame(data)

try:
    df.dropna(subset = ["S10"], inplace=True)
except:
    pass
try:
    df.dropna(subset = ["EDAD"], inplace=True)
except:
    pass
try:
    df.dropna(subset = ["Male"], inplace=True)
except:
    pass
try:
    df.dropna(subset = ["Citizen"], inplace=True)
except:
    pass

df.dropna(subset = ["P39ST.A"], inplace=True)


df["EcoInt"] = 0
df.loc[df['P39ST.A'] == 1, "EcoInt"] = 4
df.loc[df['P39ST.A'] == 2, "EcoInt"] = 3
df.loc[df['P39ST.A'] == 3, "EcoInt"] = 2
df.loc[df['P39ST.A'] == 4, "EcoInt"] = 1

df["Male"] = 1
df.loc[df.SEXO == 2, "Male"] = 0

df["Citizen"] = 1
df.loc[df.S16 == 2, "Citizen"] = 0

df["Arg"] = 0
df.loc[df.IDENPA == 32, "Arg"] = 1
df["Bol"] = 0
df.loc[df.IDENPA == 68, "Bol"] = 1
df["Bra"] = 0
df.loc[df.IDENPA == 76, "Bra"] = 1
df["Chi"] = 0
df.loc[df.IDENPA == 152, "Chi"] = 1
df["Col"] = 0
df.loc[df.IDENPA == 170, "Col"] = 1
df["CostaR"] = 0
df.loc[df.IDENPA == 188, "CostaR"] = 1
df["RepDom"] = 0
df.loc[df.IDENPA == 214, "RepDom"] = 1
df["Ecu"] = 0
df.loc[df.IDENPA == 218, "Ecu"] = 1
df["ElSal"] = 0
df.loc[df.IDENPA == 222, "ElSal"] = 1
df["Gua"] = 0
df.loc[df.IDENPA == 320, "Gua"] = 1
df["Hon"] = 0
df.loc[df.IDENPA == 340, "Hon"] = 1
df["Mex"] = 0
df.loc[df.IDENPA == 484, "Mex"] = 1
df["Nic"] = 0
df.loc[df.IDENPA == 558, "Nic"] = 1
df["Pan"] = 0
df.loc[df.IDENPA == 591, "Pan"] = 1
df["Par"] = 0
df.loc[df.IDENPA == 600, "Par"] = 1
df["Per"] = 0
df.loc[df.IDENPA == 604, "Per"] = 1
df["Uru"] = 0
df.loc[df.IDENPA == 858, "Uru"] = 1
df["Ven"] = 0
df.loc[df.IDENPA == 862, "Ven"] = 1

df["gdp"] = 0
df.loc[df.IDENPA == 32, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="ARG",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 68, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="BOL",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 76, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="BRA",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 152, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="CHL",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 170, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="COL",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 188, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="CRI",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 214, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="DOM",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 218, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="ECU",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 222, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="SLV",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 320, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="GTM",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 340, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="HND",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 484, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="MEX",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 558, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="NIC",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 591, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="PAN",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 600, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="PRY",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 604, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="PER",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 858, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="URY",
                                                 data_date=datetime.datetime(2018, 1, 1))[0].get("value"))
df.loc[df.IDENPA == 862, "gdp"] = int(wbdata.get_data("NY.GDP.PCAP.PP.CD", country="VEN",
                                                 data_date=datetime.datetime(2011, 1, 1))[0].get("value"))

try:
    df.dropna(subset = ["S26"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["S1"], inplace=True)
except:
    pass

df["clase_obj"] = 0
df.loc[df.S26 == 1, "clase_obj"] = 5
df.loc[df.S26 == 2, "clase_obj"] = 4
df.loc[df.S26 == 3, "clase_obj"] = 3
df.loc[df.S26 == 4, "clase_obj"] = 2
df.loc[df.S26 == 5, "clase_obj"] = 1

df["clase_subj"] = 0
df.loc[df.S1 == 1, "clase_subj"] = 5
df.loc[df.S1 == 2, "clase_subj"] = 4
df.loc[df.S1 == 3, "clase_subj"] = 3
df.loc[df.S1 == 4, "clase_subj"] = 2
df.loc[df.S1 == 5, "clase_subj"] = 1

try:
    df.dropna(subset = ["S7"], inplace=True)
except:
    pass

df["migration"] = 0
df.loc[df.S7 == 1, "migration"] = 1

try:
    df.dropna(subset = ["S13C"], inplace=True)
except:
    pass

df["travel"] = 0
df.loc[df.S13C > 2, "travel"] = 1

df["op_other"] = (df["P40ST.A"] + df["P40ST.B"] + df["P40ST.C"] + df["P40ST.D"]) / 4

try:
    df.dropna(subset = ["op_other"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["P56N.D"], inplace=True)
except:
    pass

df["nationalist"] = 0
df.loc[df["P56N.D"] == 1, "nationalist"] = 1

df["polpar"] = 0
df.loc[df["P21STGBS.A"] > 100, "polpar"] = 1

df["bid"] = 0
df.loc[df["P44STA.B"] == 1, "bid"] = 1
df["caf"] = 0
df.loc[df["P44STA.C"] == 1, "caf"] = 1
df["fmi"] = 0
df.loc[df["P44STA.G"] == 1, "fmi"] = 1
df["bm"] = 0
df.loc[df["P44STA.H"] == 1, "bm"] = 1

df["ois"] = df["bid"] + df["caf"] + df["fmi"] + df["bm"]

try:
    df.dropna(subset = ["ois"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["P8STIC"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["P9STGBSC"], inplace=True)
except:
    pass

try:
    df.dropna(subset = ["S3"], inplace=True)
except:
    pass

df["unemfear"] = 0
df.loc[df["S3"] == 1, "unemfear"] = 1
df.loc[df["S3"] == 2, "unemfear"] = 1

print("Number of rows ", len(df.index))

df.to_csv("C:/Users/bdeaz/PycharmProjects/createdb/Economics"
          " and financial analysis/Regression/LB2018_M6.csv")