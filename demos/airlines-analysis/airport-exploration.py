#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cwd = "/Users/Jodie.Burchell/Documents/git/pycon-us-demos/demos/airlines-analysis"
airlines = pd.read_csv(f"{cwd}/data/airlines.csv")
airlines["TimeLabel"] = pd.to_datetime(airlines["TimeLabel"], format="%Y/%m")

#%%

fig1 = sns.lineplot(
    data=airlines.loc[airlines["AirportCode"] == "ATL", ["TimeLabel", "NumDelaysCarrier"]],
    x="TimeLabel",
    y="NumDelaysCarrier"
)
fig1.set(xlabel="Airport", ylabel="Percentage of total flights delayed")
plt.show()

fig2 = sns.displot(
    data=airlines.loc[airlines["AirportCode"] == "ATL", ["TimeLabel", "NumDelaysCarrier"]],
    x="NumDelaysCarrier",
    kind="kde"
)

if __name__ == "__main__":
    print(airlines)
