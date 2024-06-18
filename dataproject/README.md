# Data analysis project

Our project is titled Income distrubution in Denmark and is about illustrating the income distrubution in Denmark based on region and age. We use data from Danmarks statistik through and an API.

We find that income has been increasing in all regions in Denmark from 2013 to 2022. The income is greatest in the region 'Hovedstaden' and the least in 'Nordjylland' for all years, which most likely is because of 'Hovedstaden' including the capital of Denmark. Generally, we would expect to see more higher-salary jobs in capitals and larger citites. We also show two box plot with the median income for all regions and age groups in 2022. We see that although the median income for Copenhagen is very high, there is a large variability in the income distrubution for the bottom 50 pct. of income earners in 2022. 

In 2022 we see that the income median is increasing in age groups but peaks at the age group 50-54 whereafter it falls. This is presumably because young people are studying and earning a lower wage for the first years of their careers whereafter salaries increase with more experience in the job market/senior positions. The fall in income in the older age groups is most likely caused by more people retiring and switching to pensions that provides a lower income than working. For almost all age groups the median is relativly high in the box, which illustrates that there is greater income variability in the 50 pct. lowest earners compared to the 50 pct. highest.

The **results** of the project can be seen from running [dataproject.ipynb](dataproject.ipynb).

We apply the **following datasets**:

1. LONS50 (Danmarks statistik) 
1. LONS30 (Danmarks statistik)

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:

``pip install matplotlib-venn``
# The DST API wrapper
%pip install git+https://github.com/alemartinello/dstapi
# A wrapper for multiple APIs with a pandas interface
%pip install pandas-datareader

import datetime
import pandas_datareader 
from dstapi import DstApi