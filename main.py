import json
import datetime 
import matplotlib.pyplot as plt

class spotifyAnalyser:

    def __init__(self, dataset_path) -> None:
        with open(dataset_path,'r', encoding="utf8") as json_read_data:
            self.spotify_data = json.load(json_read_data)

            
############################################ HELPER FUNCTIONS(for conversion) ######################################

    def string_to_datetimeobject(self, endtimeString):
    #This function will convert an input endTime string in the data into a datetime object 
        dateTime_object = datetime.datetime.strptime(endtimeString,'%Y-%m-%dT%H:%M:%SZ')
        return dateTime_object


    def convert_ms_to_readable_units(self,total_listening_time_ms):
        #check if it will equate to more than one minute 
        if total_listening_time_ms >= 60000 and total_listening_time_ms <3.6*10**6:
            total_listening_time_m = total_listening_time_ms/(60000) 
            return [total_listening_time_m,'minute']

        #check if it will equate to more than one hour 
        if total_listening_time_ms >= 3.6*10**6 and total_listening_time_ms < 8.64*10**7:
            total_listening_time_h = total_listening_time_ms/(3.6*10**6) 
            return [total_listening_time_h,'hour'] 

        #check if it will equate to more than one day
        if total_listening_time_ms >= 8.64*10**7 and total_listening_time_ms < 6.048*10**8:
            total_listening_time_d = total_listening_time_ms/(8.64*10**7) 
            return [total_listening_time_d,'day'] 

        #check if it will equate to more than one week 
        if total_listening_time_ms >= 6.048*10**8:
            total_listening_time_w = total_listening_time_ms/(6.048*10**8) 
            return [total_listening_time_w,'week'] 


    def convert_ms_to_readable_units_for_plotting(self, total_listening_time_ms, unit):
        #This will convert ms to hours, minutes, seconds for plotting purposes 
        #unit is the unit you want to convert to

        if unit == 'week':
            total_listening_time_w = total_listening_time_ms/(6.048*10**8) 
            return total_listening_time_w
        
        if unit == 'day':
            total_listening_time_d = total_listening_time_ms/(8.64*10**7) 
            return total_listening_time_d

        if unit == 'hour':
            total_listening_time_h = total_listening_time_ms/(3.6*10**6) 
            return total_listening_time_h
        if unit == 'minute':
            total_listening_time_m = total_listening_time_ms/(60000) 
            return total_listening_time_m
        if unit == 'second':
            total_listening_time_s = total_listening_time_ms/(1000) 
            return total_listening_time_s


    ############################################ META DATA ######################################

    def number_of_songs(self):
        print(len(self.spotify_data))
        return len(self.spotify_data)

    def print_number_of_songs(self):
        return str(f'The total number of songs in this dataset is: {self.number_of_songs()}')

    def number_of_unique_songs(self):
        pass 

    def total_listening_time(self):
        #This will return the total listening time of the dataset being looked at. 
        #This will use big spotify Data
        total_listening_time_ms = 0 
        for i in range(len(self.spotify_data)):
            total_listening_time_ms += self.spotify_data[i]['ms_played']
        return self.convert_ms_to_readable_units(total_listening_time_ms)


    def print_total_listening_time(self):
        total_listening_time = self.total_listening_time()

        if total_listening_time[1] == 'minute':
            print (f'"The total listening time of the entire dataset is {total_listening_time[0]} minutes.')
            return (f'"The total listening time of the entire dataset is {total_listening_time[0]}  minutes.')

        if total_listening_time[1] == 'hour':
            print (f'"The total listening time of the entire dataset is {total_listening_time[0]}  hours.')
            return (f'"The total listening time of the entire dataset is {total_listening_time[0]}  hours.')

        if total_listening_time[1] == 'day':
            print (f'"The total listening time of the entire dataset is {total_listening_time[0]}  days.')
            return (f'"The total listening time of the entire dataset is {total_listening_time[0]}  days.')

        if total_listening_time[1] == 'week':
            print (f'"The total listening time of the entire dataset is {total_listening_time[0]}  weeks.')
            return (f'"The total listening time of the entire dataset is {total_listening_time[0]}  weeks.')


    def most_recent_song(self):
    #This function will return the most recent song played in the dataset
        mostRecentDate = self.spotify_data[0]["ts"] #assign random data 
        mostRecentSong = self.spotify_data[0]["master_metadata_track_name"]
        for i in range(len(self.spotify_data)): #the data isn't ordered, so this basically iterates through the entire list to find the most recent song
            if self.spotify_data[i]["ts"] > mostRecentDate:
                mostRecentDate = self.spotify_data[i]["ts"]
                mostRecentSong = self.spotify_data[i]["master_metadata_track_name"]
        return [mostRecentSong, mostRecentDate] 
 
    def least_recent_song(self):
    #This function will return the least recent song played in the dataset, the exact opposite of the above funciton. 
        leastRecentDate = self.spotify_data[0]["ts"]
        leastRecentSong = self.spotify_data[0]["master_metadata_track_name"]
        for i in range(len(self.spotify_data)):
            if self.spotify_data[i]["ts"] < leastRecentDate:
                leastRecentDate = self.spotify_data[i]["ts"]
                leastRecentSong = self.spotify_data[i]["master_metadata_track_name"]
        return [leastRecentSong,leastRecentDate] 
 

    def time_between_most_and_least_recent_songs(self):
    #This function will calculate the amount of dates that have passed between two dates 
        time_passed_btw_mostleastrecent_song = self.string_to_datetimeobject(self.most_recent_song()[1]) - self.string_to_datetimeobject(self.least_recent_song()[1])
        
        return time_passed_btw_mostleastrecent_song


    def print_time_between_most_and_least_recent_songs(self):
        newline = '\n'
        stringDump = str(f'The most recent song was: {self.most_recent_song()} {newline}The least recent song was: {self.least_recent_song()} {newline}The time that has passed between these two songs is {self.time_between_most_and_least_recent_songs()}')

        print('The most recent song was: ', self.most_recent_song(),
            '\n The least recent song was:', self.least_recent_song(),
            '\n The time that has passed between these two songs is ', self.time_between_most_and_least_recent_songs() 
             )
        return stringDump


    def count_number_of_unique_artists(self): 
        #This will return the number of unique artists in the dataset
        #first sort your list by artist name
        sorted_list_by_artist = self.sort_based_on_artist_name()
        #then iterate through the list and count the number of unique artists 
        count = 0 
        for i in range(len(sorted_list_by_artist)):
            if sorted_list_by_artist[i]["master_metadata_album_artist_name"] != sorted_list_by_artist[i-1]["master_metadata_album_artist_name"]:
                count += 1
        return count

    def print_number_of_unique_artists(self):
        print(f'The number of unique artists in this dataset is {self.count_number_of_unique_artists()}')
        return f'The number of unique artists in this dataset is {self.count_number_of_unique_artists()}'

    def count_number_of_artist_listens(self):
        #This will return the number of times an artist has been listened to 
        #first sort your list by artist name
        sorted_list_by_artist = self.sort_based_on_artist_name()
        #then iterate through the list and count the number of unique artists 
        count = 0 
        artist_listens = []
        for i in range(len(sorted_list_by_artist)):
            if sorted_list_by_artist[i]["master_metadata_album_artist_name"] != sorted_list_by_artist[i-1]["master_metadata_album_artist_name"]:
                artist_listens.append([sorted_list_by_artist[i]["master_metadata_album_artist_name"],1])
            else:
                artist_listens[-1][1] += 1
        return artist_listens

    def print_number_of_artist_listens(self, filename):
        # print(f'The number of artist listens in this dataset is {self.count_number_of_artist_listens()}')
        artist_listens = self.count_number_of_artist_listens() 

        with open(filename, 'wb') as f:
            for item in artist_listens:
                f.write(('\t'.join(str(i) for i in item) + '\n').encode('utf-8'))
    

    def top10_most_listened_to_artists(self):
        #This will return the top 10 most listened to artists in the dataset 
        artist_listens = self.count_number_of_artist_listens()
        artist_listens.sort(key=lambda x: x[1], reverse=True)

        #then find the artist with the highest number of listens 
        top10_most_listened_to_artists = []
        for i in range(10):
            top10_most_listened_to_artists.append(artist_listens[i])
        return top10_most_listened_to_artists

    def print_top10_most_listened_to_artists(self):
        print(f'The top 10 most listened to artists in this dataset is {self.top10_most_listened_to_artists()}')
        return f'The top 10 most listened to artists in this dataset is {self.top10_most_listened_to_artists()}'


    def count_number_of_albums_listened_to(self):
        #This will return the number of albums listened to 
        #first sort your list by artist name
        sorted_list_by_artist = self.sort_based_on_album_name()
        #then iterate through the list and count the number of unique artists 
        count = 0 
        album_listens = []
        for i in range(len(sorted_list_by_artist)):
            if sorted_list_by_artist[i]["master_metadata_album_album_name"] != sorted_list_by_artist[i-1]["master_metadata_album_album_name"]:
                album_listens.append([sorted_list_by_artist[i]["master_metadata_album_album_name"],1])
            else:
                album_listens[-1][1] += 1
        return album_listens

    def top20_most_listened_to_albums(self):
        #This will return the top 20 most listened to albums in the dataset 
        album_listens = self.count_number_of_albums_listened_to()
        album_listens.sort(key=lambda x: x[1], reverse=True)

        #then find the artist with the highest number of listens
        top20_most_listened_to_albums = []
        for i in range(20):
            top20_most_listened_to_albums.append(album_listens[i])
        return top20_most_listened_to_albums

    def print_top20_most_listened_to_albums(self):
        print(f'The top 20 most listened to albums(this counts each time a song is played from this album) in this dataset is {self.top20_most_listened_to_albums()}')
        return f'The top 20 most listened to albums(this counts each time a song is played from this album) in this dataset is {self.top20_most_listened_to_albums()}'

    def count_number_of_song_listens(self):
        #This will return the number of times a song has been listened to 
        #first sort your list by artist name
        sorted_list_by_artist = self.sort_based_on_song_name()
        #then iterate through the list and count the number of unique artists 
        count = 0 
        song_listens = []
        for i in range(len(sorted_list_by_artist)):
            if sorted_list_by_artist[i]["master_metadata_track_name"] != sorted_list_by_artist[i-1]["master_metadata_track_name"]:
                song_listens.append([sorted_list_by_artist[i]["master_metadata_track_name"],1])
            else:
                song_listens[-1][1] += 1
        return song_listens

    def top30_most_listened_to_songs(self):
        #This will return the top 10 most listened to songs in the dataset 
        song_listens = self.count_number_of_song_listens()
        song_listens.sort(key=lambda x: x[1], reverse=True)

        #then find the artist with the highest number of listens
        top30_most_listened_to_songs = []
        for i in range(30):
            top30_most_listened_to_songs.append(song_listens[i])
        return top30_most_listened_to_songs
    
    def print_top30_most_listened_to_songs(self):
        print(f'The top 30 most listened to songs in this dataset is {self.top30_most_listened_to_songs()}')
        return f'The top 30 most listened to songs in this dataset is {self.top30_most_listened_to_songs()}'


    def listening_time_by_year(self):
        songs_sorted_by_date = self.sort_based_on_datetime()
        #This will create a dictionary with the years as keys and the total listening time as values
        listening_time_by_year = {}
        for i in range(len(songs_sorted_by_date)):
            if songs_sorted_by_date[i]["ts"][0:4] in listening_time_by_year:
                listening_time_by_year[songs_sorted_by_date[i]["ts"][0:4]] += songs_sorted_by_date[i]["ms_played"]
            else:
                listening_time_by_year[songs_sorted_by_date[i]["ts"][0:4]] = songs_sorted_by_date[i]["ms_played"]
        return listening_time_by_year

    def print_listening_time_by_year(self):
        listening_time_by_year = self.listening_time_by_year()
        for key in listening_time_by_year.keys():
            listening_time_by_year[key] = self.convert_ms_to_readable_units(listening_time_by_year[key])
        return f'The listening time by year is {listening_time_by_year}'

    def listening_time_by_month(self):
        #This will create a dictionary with the months as keys and the total listening time as values
        songs_sorted_by_date = self.sort_based_on_datetime()
        listening_time_by_month = {}
        for i in range(len(songs_sorted_by_date)):
            if songs_sorted_by_date[i]["ts"][0:7] in listening_time_by_month:
                listening_time_by_month[songs_sorted_by_date[i]["ts"][0:7]] += songs_sorted_by_date[i]["ms_played"]
            else:
                listening_time_by_month[songs_sorted_by_date[i]["ts"][0:7]] = songs_sorted_by_date[i]["ms_played"]
        return listening_time_by_month
    
    def print_listening_time_by_month(self):
        listening_time_by_month = self.listening_time_by_month()
        for key in listening_time_by_month.keys():
            listening_time_by_month[key] = self.convert_ms_to_readable_units(listening_time_by_month[key])
        return f'The listening time by month is {listening_time_by_month}'

    def average_daily_listening_time(self):
    #This will require you to sort your list 
    #Then you will have to calculate your average listening time for each specific day 
    #then you will have to calculate the average of all of those days 
        pass 

    def average_daily_listening_time_for_specific_day(self):

        pass 


############################################ INTERVALS ######################################
    def total_listening_time_over_interval(self, datetime1, datetime2):
    #This function will take as an input 2 datetimes, and calculate the exact amount of music listened between these two intervals 
    #This will output the total listening time over those two intervals 
    #(without sorting)This function will make do a comparison for each datapoint to check if it's above or below the given datetime, and if so, it will increment the total to return   
    #This will expect an input that adheres to self.string_to_datetimeobject format: '%Y-%m-%dT%H:%M:%SZ'
        total_listening_time = 0 
        count_songs = 0 
        for i in range (len(self.spotify_data)):
            if self.string_to_datetimeobject(self.spotify_data[i]["ts"]) >= self.string_to_datetimeobject(datetime1) and self.string_to_datetimeobject(self.spotify_data[i]["ts"])<= self.string_to_datetimeobject(datetime2): 
                total_listening_time += self.spotify_data[i]["ms_played"]
                count_songs +=1
        return_object = [self.convert_ms_to_readable_units(total_listening_time), count_songs]
        return return_object 


    def print_total_listening_time_over_interval(self, datetime1, datetime2):
        total_listening_time = self.total_listening_time_over_interval(datetime1,datetime2)

        if total_listening_time[0][1] == 'minute':
            print ("The total listening time is", total_listening_time[0][0], ' minutes between ', datetime1, ' and ' ,datetime2, 
             '. There are ', total_listening_time[1], ' songs in between this interval.')

            return ("The total listening time is ", total_listening_time[0][0], ' minutes between ', datetime1, ' and ', datetime2 
            , '. There are ', total_listening_time[1], ' songs in between this interval.')

        if total_listening_time[0][1] == 'hour':
            print ("The total listening time is ", total_listening_time[0][0], ' hours between ', datetime1, ' and ', datetime2 
            , '. There are ', total_listening_time[1], ' songs in between this interval.')

            return ("The total listening time is ", total_listening_time[0][0], ' hours between ', datetime1, ' and ', datetime2 
            , '. There are ', total_listening_time[1], ' songs in between this interval.')

        if total_listening_time[0][1] == 'day':
            print ("The total listening time is ", total_listening_time[0][0], ' days between ', datetime1, ' and ', datetime2 
            , '. There are ', total_listening_time[1], ' songs in between this interval.')

            return ("The total listening time is ", total_listening_time[0][0], ' days between ', datetime1, ' and ', datetime2 
            , '. There are ', total_listening_time[1], ' songs in between this interval.')

        if total_listening_time[0][1] == 'week':
            print ("The total listening time is ", total_listening_time[0][0], ' weeks between ', datetime1, ' and ', datetime2  
            , '. There are ', total_listening_time[1], ' songs in between this interval.')

            return ("The total listening time is ", total_listening_time[0][0], ' weeks between ', datetime1, ' and ', datetime2  
            , '. There are ', total_listening_time[1], ' songs in between this interval.') 

    def songs_listened_over_an_interval(self):
        pass 



    ############################################ SORTING ######################################

    def insertionSort_based_on_datetime(self):
    #This function will sort the list using insertion sort! I made this one myself...
        #num here is usually len(self.spotify_data)
        for i in range(len(self.spotify_data)):  
            j = i
            #100 is usually len(self.spotify_data)
            while j < (len(self.spotify_data)-1) and self.string_to_datetimeobject(self.spotify_data[j]["ts"]) > self.string_to_datetimeobject(self.spotify_data[j+1]["ts"]):
                self.spotify_data[j],self.spotify_data[j+1] = self.spotify_data[j+1],self.spotify_data[j]
                #This is where you will move the item backwards into it's correct position 
                k = j 
                while k > 0 and self.string_to_datetimeobject(self.spotify_data[k]["ts"]) < self.string_to_datetimeobject(self.spotify_data[k-1]["ts"]):
                    self.spotify_data[k],self.spotify_data[k-1] = self.spotify_data[k-1],self.spotify_data[k]
                    k -= 1 
                j += 1
        return self.spotify_data  

    def get_datetime(self, item):
        return self.string_to_datetimeobject(item['ts']) or ''

    def sort_based_on_datetime(self):
        return sorted(self.spotify_data, key=self.get_datetime)

    def get_artist_name(self, item):
        return item['master_metadata_album_artist_name'] or ''

    def sort_based_on_artist_name(self):
        return sorted(self.spotify_data, key=self.get_artist_name)

    def get_song_name(self, item):
        return item['master_metadata_track_name'] or ''
    
    def sort_based_on_song_name(self):
        return sorted(self.spotify_data, key=self.get_song_name)

    def get_album_name(self, item):
        return item['master_metadata_album_album_name'] or ''

    def sort_based_on_album_name(self):
        return sorted(self.spotify_data, key=self.get_album_name)
############################################ CREATING DATA AND REPORTS ######################################

    def insertion_sorted_Data_into_json(self):
        #The purpose of this is to take json data and put it into a new json file
        with open("sorted_spotifyData","w") as write_file:
            json.dump(self.insertionSort_based_on_datetime(), write_file)


    def sort_based_on_artist_name_into_json(self):
        #The purpose of this is to take json data and put it into a new json file
        with open("sorted_spotifyData_by_Artist","w") as write_file:
            json.dump(self.sort_based_on_artist_name(), write_file)
    
    def create_Txt_Report(self):
        #This will create a txt report of the data 
        with open('outputs/MetaData.txt', 'w') as f:
            f.write(self.print_number_of_songs())
            f.write('\n')
            f.write(self.print_total_listening_time())
            f.write('\n')
            f.write(self.print_time_between_most_and_least_recent_songs())
            f.write('\n')
            f.write(self.print_number_of_unique_artists())
            f.write('\n')
            f.write(self.print_top10_most_listened_to_artists())
            f.write('\n')
            f.write(self.print_top20_most_listened_to_albums())
            f.write('\n')
            f.write(self.print_top30_most_listened_to_songs())
            f.write('\n')
            f.write(self.print_listening_time_by_year())
            f.write('\n')
            f.write(self.print_listening_time_by_month())


############################################ PLOTTING ######################################
    def plot_listening_time_by_year(self):
        #This will use matplot lib to plot the listening time by year
        listening_time_by_year = self.listening_time_by_year()

        #apply the convert_ms_to_readable_units_for_plotting function to the values of the dictionary
        for key in listening_time_by_year.keys():
            listening_time_by_year[key] = self.convert_ms_to_readable_units_for_plotting(listening_time_by_year[key], 'day')

        print(listening_time_by_year)
        plt.bar(list(listening_time_by_year.keys()), list(listening_time_by_year.values()), color = 'green')
        plt.show()


    def plot_listening_time_by_month(self):
        #This will use matplot lib to plot the listening time by month
        listening_time_by_month = self.listening_time_by_month()

        for key in listening_time_by_month.keys():
            listening_time_by_month[key] = self.convert_ms_to_readable_units_for_plotting(listening_time_by_month[key], 'hour')

        plt.bar(list(listening_time_by_month.keys()), list(listening_time_by_month.values()), color = 'green')

        plt.xlabel('Date')
        plt.ylabel('Hours')

        plt.xticks(list(listening_time_by_month.keys())[::3])

        for x, y in zip(list(listening_time_by_month.keys()), list(listening_time_by_month.values())):
            plt.text(x, y, str(y)[:6], ha='center', va='bottom', rotation=90)

        plt.savefig('outputs/plot.png')
        # plt.show()

class Instantiate_Spotify_Analysis:
    def __init__(self):

        ##### Test Datasets
        self.small_Dataset = r'small_SpotifyData\StreamingHistory0.json'
        self.testDataset_2174songs = r'test_Data\test_endsong_2174songs.json'
        self.testDataset_351songs = r'test_Data\test_endsong_351songs.json'
        self.testDataset_24songs = r'test_Data\test_endsong_24songs.json'

        # self.instantiate_Dataset(self.big_Dataset)
        # self.instantiate_Dataset(self.testDataset_24songs)
        # self.instantiate_Dataset(self.testDataset_351songs)
        self.instantiate_Dataset(self.testDataset_2174songs)


        ##### Actual Datasets
        # endsong_data_filepaths = [r'Spotify_Data\big_SpotifyData\endsong_0.json', r'Spotify_Data\big_SpotifyData\endsong_1.json', r'Spotify_Data\big_SpotifyData\endsong_2.json', r'Spotify_Data\big_SpotifyData\endsong_3.json', r'Spotify_Data\big_SpotifyData\endsong_4.json', r'Spotify_Data\big_SpotifyData\endsong_5.json', r'Spotify_Data\big_SpotifyData\endsong_6.json', r'Spotify_Data\big_SpotifyData\endsong_7.json', r'Spotify_Data\big_SpotifyData\endsong_8.json', r'Spotify_Data\big_SpotifyData\endsong_9.json', r'Spotify_Data\big_SpotifyData\endsong_10.json', r'Spotify_Data\big_SpotifyData\endsong_11.json']
        # self.instantiate_Dataset(self.combine_json_files(endsong_data_filepaths))

    def combine_json_files(self, endsong_data_filepaths):
        #This function will combine all the json files into one json file 
        json_list = []
        for file_path in endsong_data_filepaths:
            with open(file_path, encoding='utf-8') as f:
                json_list += json.load(f)
        with open('outputs/combined_endsong_file.json', 'w') as f:
            json.dump(json_list, f)
        
        return 'outputs/combined_endsong_file.json'


    def instantiate_Dataset(self, dataset):

        spotify_data = spotifyAnalyser(dataset)

        # REPORTS 
        spotify_data.create_Txt_Report()
        # spotify_data.print_number_of_artist_listens('artist_listens.txt')

        # PLOTTING 
        # spotify_data.plot_listening_time_by_year()
        spotify_data.plot_listening_time_by_month()

        # DATA SORTING 
        # spotifyAnalyser(dataset).insertion_sorted_Data_into_json() 
        # spotifyAnalyser(dataset).sort_based_on_artist_name_into_json()

        # INTERVALS 
        # spotifyAnalyser(dataset).print_total_listening_time_over_interval('2018-08-27T09:51:44Z','2019-01-21T04:17:12Z') 


if __name__ == "__main__": 
    Instantiate_Spotify_Analysis()