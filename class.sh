#!/bin/bash

# # Set the class start time in 24-hour format (HH:MM)
# class_start_time="18:00"

# # Calculate the time until the class starts
# current_time=$(date +"%H%M")
# time_until_class=$(date -u -d"$class_start_time" +"%s")-$(date -u -d"$current_time" +"%s")


# # Check if the class has already started
# if [ $time_until_class -le 18:00 ]; then
#   echo "Class has already started!"
# else
#   echo "Reminder set: Class starts at $class_start_time. You will be reminded in $time_until_class_minutes minutes."

#   # Sleep until it's time for the reminder
#   sleep $time_until_class

#   # Display the reminder
#   notify-send "Class Reminder" "Your class is starting now!"
# fi


# Function to display a reminder
function show_reminder() {
  notify-send "Reminder" "$1"
}

# Function to calculate time until a specified time
function calculate_time_until() {
  reminder_time="$1"
  current_time=$(date +"%H:%M")
  time_until_reminder=$(date -u -d"$reminder_time" +"%s")-$(date -u -d"$current_time" +"%s")
  echo $time_until_reminder
}

# Set the reminder time in 24-hour format (HH:MM)
reminder_time="14:30"

# Calculate the time until the reminder
time_until_reminder=$(calculate_time_until "$reminder_time")

# Check if the reminder time has already passed
if [ $time_until_reminder -le 0 ]; then
  echo "It's already past the reminder time!"
else
  echo "Reminder set: You will be reminded at $reminder_time. Waiting..."
 
  show_reminder "Time to do something! Don't forget!"
fi


