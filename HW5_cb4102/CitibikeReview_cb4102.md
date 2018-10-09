
### Colin Bradley Reviewing Tanya Nabila's CitiBike Hypothesis



### Intructions from Assignment:

##### a. verify that their Null and alternative hypotheses are formulated correctly

##### b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

##### c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

##### Write your comments, suggestions, and suggested an appropriate statistical test, motivating your test choice, in a markdown named CitibikeReview_<netID>.md 
##### Suggest variations on the question, if you think it may be made more interesting.

### Response:

#### A) Tanya's research idea was to explore whether subscribed CitiBike users use the service more as a daily commute option. Based on her month of choice (September 2018) and her rationale for choosing this month (studnets in school), I assume that commute refers to getting to work or school during the weekdays. 

#### Tanya has formed the null and alternative hypotheses correctly, however, I think there is a potential opportunity for more precision in how the null hypothesis relates to the idea being explored. Tanya's hypothesis compares the ratio of weekday subscriber usage to weekend subscriber usage. This really just answers whether subscribed users use the service more during the week, but doesn't necessarily get at whether they use it for their daily commute. Testing whether a subscribed user was using the service monday-Fri, or at least x times per weekday vs. weekend usage would be more precise (however, this is not possible from the data because we don't have subscriber id). Another way to add precision might be to add in a dimension that uses starttime and stoptime from the data set since a large share of commutes (at least for those going to work) happen during specific hours of the day.

#### The other potential issue with the approach is that using subscriber usage ratios can also be impacted by other types of riders. A potential bias could be introduced if on the weekends there are a higher share of tourists or weekend visitors to the city using the CitiBike service. In this case it might seem like subscriber usage ratios are lower, thus perhaps rejecting the null hypothesis, however it's due to activity from other user groups.

#### Overall it is still a good hypothesis test given the data available.

#### B) Yes, the raw data has the required information to answer the question and Tanya has pre-processed it correctly. The primary pre-processing step she had to do was convert the starttime column and extract the day of the week, which she has done efficiently. She goes a step further and aggregates the data to the level required for the hypothesis test and adds subscriber and customer usage ratios. These ratios are calculated correctly.


#### C) Given the data available and the approach Tanya has taken to pre-process the data, it is possible to use two columns she created - 'subs-ratio' and 'cust-ratio' by day of week - to test the null hypothesis.  

#### Given the null hypothesis: Null Hypothesis:
#### The ratio of subscribed users will be the same or lower during the weekdays compared to ratio of subscribed users in the weekends.

#### I would take the average of 'subs-ratio' for weekdays (monday - friday) and compare it to the average of 'subs-ratio' for the weekends (saturday - sunday) and compare the two values. If avg('subs-ratio' weekday) > avg('subs-ratio' weekend) then we would be able to reject the null hypothesis. 