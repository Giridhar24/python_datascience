# Topic of the Day: DateTime Handling
# Explanation: Time is messy (Leap years, time zones, string formats).
# Pandas has a powerful engine to convert strings into actual "Time Objects" that you can do math with (e.g., "Add 3 days").

import pandas as pd

# Raw string data
data = {
    'Event': ['Login', 'Logout', 'Purchase'],
    'Time_String': ['2023-01-01 10:00:00', '2023-01-01 12:30:00', '2023-01-02 09:15:00']
}
df = pd.DataFrame(data)

# 1. Convert String to DateTime Object
df['Timestamp'] = pd.to_datetime(df['Time_String'])

# 2. Extract specific components
df['Hour'] = df['Timestamp'].dt.hour
df['Day_Name'] = df['Timestamp'].dt.day_name()

print(df[['Event', 'Hour', 'Day_Name']])

# 3. Time Math
# Calculate duration (Difference between times)
duration = df['Timestamp'].iloc[1] - df['Timestamp'].iloc[0]
print(f"\nDuration between Login and Logout: {duration}")