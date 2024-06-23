# Data analysis project

Our project is titled Income distrubution in Denmark and is about illustrating the income distrubution in Denmark based on region, age and sector. We use data from Danmarks statistik through an API.We use two statistics, LONS50 and LONS30, clean them both and merge them. 

We then start our analysis by first examining the overall income devlopment from 2013 to 2022, looking at the hourly wage (earnings in DKK per hour worked) for all of Denmark. We then analyize the income devlopment and income distrubution for the different areas in Denmark using a box-plot. We then look at the income distrubution for the different age groups - also using a box-plot.Lastly we examine the devlopment and growth rate in the income for different sector.

We find that income has been increasing in all regions in Denmark from 2013 to 2022. The income is greatest in the region 'Hovedstaden' and the least in 'Nordjylland' for all years, which most likely is because of 'Hovedstaden' including the capital of Denmark. Generally, we would expect to see more higher-salary jobs in capitals and larger citites. We also show two box plot with the median income for all regions and age groups in 2022. We see that although the median income for Copenhagen is very high, there is a large variability in the income distrubution for the bottom 50 pct. of income earners in 2022. 

In 2022 we see that the income median is increasing in age groups but peaks at the age group 50-54 whereafter it falls. This is presumably because young people are studying and earning a lower wage for the first years of their careers whereafter salaries increase with more experience in the job market/senior positions. The fall in income in the older age groups is most likely caused by more people retiring and switching to pensions that provides a lower income than working. For almost all age groups the median is relativly high in the box and higher than the average, which illustrates that there is greater income variability in the 50 pct. lowest earners compared to the 50 pct. highest.

The average income has increased for all sectors in Denmark from 2013 to 2022, however the sector Municipal and regional gowerment has had the greates growth rate, which is also the case when looking at the individual areas. In region Hovedstaden the highest income is from the sector Corporations and organizations, wheras in the other areas the sector for Goverment including social security funds has the highest average income, which could be because of higher average wages in the private sector in the capital city.

The **results** of the project can be seen from running [dataproject.ipynb](dataproject.ipynb).


We apply the **following datasets**:

1. LONS50 (Danmarks statistik) 
1. LONS30 (Danmarks statistik)

We have used OpenAI ChatGPT 4o to help with making code for importing, cleaning and merging the two datasets.

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:

# The DST API wrapper
%pip install git+https://github.com/alemartinello/dstapi

# A wrapper for multiple APIs with a pandas interface
%pip install pandas-datareader

# For data visualization
%pip install seaborn

# For widgets
%conda install -c conda-forge nodejs
%pip install ipywidgets

# Enable the necessary Jupyter notebook extensions
!jupyter nbextension enable --py widgetsnbextension
!jupyter nbextension install --py widgetsnbextension
!jupyter labextension install @jupyter-widgets/jupyterlab-manager
