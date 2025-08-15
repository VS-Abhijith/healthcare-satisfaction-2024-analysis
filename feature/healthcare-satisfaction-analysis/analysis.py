import pandas as pd
import matplotlib.pyplot as plt

# Analyst email (verification)
print("Analyst: 22ds3000188@ds.study.iitm.ac.in")

# Data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Satisfaction": [-2.46, 0.93, 7.04, 5.38]
}
df = pd.DataFrame(data)

# Average calculation
avg = df["Satisfaction"].mean()
print(f"Average satisfaction score: {avg:.2f}")

# Visualization
plt.plot(df["Quarter"], df["Satisfaction"], marker="o", label="Company")
plt.axhline(4.5, color="r", linestyle="--", label="Industry Target")
plt.title("Patient Satisfaction Score - 2024")
plt.xlabel("Quarter")
plt.ylabel("Score")
plt.legend()
plt.savefig("feature/healthcare-satisfaction-analysis/visualization.png")

