(Super simple) Python Module for HipChat API
==================================

Description
-----------

Easy peasy wrapper for the `HipChat API`_. Exposes core URI endpoint wrapper and some basic methods for common integrations.


Dependencies
------------
None beyond the Python standard library.

Usage
-----

Instantiate::

    import hipchat.py
    hipster = hipchat.HipChat(token=YourHipChatToken)

Request a URI endpoint as described in the HipChat API docs::

    hipster.method(url='method/url/', method="GET/POST", parameters={'name':'value', })

Example methods::

    # List rooms
    hipster.method('rooms/list')
    
    # Post a message to a HipChat room
    hipster.method('rooms/message', method='POST', parameters={'room_id': 8675309, 'from': 'HAL', 'message': 'All your base...'})
    
Two handy shortcut methods::

    # List rooms, print response JSON
    print hipster.rooms_list()

    # POST a message to a room, print response JSON
    print hipster.room_message(8675309, 'HAL', 'All your base...')


.. _`HipChat API`: https://www.hipchat.com/docs/api
