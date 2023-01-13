print('Enter desired auto service:')
service_name = input()
print(f'You entered: {service_name}')
if service_name == 'Oil change':
    print(f'Cost of oil change: $35')
elif service_name == 'Tire rotation':
    print(f'Cost of tire rotation: $19')
elif service_name == 'Car wash':
    print(f'Cost of car wash: $7')
else:
    print('Error: Requested service is not recognized')
