# Overview of Election Audit

The purpose of election audit is to see if using python to write a script for automating the process of counting votes is better than using traditional means, like Excel.

### Results of Election-Audit

* In this election there were a total of 369,711 votes cast
   * To find this we used the code: `for row in reader: total_votes = total_votes + 1)`, this tells the script that every row in the results file is a vote cast and that the total votes will increase by one vote as it goes down the rows until the end of the file
 
* For each county in the precinct:
    * Jefferson had 38,855 votes which was 10.5% of all votes
    * Denver residents cast 306,055 votes resulting in 82.8% of the votes 
    * Arapahoe county had 24,801 votes which was 6.7% of the total votes
    
* Denver County had the highest turn out of all counties for the election

* Candidates of the election received the following:
    * Charles Casper Stockham: 23.0% (85,213) of the total votes
    * Diana DeGette: 73.8% (272,892) of the total votes
    * Raymon Anthony Doane: 3.1% (11,606) of the total votes
    
* The winner of the election with 73.8% of the total vote (272,892 total votes) was Diana DeGette


## Election-Audit Summary

The script effectively read the election results raw data, collected the necessary information, reworked the data, and wrote a new file to deliver the results of the election in a clear and concise way. After writing this script it is clear to see that this can be used for any election within the state or country at large. There are a couple things that need to be modified before being bale to effectively use this for more applications. The first modification that would need to be necessart would be to build in a new for loop it incorporate addition disctricts and their votes. This would be able to give us the entire state's data for any election. This same script could be used for not just candidates, but also for bills and proposals on the doceket. For this to happen we would need to add new variables for each new proposal as well as new loopsto colect the information. These modifications would then need to be written into the analysis file using the `file.write()` code.
