def keep_regs(df, regs):
    """ Example function. Keep only the subset regs of regions in data.

    Args:
        df (pd.DataFrame): pandas dataframe 

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    for r in regs:
        I = df.reg.str.contains(r)
        df = df.loc[I == False] # keep everything else
    
    return df

import seaborn as sns
import matplotlib.pyplot as plt

#Plot for income development
def plot_avg_income_over_years(avg_income_by_year):
    """
    Plots the average income over the years.

    Parameters:
    - avg_income_by_year: DataFrame or Series with index as years and values as average income.
    """
    plt.figure(figsize=(12, 6))
    avg_income_by_year.plot(kind='line', marker='o', color='b', linestyle='-')
    plt.title('Average Income Over the Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average Income', fontsize=14)
    plt.grid(True)
    plt.show()


#Plot for income development for different regions
def plot_avg_income_by_year_area(merged_df, top_n_areas=6):
    """
    Plots the average income over the years by top areas.

    Parameters:
    - merged_df: DataFrame containing the merged data.
    - top_n_areas: int, the number of top areas to include in the plot.
    """
    # Group the data by year and area, then calculate the average income for each combination
    avg_income_by_year_area = merged_df.groupby(['TID', 'OMRÅDE'])['INDHOLD_area'].mean()

    # Select only the top N areas with the highest average income
    top_areas = avg_income_by_year_area.groupby(level='OMRÅDE').mean().nlargest(top_n_areas).index

    # Filter the data to include only the top areas
    filtered_data = avg_income_by_year_area.loc(axis=0)[:, top_areas]

    # Plotting the average income over the years for each top area
    plt.figure(figsize=(12, 6))
    for area, data in filtered_data.groupby(level='OMRÅDE'):
        years = data.index.get_level_values('TID').astype(str).str[:4]  # Extracting the year from the index
        plt.plot(years, data.values, label=area, marker='o', linestyle='-')

    plt.title('Average Income Over the Years by Top Areas', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average Income', fontsize=14)
    plt.legend(title='Area', loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)

    # Set x-axis ticks
    plt.xticks(years)

    plt.show()


#plot for income distrubution by age in 2022
def plot_income_distribution_by_age(merged_df, most_recent_year):
    """
    Plots the income distribution by age group for the most recent year.

    Parameters:
    - merged_df: DataFrame containing the merged data.
    - most_recent_year: int, the most recent year to filter the data.
    """
    # Filter merged_df for the most recent year
    merged_df_recent_year = merged_df[merged_df['TID'] == most_recent_year]

    # Set the seaborn style for better aesthetics
    sns.set_style("whitegrid")

    # Plotting the boxplot for Age Groups
    plt.figure(figsize=(18, 10))
    sns.boxplot(x='ALDER1', y='INDHOLD_age', data=merged_df_recent_year, palette="Set3", showfliers=True, showmeans=True,
                meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"10"})
    plt.title(f'Income Distribution by Age Group for {most_recent_year}', fontsize=16)
    plt.xlabel('Age Group', fontsize=14)
    plt.ylabel('Income', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()
    plt.show()


#plot for income distrubution by area in 2022
def plot_income_distribution_by_area(merged_df, most_recent_year):
    """
    Plots the income distribution by area for the most recent year.

    Parameters:
    - merged_df: DataFrame containing the merged data.
    - most_recent_year: int, the most recent year to filter the data.
    """
    # Filter merged_df for the most recent year
    merged_df_recent_year = merged_df[merged_df['TID'] == most_recent_year]

    # Set the seaborn style for better aesthetics
    sns.set_style("whitegrid")

    # Plotting the boxplot for Areas
    plt.figure(figsize=(18, 10))
    sns.boxplot(x='OMRÅDE', y='INDHOLD_area', data=merged_df_recent_year, palette="Set2", showfliers=True, showmeans=True,
                meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"10"})
    plt.title(f'Income Distribution by Area for {most_recent_year}', fontsize=16)
    plt.xlabel('Area', fontsize=14)
    plt.ylabel('Income', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()
    plt.show()
