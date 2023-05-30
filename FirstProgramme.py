def calculate_fan_consumption(power_rating,operating_hours,electricity_rate):
   energy_consumed=power_rating*operating_hours
   energy_consumed_kWh=energy_consumed/1000
   cost_of_electricity=energy_consumed_kWh*electricity_rate
   return energy_consumed,energy_consumed_kWh,cost_of_electricity

fans=[
 {"name":"Fan 1","power_rating":60,"operating_hours":8},
 {"name": "Fan 2", "power_rating": 75, "operating_hours": 6},
 {"name": "Fan 3", "power_rating": 90, "operating_hours": 10}
]

electricity_rate=0.12
for fan in fans:
    fan_power_rating=fan["power_rating"]
    operating_hours=fan["operating_hours"]

    energy_consumed,energy_consumed_kWh,cost_of_electricity=calculate_fan_consumption(fan_power_rating,operating_hours,electricity_rate)

    print("Fan",fan["name"])
    print("Energy Consumed:{}watt-hours".format(energy_consumed))
    print("Energy Consumed:{}kilowat-hours".format(energy_consumed_kWh))
    print("Cost of Electricity:$(.2f)".format(cost_of_electricity))


