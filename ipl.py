import pandas as pd
import random

# Batsmen, bowlers, and venues for random selection
batsmen = ['Ruturaj', 'Conway', 'Dhoni', 'Rayudu', 'Jadeja', 'Moeen Ali', 'Gaikwad', 'Mishra', 'Vijay', 'Rahul']
bowlers = ['Bumrah', 'Shami', 'Boult', 'Archer', 'Chahar', 'Thakur', 'Jamieson', 'Patel', 'Rahul', 'Saini']
venues = ['Wankhede', 'Narendra Modi Stadium', 'Eden Gardens', 'M Chinnaswamy', 'MA Chidambaram', 'Rajiv Gandhi Stadium']

# Create 20 matches, 20 overs each, 6 balls per over (4800 rows)
data = []
for match_id in range(1, 21):  # 20 matches
    for over in range(1, 21):  # 20 overs
        for ball in range(1, 7):  # 6 balls in an over
            batsman = random.choice(batsmen)
            bowler = random.choice(bowlers)
            runs = random.choice([0, 1, 2, 3, 4, 6])  # Random runs scored
            dismissal = random.choice(['No', 'Caught', 'Bowled', 'Run Out', 'LBW']) if runs == 0 else 'No'
            venue = random.choice(venues)
            data.append([match_id, over, ball, batsman, bowler, runs, dismissal, venue])

# Convert data to DataFrame
df_large = pd.DataFrame(data, columns=['match_id', 'over', 'ball', 'batsman', 'bowler', 'runs', 'dismissal', 'venue'])

# Save DataFrame to CSV
df_large.to_csv('ipl_large_data.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv("ipl2025.csv")

# Display the first few rows of the data to check
print(df.head())

# Calculate total runs by each batsman
batsman_runs = df.groupby('batsman')['runs'].sum()

# Display the runs
print(batsman_runs)

# Get the top 10 batsmen by total runs
top_batsmen = batsman_runs.sort_values(ascending=False).head(10)

# Plot the bar chart for the top 10 batsmen
top_batsmen.plot(kind='bar', figsize=(10, 6))
plt.title('Top 10 Batsmen by Total Runs')
plt.xlabel('Batsman')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.show()

# Count the number of each dismissal type
dismissals = df['dismissal'].value_counts()

# Plot the pie chart for dismissal types
dismissals.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Dismissal Types Distribution')
plt.ylabel('')
plt.show()
# Filter the data for Powerplay (overs 1-6)
powerplay_df = df[df['over'] <= 6]

# Group by batsman and calculate total runs scored in Powerplay
powerplay_batsmen_runs = powerplay_df.groupby('batsman')['runs'].sum()

# Plot the runs scored by each batsman in Powerplay
powerplay_batsmen_runs.sort_values(ascending=False).plot(kind='bar', figsize=(12, 6))
plt.title('Runs Scored by Batsmen in Powerplay (Overs 1-6)')
plt.xlabel('Batsman')
plt.ylabel('Runs')
plt.xticks(rotation=45)
plt.show()
batsman_runs = df.groupby('batsman')['runs'].sum().sort_values(ascending=False)
batsman_runs.plot(kind='bar', figsize=(12, 6))
plt.title('Total Runs Scored by Each Batsman')
plt.xlabel('Batsman')
plt.ylabel('Runs')
plt.xticks(rotation=45)
plt.show()
runs_per_over = df.groupby('over')['runs'].sum()
runs_per_over.plot(kind='line', figsize=(12, 6), marker='o')
plt.title('Runs Scored in Each Over')
plt.xlabel('Over')
plt.ylabel('Total Runs')
plt.grid(True)
plt.show()
# Assuming there's a 'team' column
team_runs = df.groupby('team')['runs'].sum().sort_values(ascending=False)
team_runs.plot(kind='bar', figsize=(12, 6))
plt.title('Total Runs Scored by Each Team')
plt.xlabel('Team')
plt.ylabel('Runs')
plt.xticks(rotation=45)
plt.show()
bowler_runs = df.groupby('bowler')['runs'].sum().sort_values(ascending=False)
bowler_runs.plot(kind='bar', figsize=(12, 6))
plt.title('Total Runs Conceded by Each Bowler')
plt.xlabel('Bowler')
plt.ylabel('Runs Conceded')
plt.xticks(rotation=45)
plt.show()
