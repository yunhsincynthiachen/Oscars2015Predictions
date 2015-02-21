# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 13:17:03 2015

@author: ychen1
"""

from pattern.web import *
from pattern.en import *
import matplotlib.pyplot as plt

def oscarsmoviestwittersearch(textfile,dict_stuff):
    """ This function, which we only run once, produces a set of tweets that we can work with in a plaintext
    file. The output of this function is a file containing all of our tweets, separated by /n """
    L = []
    L2 = []
    t = Twitter()
    for key in dict_stuff:  #loops through all the keys in the dictionary, searching tweets for movie titles and words "Oscars", "will", and "win"
        for tweet in t.search(key + ' ' + dict_stuff[key]):
            L.append(tweet.text)
            L2.append(sentiment(tweet.text))

    file = open(textfile,'w') #opens a new file, writes all of our tweets to this file, and closes file
    for i in L:
        file.write(str(i)+'\n')
    file.close()
    
def openbestfiletweets(textfile):
    """ This function opens the plaintext file and outputs it as a varaible that can be called"""
    with open(textfile,'r') as myfile:
        data = myfile.readlines()
    return data
    
def makingtweetslowercase(data):
    """This helps us search through all of the tweets by making all of the text in the tweets lowercase. The 
    function also creates a list of all our tweets which makes it easy for us to loop through them and search
    for the relevant information we need"""
    tweets = []
    for i in range(len(data)):
        tweets.append(data[i].lower())  #so we simultaneously make all of the tweets lowercase while appending them to a list
    return tweets

def finding_sentiment_analysis(index, lower_case_list):
    """ This function takes as input a list of all the indices for the tweets which mentioned the relevant movie
    and the full data-set of tweets. Then, using the indices it has found, it produces the indvidual sentiments
    of each relevant tweet. """
    sent_index = []
    for j in index: #loops through all the relevant tweets that pertain to each movie, find the sentiment analysis, and append it to a list
        sent_index.append((sentiment(lower_case_list[j])))
    return sent_index

def finding_tot_sentiment_for_movie(sent_index):
    """ This function takes as input the list of all of the sentiments, takes only the first sentiment value which
    indicates the postivity or negatviity of the tweet, and sums all of the sentiments """
    tot_sent = 0    #initializes starting value for total sentiment for each movie at 0
    for i in sent_index:
        tot_sent += i[0]
    return tot_sent
    
##############################################################################################################

if __name__ == "__main__":
    oscarsmovievalue = '\"oscars\"will win';
    oscarsactorvalue = '\"oscars\"will win';
    oscarsactressvalue = '\"oscars\"will win';
    oscarssupportactorvalue = '\"oscars\"best supporting actor\"will win';
    oscarssupportactressvalue = '\"oscars\"will win';
    oscarsdirectorvalue = '\"oscars\"will win';
    oscarsscorevalue = '\"oscars\"score\"will win';
    oscarssongvalue = '\"oscars\"song\"will win';
    oscarsforeignvalue = '\"oscars\"will win';
    oscarsadaptedvalue = '\"oscars\"screenplay\"will win';
    oscarsoriginalvalue = '\"oscars\"screenplay\"will win';
    
    oscarbestmovie = {'\"american sniper\"':oscarsmovievalue,
               '\"birdman\"':oscarsmovievalue, 
               '\"boyhood\"':oscarsmovievalue, 
               '\"grand budapest hotel\"':oscarsmovievalue, 
               '\"imitation game\"':oscarsmovievalue,
               '\"selma\"':oscarsmovievalue,
               '\"theory of everything\"':oscarsmovievalue, 
               '\"whiplash\"':oscarsmovievalue}
               
    oscarbestactor = {'\"steve carell\"':oscarsactorvalue,
               '\"bradley cooper\"':oscarsactorvalue, 
               '\"benedict cumberbatch\"':oscarsactorvalue, 
               '\"michael keaton\"':oscarsactorvalue, 
               '\"eddie redmayne\"':oscarsactorvalue}
               
    oscarbestactress = {'\"marion cotillard\"':oscarsactressvalue, 
               '\"felicity jones\"':oscarsactressvalue, 
               '\"julianne moore\"':oscarsactressvalue,
               '\"rosamund pike\"':oscarsactressvalue, 
               '\"reese witherspoon\"':oscarsactressvalue}
              
    oscarbestactorsupport = {'\"robert duvall\"':oscarssupportactorvalue,
               '\"ethan hawke\"':oscarssupportactorvalue, 
               '\"edward norton\"':oscarssupportactorvalue, 
               '\"mark ruffalo\"':oscarssupportactorvalue, 
               '\"jk simmons\"':oscarssupportactorvalue}
    
    oscarbestactresssupport = {'\"patricia arquette\"':oscarssupportactressvalue,
               '\"laura dern\"':oscarssupportactressvalue, 
               '\"keira knightley\"':oscarssupportactressvalue, 
               '\"emma stone\"':oscarssupportactressvalue, 
               '\"meryl streep\"':oscarssupportactressvalue}
    
    oscarbestdirector = {'\"alejandro\"':oscarsdirectorvalue,
               '\"richard linklater\"':oscarsdirectorvalue, 
               '\"bennett miller\"':oscarsdirectorvalue, 
               '\"wes anderson\"':oscarsdirectorvalue, 
               '\"morten tyldum\"':oscarsdirectorvalue}
               
    oscaranimated = {'\"big hero 6\"':oscarsdirectorvalue,
               '\"boxtrolls\"':oscarsdirectorvalue, 
               '\"how to train your dragon 2\"':oscarsdirectorvalue, 
               '\"song of the sea\"':oscarsdirectorvalue, 
               '\"tale of the princess kaguya\"':oscarsdirectorvalue}

    oscarscore = {'\"grand budapest hotel\"':oscarsscorevalue,
               '\"imitation game\"':oscarsscorevalue, 
               '\"interstellar\"':oscarsscorevalue, 
               '\"mr. turner\"':oscarsscorevalue, 
               '\"theory of everything\"':oscarsscorevalue}

    oscarsong = {'\"lego movie\"':oscarssongvalue,
               '\"selma\"':oscarssongvalue, 
               '\"beyond the lights\"':oscarssongvalue, 
               '\"glen campbell\"':oscarssongvalue, 
               '\"begin again\"':oscarssongvalue}
    
    oscarforeign = {'\"ida\"':oscarsforeignvalue,
               '\"leviathan\"':oscarsforeignvalue, 
               '\"tangerines\"':oscarsforeignvalue, 
               '\"timbuktu\"':oscarsforeignvalue, 
               '\"wild tales\"':oscarsforeignvalue}
               
    oscaradapted = {'\"american sniper\"':oscarsadaptedvalue,
               '\"imitation game\"':oscarsadaptedvalue, 
               '\"inherent vice\"':oscarsadaptedvalue, 
               '\"theory of everything\"':oscarsadaptedvalue, 
               '\"whiplash\"':oscarsadaptedvalue}
               
    oscaroriginal = {'\"birdman\"':oscarsoriginalvalue,
               '\"boyhood\"':oscarsoriginalvalue, 
               '\"foxcatcher\"':oscarsoriginalvalue, 
               '\"grand budapest hotel\"':oscarsoriginalvalue, 
               '\"nightcrawler\"':oscarsoriginalvalue}
               
    oscarss = [oscarbestmovie,oscarbestactor,oscarbestactress,oscarbestactorsupport,oscarbestactresssupport,oscarbestdirector,oscaranimated, oscarscore,oscarsong,oscarforeign,oscaradapted,oscaroriginal]    #initializes a dictionary that we can use to search through Twitter for

    textfiles = ['bestmovietweets.txt','bestactortweets.txt','bestactresstweets.txt','bestactorsupporttweets.txt','bestactresssupporttweets.txt','bestdirectortweets.txt','bestanimatedfilm.txt','bestscore.txt','bestsong.txt','bestforeign.txt','bestadapted.txt','bestoriginal.txt']
    
    lists = []
    for i in textfiles:
        #oscarsmoviestwittersearch(i,oscarss[textfiles.index(i)])
        lists.append(makingtweetslowercase(openbestfiletweets(i))) #lower_case_list contains all of the tweets, in lowercase, in a list
    
    #we initialize a bunch of empty lists to store the indices of each tweet that contain any of these movie names
    sizes = []
    sumofsentiments = 0
    
    all_index2 = [[],[],[],[],[],[],[],[]]
    all_index = [[],[],[],[],[]] ####need to change index name
    all_sent_oscars = []
    movie_names = ['american sniper','birdman','boyhood','grand budapest hotel','imitation game','selma','theory of everything','whiplash']
    actor_names = ['steve carell','bradley cooper','benedict cumberbatch','michael keaton','eddie redmayne']
    actress_names = ['marion cotillard','felicity jones','julianne moore','rosamund pike','reese witherspoon']
    actorsupport_names = ['robert duvall','ethan hawke','edward norton','mark ruffalo','simmons']
    actresssupport_names = ['patricia arquette','laura dern','keira knightley','emma stone','meryl streep']
    director_names = ['alejandro','richard linklater','bennett miller','wes anderson','morten tyldum']
    animated_names = ['big hero 6', 'boxtrolls','how to train your dragon 2','song of the sea', 'tale of the princess kaguya']
    score_names = ['grand budapest hotel','imitation game','interstellar','mr. turner','theory of everything']
    song_names = ['lego movie','selma','beyond the lights','glen campbell','begin again'] 
    foreign_names = ['ida','leviathan','tangerines','timbuktu','wild tales']
    adapted_names = ['american sniper','imitation game','inherent vice','theory of everything','whiplash']
    originalscreenplay_names = ['birdman','boyhood','foxcatcher','grand budapest hotel','nightcrawler']
    
    for name in originalscreenplay_names: ####need to change list name
        for i in range(len(lists[11])): ####need to change index number
            if name in lists[11][i]: #n###eed to change index number
                all_index[originalscreenplay_names.index(name)].append(i) ####need to change list name

    for i in range(len(all_index)):
        all_sent_oscars.append(finding_tot_sentiment_for_movie(finding_sentiment_analysis(all_index[i], lists[11]))) ####need to change index number

    
    #using matplotlib to produce a pie chart of the probabilities of each movie to win Best Picture for the Oscars
    sum_name_list = []    
    for sum_name in all_sent_oscars:
        if sum_name < 0:
            sum_name_list.append(-sum_name)
        else:
            sum_name_list.append(sum_name)
            
    print sum_name_list
    
    for name in sum_name_list:
        sumofsentiments += (name)/100
    
    for size_name in sum_name_list:
        sizes.append(size_name/sumofsentiments)
    
    
    
    labels = ['American Sniper','Birdman','Boyhood','The Grand Budapest Hotel','The Imitation Game','Selma','Theory of Everything','Whiplash']
    labels1 = ['Steve Carell','Bradley Cooper','Benedict Cumberbatch','Michael Keaton','Eddie Redmayne']
    labels2 = ['Marion Cotillard','Felicity Jones','Julianne Moore','Rosamund Pike','Reese Witherspoon']
    labels3 = ['Robert Duvall','Ethan Hawke','Edward Norton','Mark Ruffalo','J.K. Simmons']
    labels4 = ['Patricia Arquette','Laura Dern','Keira Knightley','Emma Stone','Meryl Streep']
    labels5 = ['Alejandro G. Inarritu','Richard Linklater','Bennett Miller','Wes Anderson','Morten Tyldum']
    labels6 = ['Big Hero 6','The Boxtrolls','How to Train Your Dragon 2','Song of the Sea','The Tale of the Princess Kaguya']    
    labels7 = ['The Grand Budapest Hotel','The Imitation Game','Interstellar','Mr. Turner','Theory of Everything']
    labels8 = ['Everything is Awesome','Glory','Grateful','I am Not Gonna Miss You','Lost Stars']
    labels9 = ['Ida','Leviathan','Tangerines','Timbuktu','Wild Tales']    
    labels10 = ['American Sniper','The Imitation Game','Inherent Vice','Theory of Everything','Whiplash']
    labels11 = ['Birdman','Boyhood','Foxcatcher','The Grand Budapest Hotel','Nightcrawler']
    
    colors = ['yellowgreen','gold','orange','red','lightskyblue','blue','lightcoral','purple']
    colors1 = ['yellowgreen','gold','orange','red','lightskyblue']  
    font = {'size':12}    
    plt.rc('font',**font)
    plt.pie(sizes,labels=labels11,colors=colors1,autopct='%1.1f%%') #change labels and colors
    plt.axis('equal')
    plt.show()
    
