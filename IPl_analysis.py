# IPL Matches Analysis – Fully Fixed Version
# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------
# Step 1: Load CSV
# ------------------------------
matches = pd.read_csv("matches.csv")

# Clean column names (remove spaces)
matches.columns = matches.columns.str.strip()

# Ensure numeric column for 'win_by_runs'
if 'win_by_runs' in matches.columns:
    matches['win_by_runs'] = pd.to_numeric(matches['win_by_runs'], errors='coerce').fillna(0)

# ------------------------------
# Step 2: Create output folder
# ------------------------------
output_folder = "ipl_plots"
os.makedirs(output_folder, exist_ok=True)

sns.set(style="darkgrid")

# ------------------------------
# 1. Top 10 Winning Teams
# ------------------------------
if 'winner' in matches.columns:
    top_winners = matches['winner'].dropna().value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_winners.values, y=top_winners.index, palette="viridis")
    plt.title("Top 10 Winning Teams")
    plt.xlabel("Matches Won")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/top_winners.png")
    plt.close()

# ------------------------------
# 2. Toss Decision Counts
# ------------------------------
if 'toss_decision' in matches.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x="toss_decision", data=matches, palette="coolwarm")
    plt.title("Toss Decision Analysis")
    plt.xlabel("Decision")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/toss_decision.png")
    plt.close()

# ------------------------------
# 3. Matches per Season
# ------------------------------
if 'season' in matches.columns:
    season_counts = matches['season'].dropna().value_counts().sort_index()
    plt.figure(figsize=(8,5))
    sns.barplot(x=season_counts.index, y=season_counts.values, palette="cubehelix")
    plt.title("Matches Played per Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/matches_per_season.png")
    plt.close()

# ------------------------------
# 4. Top Cities Hosting Matches
# ------------------------------
if 'city' in matches.columns:
    top_cities = matches['city'].dropna().value_counts().head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(x=top_cities.values, y=top_cities.index, palette="mako")
    plt.title("Top 10 Cities Hosting IPL Matches")
    plt.xlabel("Matches Hosted")
    plt.ylabel("City")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/top_cities.png")
    plt.close()

# ------------------------------
# 5. Distribution of Win Margins (Runs)
# ------------------------------
if 'win_by_runs' in matches.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(matches[matches['win_by_runs'] > 0]['win_by_runs'], bins=30, kde=True, color="green")
    plt.title("Distribution of Wins by Runs")
    plt.xlabel("Win Margin (Runs)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/win_margin_distribution.png")
    plt.close()

print(f"✅ All 5 graphs saved in '{output_folder}' folder!")
