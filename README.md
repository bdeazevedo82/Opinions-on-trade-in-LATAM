# Opinions on trade in LATAM

This repository contains code on regressions and data analysis used in one of my publications on trade issues (Article available in spanish at: https://publications.iadb.org/es/revista-integracion-comercio-2019-el-nuevo-factor-del-comercio-aportes-de-la-economia-del-comportamiento-y-la-opinion-publica-a-la-integracion, pages 54-69)

## Summary of article
A classic line of research in trade and international relations consists of identifying the factors that are decisive when it comes to explaining why certain people and countries
have more protectionist positions than others. What explains the differences in citizens' attitudes towards international trade and economic integration?

We know based on the information provided by Latinobarómetro (LB) - a survey of more than 20 thousand people in 18 Latin American countries - that the attitude of Latin Americans 
towards trade and regional economic integration is mostly favorable: 72% are very in favor or in favor in both cases. But what factors explain this high support? 

To try to answer these questions we estimated a series of Ordered Logit models to analyze the opinions of Latin Americans in favor or against regional economic integration. 

## Content of repository:
- "Latinobarometro_database.md": Description of LB survey and link to download full database.
- "Clean and prepare data.py": Python code to load, clean and transform data for statistic analysis and save it in csv format.
- "STATA Models dofile.do": STATA dofile to run a series of Ordered Logit and Logit models, including summary analysis of results and tables.
- Graphs folder: Includes all graphs saved from STATA analysis.

Analysis is based and adds on seminal work by Mayda y Rodrik (2001). “Why are some people (and countries) more protectionist than others?”, Working Paper 8461, National Bureau of 
Economic Research. Disponible en: https://www.nber.org/papers/w8461.pdf
