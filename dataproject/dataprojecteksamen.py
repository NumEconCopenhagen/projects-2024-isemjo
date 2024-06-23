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
import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

#The following plots and dropboxes are made using OpenAI Chatgpt 4o:

#The plot for income development in all of Denmark
def plot_avg_income_over_years(avg_income_by_year):
    plt.figure(figsize=(12, 6))
    avg_income_by_year.plot(kind='line', marker='o', color='b', linestyle='-')
    plt.title('Average Income Over the Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average Income', fontsize=14)
    plt.grid(True)
    plt.show()


#plot for income devlopment by area
def plot_avg_income_by_year_area(merged_df):

    # We group the data by year and area, then calculate the average income for each combination
    avg_income_by_year_area = merged_df.groupby(['TID', 'OMRÅDE'])['INDHOLD_area'].mean()

    # Plots the average income over the years for each area
    plt.figure(figsize=(12, 6))
    for area, data in avg_income_by_year_area.groupby(level='OMRÅDE'):
        years = data.index.get_level_values('TID').astype(str).str[:4]  # Extracting the year from the index
        plt.plot(years, data.values, label=area, marker='o', linestyle='-')

    plt.title('Average Income Over the Years by Area', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average Income', fontsize=14)
    plt.legend(title='Area', loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)

    # Set x-axis ticks
    plt.xticks(years)

    plt.show()

#plot for income distrubution by age in 2022
def plot_income_distribution_by_age(merged_df, most_recent_year):

    # Filter merged_df for the most recent year
    merged_df_recent_year = merged_df[merged_df['TID'] == most_recent_year]

    # Set the seaborn style for better aesthetics
    sns.set_style("whitegrid")

    # Plots the boxplot for Age Groups
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



#Plot for average income over time by sector with dropdown box for area

def prepare_data(Inc_age_cleaned, Inc_area_cleaned):
    # Merge datasets on common 'TID' and 'SEKTOR'
    merged_df = pd.merge(Inc_age_cleaned, Inc_area_cleaned, on=['TID', 'SEKTOR'], suffixes=('_age', '_area'))

    # Calculate the average income for each sector, area, and year
    avg_income_by_sector_area = merged_df.groupby(['TID', 'SEKTOR', 'OMRÅDE'])['INDHOLD_area'].mean().reset_index()
    return avg_income_by_sector_area

def create_plot(avg_income_by_sector_area, area):
    filtered_df = avg_income_by_sector_area[avg_income_by_sector_area['OMRÅDE'] == area]
    fig = px.line(filtered_df, x='TID', y='INDHOLD_area', color='SEKTOR', 
                  labels={'TID': 'Year', 'INDHOLD_area': 'Average Income', 'SEKTOR': 'Sector'},
                  title=f'Average Income Over Time by Sector in {area}')
    return fig

def interactive_plot(Inc_age_cleaned, Inc_area_cleaned):
    avg_income_by_sector_area = prepare_data(Inc_age_cleaned, Inc_area_cleaned)

    # Define the function to update the plot based on the selected area
    def update_plot(area):
        fig = create_plot(avg_income_by_sector_area, area)
        fig.show()

    # Create a dropdown menu for area selection
    area_dropdown = widgets.Dropdown(
        options=avg_income_by_sector_area['OMRÅDE'].unique(),
        description='Select Area:',
        disabled=False,
    )

    # Link the dropdown to the update function
    output = widgets.interactive_output(update_plot, {'area': area_dropdown})

    # Display the dropdown and output
    display(area_dropdown, output)

    # Initial plot
    update_plot(avg_income_by_sector_area['OMRÅDE'].unique()[0])

#Dropdown box for growth rate by sector for each area
def calculate_growth_rate(df):
    growth_rates = []
    for (sector, area), group in df.groupby(['SEKTOR', 'OMRÅDE']):
        initial_income = group[group['TID'] == group['TID'].min()]['INDHOLD_area'].values[0]
        final_income = group[group['TID'] == group['TID'].max()]['INDHOLD_area'].values[0]
        growth_rate = ((final_income - initial_income) / initial_income) * 100
        growth_rates.append({'SEKTOR': sector, 'OMRÅDE': area, 'Growth Rate': growth_rate})
    return pd.DataFrame(growth_rates)

def interactive_growth_rate(Inc_age_cleaned, Inc_area_cleaned):
    avg_income_by_sector_area = prepare_data(Inc_age_cleaned, Inc_area_cleaned)
    growth_rates_df = calculate_growth_rate(avg_income_by_sector_area)

    # Function to update the growth rate table based on the selected area
    def update_table(area):
        filtered_df = growth_rates_df[growth_rates_df['OMRÅDE'] == area]
        display(filtered_df)

    # Create a dropdown menu for area selection
    area_dropdown = widgets.Dropdown(
        options=growth_rates_df['OMRÅDE'].unique(),
        description='Select Area:',
        disabled=False,
    )

    # Link the dropdown to the update function
    output = widgets.interactive_output(update_table, {'area': area_dropdown})

    # Display the dropdown and output
    display(area_dropdown, output)