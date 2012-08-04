from hipchat import *

hipster = HipChat('2fea4b530ca75dd5cb961358260a12')

print hipster.method('rooms/list')

print hipster.method('rooms/message', method='POST', parameters={'room_id': 89753, 'from': 'HAL', 'message': 'All your base...'})

# print response
