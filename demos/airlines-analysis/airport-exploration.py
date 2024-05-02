#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

airlines = pd.read_csv("data/airlines.csv")
airlines["TimeLabel"] = pd.to_datetime(airlines["TimeLabel"])

#%%

fig1 = sns.lineplot(
    data=airlines.loc[airlines["AirportCode"] == "ATL", ["TimeLabel", "NumDelaysCarrier"]],
    x="TimeLabel",
    y="NumDelaysCarrier"
)
fig1.set(xlabel="Airport", ylabel="Percentage of total flights delayed")
plt.show()

if __name__ == "__main__":
    print(airlines)
