import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    checkcity = True
    
    while checkcity :
        city = input('Choose the city you want to know about it (chicago, new york city, washington) :').lower()
        if city in ['chicago','new york city','washington']:
            checkcity = False
            break
        print('invalid input please make sure you choose the right city')


    # TO DO: get user input for month (all, january, february, ... , june)
    checkmonth = True
    while checkmonth :
        month = input('Choose month \n(all, january, february, march, april, may, june) :').lower()
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            checkmonth = False
            break
        print('invalid input please make sure you choose the right month')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    checkday = True
    while checkday :
        day = input('Choose day \n(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday ) :').lower()
        if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
            checkday = False
            break
        print('invalid input please make sure you choose the right day')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month =df['month'].mode()[0]
    months =['january', 'february', 'march', 'april', 'may', 'june']
    month = months[most_common_month - 1]
    print('Most common month is : ',month)


    # TO DO: display the most common day of week
    most_common_day =df['day_of_week'].mode()[0]
    print('Most common day is : ',most_common_day)


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common start hour is : ',most_common_hour)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_Start_station =df['Start Station'].mode()[0]
    print('Most common Start Station is : ',most_common_Start_station)
    
    # TO DO: display most commonly used end station
    most_common_End_station =df['End Station'].mode()[0]
    print('Most common End Station is : ',most_common_End_station)

 
    # TO DO: display most frequent combination of start station and end station trip
    
    # Group by Start station and End station, then count occurrences of each combination
    trip_counts = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count')

    # Find the most frequent combination by sorting the trip_counts in descending order then take the first row
    most_frequent_trip = trip_counts.sort_values(by='count', ascending=False).head(1)

    print('\nThe most frequent trip is:\n',most_frequent_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_second = df['Trip Duration'].sum()
    print('The total travel time {} seconds '.format(total_travel_second))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    # Convert mean_travel_time seconds into  hours, minutes, and seconds
    hours = mean_travel_time // 3600  # 3600 is the number of seconds in an hour (60 minutes x 60 seconds) 
    minutes = (mean_travel_time % 3600) // 60
    seconds = mean_travel_time % 60 
    
    print('The mean travel time is: {h} hours, {m} minutes, and {s} seconds'.format(h = hours, m = minutes ,s = round(seconds, 2) ) )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        #counts each user type
        user_types = df.groupby(['User Type']).size().reset_index(name='count')
        print('The counts of each user type is :\n\n ',user_types,'\n')
    except:
        pass
    
    try:
    # TO DO: Display counts of gender
    
        gender = df.groupby(['Gender']).size().reset_index(name='count')
        print('The number of each gender is :\n\n ',gender)
    except KeyError :
         # Handle missing columns
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earlist = int(df['Birth Year'].min())
        print('\nThe earlist year is : ', earlist)
        most_recent = int(df['Birth Year'].max())
        print('The most recent year is : ', most_recent)
        most_common = int(df['Birth Year'].mode()[0])
        print('The most common year is : ', most_common)
    except KeyError :
         # Handle missing columns
        pass
    except ValueError:
        # Handle cases where there is no valid data for calculations
        print(f"Value error: {e}. The data may contain invalid values.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def display_dataframe(df):
    """Displays the data in the dataframe"""
    print('This is a subset of the data\n')
    number_of_rows = 5
    while True:
        print(df.head(number_of_rows))
        answer = input('do you want to see more data: ')
        if answer != 'yes':
            break
        
        if number_of_rows >= df.shape[0]:  # Check if All rows have been printed
            print("All rows have been printed.")
            break
        number_of_rows += 5
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_dataframe(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
