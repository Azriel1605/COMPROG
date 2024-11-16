def format_duration(seconds):
    if seconds == 0:
        return 'now'
    seconds_of_year = 60*60*24*365
    print(seconds_of_year)
    seconds_of_day = seconds_of_year//365
    seconds_of_hour = seconds_of_day//24
    seconds_of_minutes = 60
    
    year = seconds // seconds_of_year
    seconds -= year * seconds_of_year
    day = seconds // seconds_of_day
    seconds -= day * seconds_of_day
    hour = seconds // seconds_of_hour
    seconds -= hour * seconds_of_hour
    minutes = seconds // seconds_of_minutes
    seconds -= minutes * seconds_of_minutes
    
    word = []
    if year:
        if year > 1:
            word.append(f'{year} years')
            
        else:
            word.append(f'{year} year')
            
    if day:
        if day > 1:
            word.append(f'{day} days')
        else:
            word.append(f'{day} day')
            
    if hour:
        if hour > 1:
            word.append(f'{hour} hours')
        else:
            word.append(f'{hour} hour')
            
    if minutes:
        if minutes > 1:
            word.append(f'{minutes} minutes')
        else:
            word.append(f'{minutes} minute')
            
            
    if seconds:
        if seconds > 1:
            word.append(f'{seconds} seconds')
        else:
            word.append(f'{seconds} second')
            
    print(word)
    if len(word) == 2:
        text = ' and '.join(word)
    else:
        if len(word) != 1:
            word[-2] = f'{word[-2]} and {word[-1]}'
            word.pop(-1)
        text = ', '.join(word)
    return text
    
    
print(format_duration(3662))
        
        
        