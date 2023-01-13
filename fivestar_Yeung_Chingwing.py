"""
Program: fivestar.py


Calculate the total charge for a customer's video rentals,
given the number of each type of video. Prompt the user for input.

Use constant variable for the rental amount

New video rental = $3.00
Oldie rental = $2.00

"""
#prompt user to enter input for new and old videos
no_of_new_video = int(input('No of new video:'))
no_of_old_video = int(input('No of old video:'))

#output total charge
total_charge = (no_of_new_video * 3.00) + (no_of_old_video * 2.00)
print('total charge: $', total_charge)
