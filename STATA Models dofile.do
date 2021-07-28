import delimited using "C:\Users\bdeaz\PycharmProjects\createdb\Economics and financial analysis\Regression\LB2018_M1"

*Our dependent variable is ecoint, with values ranging from 1 to 4 (1 being "very against" regional economic integration and 4 being
*very in favor of regional economic integration).
*We use Ordered Logit models with country dummy variables.

*Model 1: "Naive model"
*As a first approximation, an analysis is carried out leaving aside economic theory. Support for trade is modeled simply using 
*basic sociodemographic variables: Age (edad), Gender (male), Citizenship (citizen) and Years of schooling (s10). This is our basic model.

quietly ologit ecoint edad s10 male citizen arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

mfx, predict(outcome(4)) varlist(edad s10 male citizen)

/*
Marginal effects after ologit
      y  = Pr(ecoint==4) (predict, outcome(4))
         =  .23004738
------------------------------------------------------------------------------
variable |      dy/dx    Std. Err.     z    P>|z|  [    95% C.I.   ]      X
---------+--------------------------------------------------------------------
    edad |   .0010892      .00017    6.55   0.000   .000763  .001415   40.0076
     s10 |   .0136697      .00068   20.22   0.000   .012345  .014994   10.3825
    male*|   .0584906      .00507   11.54   0.000    .04856  .068421   .492791
 citizen*|  -.0571222      .02595   -2.20   0.028   -.10799 -.006255   .986992
------------------------------------------------------------------------------
(*) dy/dx is for discrete change of dummy variable from 0 to 1

Table shows the estimated marginal effect on the probability of support for regional economic integration being the highest (ecoint==4), given an increase 
in the value of the relevant regressor, holding all other regressors at their mean value. We are focusing here on those that seem truly in favour of 
economic integration

RESULT INTERPRETATION: Support for integration is significantly greater at a younger age, at a higher educational level and among men (compared to women). 
Citizens tend to be les pro trade integration than immigrants.
The results confirm in particular the strong positive impact found on the relevant litterature of the level of education on support for trade openness and 
regional economic integration. Each additional year of formal education adds 1.4 percentage points to the probability of being very favorable towards 
integration.
Also in line with all previous literature, there is a strong gender bias or gender gap, for which the probability that women are in 
favor of regional economic integration is almost 6 percentage points lower than that of men.

To visualize better the marginal effect or years of education on opinions on economic integration, we plot margins of s10.
*/

quietly ologit ecoint edad i.s10 male citizen arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

margins s10, predict(outcome(4))

marginsplot

*See GRAPH 1 in folder.


*Model 2: Stolper-Samuelson

*International trade has important distributional consequences. 
*The Stolper-Samuelson theorem indicates that, assuming a cost-free intersectoral mobility of productive factors, trade and integration benefit individuals
*who possess the factors with which the economy is relatively well endowed, and hurts others. We model this idea by focusing on human capital, represented 
*by the years of schooling of each individual. In addition, using the GDP per capita as a proxy for the average level of human capital in each country, 
*we include an additional variable that combines the years of education of the respondent with the logarithm of the GDP per capita of the country (educgdp).

gen educgdp = s10*log(gdp)

quietly ologit ecoint edad s10 male citizen educgdp arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

mfx, predict(outcome(4)) varlist(edad s10 male citizen educgdp)

/*
Marginal effects after ologit
      y  = Pr(ecoint==4) (predict, outcome(4))
         =  .22986858
------------------------------------------------------------------------------
variable |      dy/dx    Std. Err.     z    P>|z|  [    95% C.I.   ]      X
---------+--------------------------------------------------------------------
    edad |    .001106      .00017    6.65   0.000    .00078  .001432   40.0076
     s10 |  -.0450647        .013   -3.47   0.001  -.070547 -.019583   10.3825
    male*|    .058764      .00507   11.60   0.000   .048836  .068692   .492791
 citizen*|   -.058155        .026   -2.24   0.025  -.109106 -.007204   .986992
 educgdp |   .0061791      .00137    4.52   0.000   .003501  .008857   99.8782
------------------------------------------------------------------------------
(*) dy/dx is for discrete change of dummy variable from 0 to 1

*RESULT INTERPRETATION: Results tend to suggest that relative human capital endowments influence opinion about trade and integration in line with the 
predictions of the Stolper-Samuelson theorem. Indeed, years of education is positively correlated with support for trade and integration in countries that 
are relatively well endowed with human capital (high GDP per capita), but weakly or negatively correlated with support for trade and integration in countries 
that are relatively poorly endowed with human capital (low GDP per capita). This is reflected in the signs of marginal effects for s10 and educgdp. 
However, literature on this suggests caution.

*/

clear


*Model 3: Social and economic status

import delimited using "C:\Users\bdeaz\PycharmProjects\createdb\Economics and financial analysis\Regression\LB2018_M3"

*Here we explore the relative income of individuals. Litterature suggests that individuals at the top end of the income distribution may be more supportive of
*trade and integration than those at the bottom. Although without an obvious correlate in international trade theories, this finding is consistent with an 
*empirical regularity of the last decades: the incidence of globalization (especially financial integration) in greater income inequality, both in rich 
*countries as well as developing.
*We incorporate variable clase_obj to the basic model.
*Variable ranges from 1 to 5, 1 if the person belongs to the bottom socioeconomic class and 5 the highest.

quietly ologit ecoint edad s10 male citizen clase_obj arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

mfx, predict(outcome(4)) varlist(edad s10 male citizen clase_obj)

/*
Marginal effects after ologit
      y  = Pr(ecoint==4) (predict, outcome(4))
         =  .23039737
------------------------------------------------------------------------------
variable |      dy/dx    Std. Err.     z    P>|z|  [    95% C.I.   ]      X
---------+--------------------------------------------------------------------
    edad |   .0010383      .00017    6.15   0.000   .000707  .001369   39.9735
     s10 |   .0119643      .00072   16.67   0.000   .010557  .013371    10.435
    male*|    .056754      .00513   11.06   0.000   .046695  .066813   .494679
 citizen*|  -.0620034      .02644   -2.35   0.019  -.113817  -.01019   .986919
clas~obj |   .0259759      .00327    7.95   0.000   .019573  .032379   3.52954
------------------------------------------------------------------------------
(*) dy/dx is for discrete change of dummy variable from 0 to 1

RESULT INTERPRETATION: As expected, the better relative socioeconomic position of the individual, the highest the probability of being very favourable 
to regional economic integration. 
*/

*Interestingly, when using instead self-perceived social class, the relation becomes less linear (see Graph 2).

quietly ologit ecoint edad s10 male citizen i.clase_obj i.clase_subj arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

margins clase_obj, predict(outcome(4))

marginsplot

margins clase_subj, predict(outcome(4))

marginsplot

*See GRAPHS 2a and 2b in folder.

clear


*Model 4: Role of values, knowledge and cosmpolitanism

import delimited using "C:\Users\bdeaz\PycharmProjects\createdb\Economics and financial analysis\Regression\LB2018_M4"

*This model seeks to capture the impact on attitudes towards trade and the integration of different values, such as community and regional attachment, 
*patriotism, nationalism and chauvinism. 
*We also include a variable ois that intends to capture the knowledge of international economic issues using people's knowledge about international financial
*organizations, such as the IMF and the World Bank. Variable ranges from 0 (no knowledge) to 4 (large knowledge).
*Recent litterature points that the level of education may be less important for opinions on trade than the exposure to economic information that some 
*particular studies provide.

quietly ologit ecoint edad s10 male citizen migration travel op_other nationalist polpar ois arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

mfx, predict(outcome(4)) varlist(edad s10 male citizen migration travel op_other nationalist polpar ois)

/*
Marginal effects after ologit
      y  = Pr(ecoint==4) (predict, outcome(4))
         =   .2414881
------------------------------------------------------------------------------
variable |      dy/dx    Std. Err.     z    P>|z|  [    95% C.I.   ]      X
---------+--------------------------------------------------------------------
    edad |   .0015538      .00023    6.81   0.000   .001107  .002001   38.4269
     s10 |   .0082723      .00097    8.52   0.000   .006369  .010176   11.0527
    male*|   .0376296      .00659    5.71   0.000   .024714  .050546   .538636
 citizen*|  -.0412872      .03261   -1.27   0.205  -.105199  .022624   .987037
migrat~n*|    .014808      .00764    1.94   0.053  -.000176  .029792   .308333
  travel*|   .0167383      .01109    1.51   0.131  -.004993   .03847   .113889
op_other |  -.1319607      .00662  -19.94   0.000  -.144932  -.11899   2.15924
nation~t*|  -.0358874       .0067   -5.36   0.000  -.049012 -.022762   .396886
  polpar*|   .0440926      .00706    6.24   0.000   .030254  .057931   .442761
     ois |   .0324082      .00254   12.75   0.000   .027428  .037389   1.79158
------------------------------------------------------------------------------
(*) dy/dx is for discrete change of dummy variable from 0 to 1


RESULT INTERPRETATION: We find that a high degree of nationalism has a negative impact on support for integration. 
The cosmopolitan factors also play an important role: those who travel abroad frequently and those who have thought about migrating are more supportive 
of integration. 
Similarly, having generally negative opinions about the rest of the world (op_other variable) decreases by 13% the probability of having a very 
favourable opinion about regional economic integration.
The feeling of belonging to a party or political (polpar) has a significant and positive impact, no matter the ideological color, suggesting that
support for regional economic integration in Latin America may not be strongly associated with a particular political force or a specific ideology.

Finally, our proxy to knowledge of international economics is also very significant. The probability of being very in favour of economic integration
increases in our model from 20% if ois == 0 to above 30% is ois == 3 or == 4 (see GRAPH 3).
*/

quietly ologit ecoint edad s10 male citizen migration travel op_other nationalist polpar i.ois arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven 

margins ois, predict(outcome(4))

marginsplot

*See GRAPH 3 in folder.

clear


*Model 5: Anxiety and econommic expectations

import delimited using "C:\Users\bdeaz\PycharmProjects\createdb\Economics and financial analysis\Regression\LB2018_M5"

*Finally, the last model is based on an idea by Mansfield, Mutz and Brackbill (2016), who introduce a new aspect in the litterature related to expectations
*and anxiety. The question they attempt to answer is why did the American public become more trade protectionist during the 2007-2009 crisis? 
*The results of their analysis suggest that the shift in views on trade was due more to an emotional reaction than to a conscious reassessment of the
*merits of trade. Sentiments of anxiety, concern for the future and aversion to risk led to a more protectionist opinion.

*To test this hypothesis in the region, we build a model including some variables related to people's expectations: a variable (P8STGBSC) that identifies people who 
*expect the country's economic situation to worsen in the next 12 months and another variable (P9STGBSC) that identifies people who expect that their 
*personal economic situation will get worse in the next 12 months. 
*We also include a variable (unemfear)that identifies people who are worried about losing their job in the next 12 months.

quietly ologit ecoint edad s10 male citizen unemfear p8stic p9stgbsc arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

mfx, predict(outcome(4)) varlist(edad s10 male citizen unemfear p8stic p9stgbsc)

/*
Marginal effects after ologit
      y  = Pr(ecoint==4) (predict, outcome(4))
         =  .23094173
------------------------------------------------------------------------------
variable |      dy/dx    Std. Err.     z    P>|z|  [    95% C.I.   ]      X
---------+--------------------------------------------------------------------
    edad |   .0011554      .00018    6.36   0.000   .000799  .001512   39.5829
     s10 |   .0133734      .00073   18.39   0.000   .011948  .014799   10.5673
    male*|   .0564491       .0054   10.45   0.000   .045857  .067041   .501766
 citizen*|  -.0556544      .02683   -2.07   0.038  -.108249 -.003059   .986236
unemfear*|   -.011043      .00558   -1.98   0.048  -.021975 -.000111   .443057
  p8stic |  -.0202314      .00284   -7.13   0.000  -.025794 -.014669   3.06523
p9stgbsc |  -.0155018      .00306   -5.07   0.000  -.021491 -.009512   2.64129
------------------------------------------------------------------------------
(*) dy/dx is for discrete change of dummy variable from 0 to 1

RESULT INTERPRETATION: Greater concern about the future (proxied by all three variables) seems to significantly reduce support for regional economic integration. 
Although the analysis does not allow to be conclusive, it could suggest that greater anxiety about the future generates an almost emotional impulse against 
integration and in favor of a sense of security associated with protectionism.
This is relevant in a regional context of deep structural change. The stagnation of economic growth and the interruption and in some cases reversal of the 
process of poverty reduction and development of the middle classes in the region are some aspects that could generate anxiety and end up affecting support 
for integration and trade.
 
*/

quietly ologit ecoint edad s10 male citizen unemfear i.p8stic i.p9stgbsc arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

margins p8stic, predict(outcome(4)) 

marginsplot

margins p9stgbsc, predict(outcome(4))

marginsplot

*See GRAPHS 4a and 4b in folder.


/*
Some concluding remarks:
Exposure to economic ideas, sociodemographic characteristics, values and even emotions seem to be very relevant when explaining opinions 
about trade and economic integration. This does not necessarily mean that individuals are behaving irrationally. In fact, in a world integrated in 
increasingly complex ways, unless individuals feel the benefits and costs of integration directly and clearly, they may well have only non-economic signals 
to turn to to form opinions. Values, affinities, ideological and partisan stances, emotions, and other hard-to-measure variables can exert a powerful 
influence on preferences. 

This would explain, at least in part, why our analysis, once all the significant variables are added in a summary model presented below, only manages to 
explain around 12% of the variation in the attitudes of Latin Americans towards regional economic integration.
*/

clear

import delimited using "C:\Users\bdeaz\PycharmProjects\createdb\Economics and financial analysis\Regression\LB2018_M6"

gen educgdp = s10*log(gdp)

regress ecoint edad s10 male clase_obj op_other nationalist polpar ois p8stic p9stgbsc arg bol bra chi col costar repdom ecu elsal gua hon mex nic pan par per uru ven

/*

      Source |       SS       df       MS              Number of obs =   10872
-------------+------------------------------           F( 27, 10844) =   54.05
       Model |  818.552491    27  30.3167589           Prob > F      =  0.0000
    Residual |  6081.89306 10844  .560853288           R-squared     =  0.1186
-------------+------------------------------           Adj R-squared =  0.1164
       Total |  6900.44555 10871  .634757202           Root MSE      =   .7489

------------------------------------------------------------------------------
      ecoint |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        edad |   .0024017   .0005033     4.77   0.000     .0014151    .0033883
         s10 |   .0153647   .0022054     6.97   0.000     .0110417    .0196877
        male |   .0665976   .0146445     4.55   0.000     .0378916    .0953035
   clase_obj |   .0401105   .0094324     4.25   0.000     .0216212    .0585997
    op_other |  -.2646218   .0142101   -18.62   0.000    -.2924762   -.2367674
 nationalist |   -.087473   .0150154    -5.83   0.000    -.1169059   -.0580401
      polpar |     .06908   .0153313     4.51   0.000     .0390279    .0991322
         ois |   .0630187   .0055443    11.37   0.000     .0521508    .0738866
      p8stic |  -.0372351    .007586    -4.91   0.000    -.0521049   -.0223652
    p9stgbsc |  -.0240808   .0081086    -2.97   0.003    -.0399752   -.0081863

	
Model includes dummies for countries.

*/
