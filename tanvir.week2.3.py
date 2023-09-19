# Get input seconds from user
seconds = int(input("Enter seconds: "))

# Convert seconds to hours, minutes and seconds
hours = seconds // 3600  # Divide by 3600 and get the integer quotient
seconds = seconds % 3600  # Get the remainder after dividing by 3600
minutes = seconds // 60  # Divide by 60 and get the integer quotient
seconds = seconds % 60  # Get the remainder after dividing by 60

# Print hours, minutes and seconds
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)
