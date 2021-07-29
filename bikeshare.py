import time
import pandas as pd
import numpy as np
# This Dict has The cities names and each file
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
    f=False
    print('Please enter name of the city you want: (chicago, newyork city, washington)')
    # Ask the user to input the city that he want to analysis it
    while  f!= True:
        city=input()
        city=city.lower()
        if city == "chicago" or city == "new york city" or city == "washington" :
            f=True
        if f==False:
            print('Wrong ====> (chicago, new york city, washington)')

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Please enter name of the month you want: (all, january, february, ... , june)')
    # Ask the user to input the month that he want to analysis it or all months
    f=False
    while   f!= True:
        month=input()
        month=month.lower()
        if month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june' or month=='all':
            f=True
        if f==False:
            print('Wrong ====> (all, january, february, ... , june)')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Please enter name of the day you want: (all, monday, tuesday, ... sunday)')
    # Ask the user to input the day that he want to analysis it or all days
    f=False
    while   f!=True:
        day=input()
        day=day.lower()
        if day=='all' or day=='sunday' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday':
            f=True
        if f==False:
            print('Wrong=====> (all, monday, tuesday, ... sunday)')


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
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
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
    popular_month = df['month'].mode()[0]
    print("the most common month",popular_month,"\n")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("the most common day of week",popular_day,"\n")


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("the most common start hour",popular_hour,"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    print("most commonly used start station ",df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station

    print("most commonly used end station ",df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    df['trip road']=df['Start Station']+" to "+df['End Station']
    print("most frequent combination of start station and end station trip ",df['trip road'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['trip time']=(df['End Time']-df['Start Time']).dt.total_seconds()
    total_time=df['trip time'].sum()
    year=total_time%(365*24*60*60)
    total_time=total_time-(year*365*24*60*60)
    day=total_time%(24*60*60)
    total_time=total_time-(day*24*60*60)
    hour=total_time%(60*60)
    total_time=total_time-(hour*60*60)
    mins=total_time%(60)
    total_time=total_time-(mins*60)
    print("The total travel time => ",year,"years",day,"days",hour,"hours",mins,"minutes")

    # TO DO: display mean travel time
    print("The mean travel time => ",df['trip time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    if "User Type" in df.columns:
        a=df['User Type'].value_counts()
        print("counts of user types\n",a)
    else:
        print("Not finding User Type !!!!")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        b=df['Gender'].value_counts()
        print("counts of gender\n",b)
    else:
        print("Not finding Gender !!!!")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("most earliest year of birth ",int(df['Birth Year'].min()),"\n")
        print("most recent year of birth ",int(df['Birth Year'].max()),"\n")
        print("most common year of birth ",int(df['Birth Year'].mode()[0]),"\n")
    else:
        print("Not finding Birth Year !!!!")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    
    """ Your docstring here """
    i = 0
    f=False
    raw = input("Would you like to see 5 lines of data? Enter yes or no.\n").lower() # TO DO: convert the user input to lower case using lower() function
    #pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no' or raw =='n':
            break
        elif raw == 'yes' or raw == 'y' or raw == 'ye':
            for line in range(i,i+5):
                print(df.iloc[line])
             # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to see more 5 lines of data? Enter yes or no.\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
           
       
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower() != 'y' and restart.lower() != 'ye':
            break
        elif restart.lower() == 'no' or restart.lower() == 'n':
            break
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            


if __name__ == "__main__":
	main()
