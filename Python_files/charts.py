import matplotlib.pyplot as plt
import seaborn as sns

def top_players_by_metrics(data):
    """Generates bar charts for the top 10 players by points, rebounds, and assists."""
    metrics = {'Points': 'pts', 'Rebounds': 'reb', 'Assists': 'ast'}
    for metric_name, col in metrics.items():
        top_players = data.nlargest(10, col)[['player_name', col]]
        plt.figure(figsize=(12, 6))
        sns.barplot(data=top_players, x=col, y='player_name', palette='Blues_d')
        plt.title(f'Top 10 Players by {metric_name}')
        plt.xlabel(metric_name)
        plt.ylabel('Player Name')
        plt.show()

def distribution_of_metrics(data):
    """Displays a box plot showing the distribution of points, rebounds, and assists."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data[['pts', 'reb', 'ast']], palette='pastel')
    plt.title("Distribution of Points, Rebounds, and Assists")
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.grid(axis='y')
    plt.show()

def top_colleges_producing_players(data):
    """Shows the top 10 colleges producing NBA players."""
    top_colleges = data['college'].value_counts().head(10).reset_index()
    top_colleges.columns = ['college', 'player_count']
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_colleges, x='player_count', y='college', palette='coolwarm')
    plt.title('Top 10 Colleges Producing Players')
    plt.xlabel('Number of Players')
    plt.ylabel('College')
    plt.show()

def average_performance_by_college(data):
    """Plots average points, rebounds, and assists by top colleges."""
    top_colleges = data['college'].value_counts().head(10).index
    college_performance = data[data['college'].isin(top_colleges)] \
        .groupby('college')[['pts', 'reb', 'ast']].mean().reset_index()
    college_performance.set_index('college').plot(kind='bar', figsize=(12, 6), color=['skyblue', 'lightgreen', 'salmon'])
    plt.title('Average Points, Rebounds, and Assists by Top Colleges')
    plt.xlabel('College')
    plt.ylabel('Average Metric Value')
    plt.xticks(rotation=45)
    plt.legend(title='Metrics')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def age_performance_trends(data):
    """Plots average performance metrics by age."""
    age_performance = data.groupby('age')[['pts', 'reb', 'ast']].mean().reset_index()
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=age_performance, x='age', y='pts', label='Points', marker='o', color='#1f77b4', linewidth=2)
    sns.lineplot(data=age_performance, x='age', y='reb', label='Rebounds', marker='s', color='#2ca02c', linewidth=2)
    sns.lineplot(data=age_performance, x='age', y='ast', label='Assists', marker='D', color='#d62728', linewidth=2)
    plt.title('Average Performance Metrics by Age', fontsize=16, fontweight='bold')
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Average Metric Value', fontsize=12)
    plt.legend(title='Metrics', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def advanced_metrics_distribution(data):
    """Plots the distribution of advanced metrics like usage rate, true shooting percentage, and net rating."""
    sns.set_theme(style="whitegrid", context="notebook", palette="deep")
    plt.figure(figsize=(12, 6))
    sns.kdeplot(data=data, x='usg_pct', fill=True, color='#1f77b4', alpha=0.6, linewidth=2, label='Usage Rate (usg_pct)')
    sns.kdeplot(data=data, x='ts_pct', fill=True, color='#2ca02c', alpha=0.6, linewidth=2, label='True Shooting % (ts_pct)')
    sns.kdeplot(data=data, x='net_rating', fill=True, color='#d62728', alpha=0.6, linewidth=2, label='Net Rating')
    plt.title('Distribution of Advanced Metrics', fontsize=16, fontweight='bold')
    plt.xlabel('Metric Value', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.legend(title='Metrics', fontsize=10)
    plt.grid(visible=True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def performance_vs_height_weight(data):
    """Plots the performance metrics against player height and weight."""
    plt.figure(figsize=(14, 8))
    sns.regplot(data=data, x='player_height', y='pts', color='#1f77b4', label='Points', scatter_kws={'alpha': 0.6}, line_kws={'color': 'black'})
    sns.regplot(data=data, x='player_height', y='reb', color='#2ca02c', label='Rebounds', scatter_kws={'alpha': 0.6}, line_kws={'color': 'black'})
    sns.regplot(data=data, x='player_height', y='ast', color='#d62728', label='Assists', scatter_kws={'alpha': 0.6}, line_kws={'color': 'black'})
    plt.title('Performance Metrics vs Player Height', fontsize=16, fontweight='bold')
    plt.xlabel('Height (m)', fontsize=12)
    plt.ylabel('Performance Metric Value', fontsize=12)
    plt.legend(title='Metrics', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(14, 8))
    sns.regplot(data=data, x='player_weight', y='pts', color='#1f77b4', label='Points', scatter_kws={'alpha': 0.6}, line_kws={'color': 'black'})
    sns.regplot(data=data, x='player_weight', y='reb', color='#2ca02c', label='Rebounds', scatter_kws={'alpha': 0.6}, line_kws={'color': 'black'})
    sns.regplot(data=data, x='player_weight', y='ast', color='#d62728', label='Assists', scatter_kws={'alpha': 0.6}, line_kws={'color': 'black'})
    plt.title('Performance Metrics vs Player Weight', fontsize=16, fontweight='bold')
    plt.xlabel('Weight (kg)', fontsize=12)
    plt.ylabel('Performance Metric Value', fontsize=12)
    plt.legend(title='Metrics', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

