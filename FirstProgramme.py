def calculate_average_temperature(temperatures):
    total_temperature = sum(temperatures)
    num_readings = len(temperatures)
    average_temperature = total_temperature / num_readings
    return average_temperature

river_temperatures = [12.5, 13.2, 14.8, 15.6, 13.9, 12.1, 11.8, 14.3]
average_temp = calculate_average_temperature(river_temperatures)

# Display the average temperature
print("Average River Temperature: {:.2f} degrees".format(average_temp))
