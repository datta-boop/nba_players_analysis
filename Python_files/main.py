import pandas as pd
import preprocessor
import charts

data_url = 'https://drive.google.com/file/d/1pHWdi3JL7adFVLclrl28a1x_S9w1AkWs/view?usp=sharing'

# Load the data
def load_data(url):
    try:
        data = pd.read_csv(url)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Main function
def main():
    # Step 1: Load the data
    data = load_data(data_url)
    if data is None:
        return

    # Step 2: Preprocess the data
    cleaned_data = preprocessor.clean_data(data)

    # Step 3: Visualize the data
    print("Generating visualizations...")

    charts.top_players_by_points_rebounds_assists(cleaned_data)
    charts.distribution_of_metrics(cleaned_data)
    charts.top_colleges_and_performance(cleaned_data)
    charts.performance_by_age(cleaned_data)
    charts.advanced_metrics_distribution(cleaned_data)
    charts.top_net_rating_players(cleaned_data)
    charts.correlation_heatmap(cleaned_data)
    charts.performance_vs_height(cleaned_data)
    charts.performance_vs_weight(cleaned_data)
    charts.team_average_height_vs_performance(cleaned_data)
    charts.draft_year_performance(cleaned_data)
    charts.top_players_scatterplot(cleaned_data)
    charts.team_performance_over_seasons(cleaned_data)

    print("Visualizations generated successfully.")


main()
