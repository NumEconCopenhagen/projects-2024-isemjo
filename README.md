# \[isemjo\]

**Group members:**
- Isabella Grünwald (nlv483)
- Emil Munch (snd950)
- Josephine Ørum-Hansen (fpl469)


This repository contains  
1. Inaugural project.  
In this project we examine different outcomes for an exchange economy defined for for two agents, A and B, and two goods. We define and illustrate the pareto efficent allocations in and Edgeworth box. We then solve for the market clearing price by calculating the error in the market clearing condition. We solve for the optimal allocations given that agent A maximizes her own utility and after, that A maximizes her utility given that agent B's utility cannot be worse than his intital endowment. In the end we solve the social planner problem and compare all the allocations in the Edgeworth box. We see that all the allocations are in the pareto efficient area.

We also solve and simulate a pre-specified economic model where we visualize the results.

2. Data project.
We fetch data from LONS50 (Danmarks statistik) on LONS30 (Danmarks statistik) using an API and show the income distrubution in Denmark based on region, age and sector.

We examining the overall income devlopment from 2013 to 2022, looking at the hourly wage (earnings in DKK per hour worked) for all of Denmark. We then analyize the income devlopment and income distrubution for the different areas in Denmark and for the different age groups. W finish by examining the devlopment and growth rate in the income for different sector.

We find that income has been increasing in all regions in Denmark from 2013 to 2022. The income is greatest in the region 'Hovedstaden' and the least in 'Nordjylland' for all years, which most likely is because of 'Hovedstaden' including the capital of Denmark. Generally, we would expect to see more higher-salary jobs in capitals and larger citites. We also show two box plot with the median income for all regions and age groups in 2022. We see that although the median income for Copenhagen is very high, there is a large variability in the income distrubution for the bottom 50 pct. of income earners in 2022.

In 2022 we see that the income median is increasing in age groups but peaks at the age group 50-54 whereafter it falls. This is presumably because young people are studying and earning a lower wage for the first years of their careers whereafter salaries increase with more experience in the job market/senior positions. The fall in income in the older age groups is most likely caused by more people retiring and switching to pensions that provides a lower income than working. For almost all age groups the median is relativly high in the box and higher than the average, which illustrates that there is greater income variability in the 50 pct. lowest earners compared to the 50 pct. highest.

The average income has increased for all sectors in Denmark from 2013 to 2022, however the sector Municipal and regional gowerment has had the greates growth rate, which is also the case when looking at the individual areas. In region Hovedstaden the highest income is from the sector Corporations and organizations, wheras in the other areas the sector for Goverment including social security funds has the highest average income, which could be because of higher average wages in the private sector in the capital city.

3. Model project.
In this project, we explored the Solow model with land and its implications using Python. We implemented the Solow Model with land and its extensions (natural resource), analyzing steady states, dynamics, and the impact of different parameters on economic growth.

The interactive plots and simulations provided insights into how changes in savings rates, population growth, and technological progress can affect the long-term economic output.

In the Solow model with land we calculate the SS value of capital-output to 2.54 and when we extend the model with natural resource the capital-output SS value falls to 2.34.

It features:

Solow Growth Model Implementation: Extends the basic Solow model to include land and exhaustible natural resources.
Multi-Start Optimization: Employs a multi-start optimization approach to robustly find the steady state solutions.
Interactive Visualization: Utilizes interactive sliders to dynamically explore how changes in model parameters affect the steady state.

4. Exam project.

We have used OpenAI ChatGPT 4o to help with making the code for problem 1, 2 and 3.

In problem 1 we consider a production economy and CO2 taxation. 

First we consider 10 values of p1 and p2 respectively in the range of {0.1,2.0}, where we find the market clearing values for the labour market, for the goods market 1 and for the goods market 2. In the next part we find the equilibrium prices p1 and p2 by using Walras’ law and checking two of the market clearings. In the end we have to find a value of tau that maximizes the social welfare function.

Problem 2 deals with a career choice model. 

In question 2.1 we simulate and calculate expected utility and average realized utility and find that they are the same as the random noise is zero on average (law of large numbers).

In question 2.2. we consider the case where graduates do not themselves now the utility from each career track but only the average utility of their friends for each career. We find that graduate types with more friends end up choicing the career with the highest given utility (v=3) and therefore end up with the highest realized utility. They also have a smaller difference between average subjective expected utility and realized utility.

In question 2.3. we build from question 2, but now consider the case where graduates can switch careers after 1 year but have a switching costs. We find that the difference between expected subejctive utility after switching and average ex post relalized utility after switching is decreasing in the graduate type, reflecting that more friends results in a more informed decision making. Because of the presence of swithcing costs we see that both the expected and realized utility is lower compared question 2.2.

We look at the share of graduates switching careers conditional on the inital career choice. We find that carrer choice 1 has the highest share of graduates switching, followed by career 2 and then 3, which is consisten with the given utility v for each carrer track. We see that the share of graduates switching is decreasing in the graduate type, again refleting that graduate types with more friends are more informed of the value of v for each career.
