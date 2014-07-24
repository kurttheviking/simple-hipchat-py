(Super simple) Python HipChat
=============================

Description
-----------

Easy peasy wrapper for the `HipChat API <https://www.hipchat.com/docs/api>`_. Exposes core URI endpoint wrapper and some basic methods for common integrations.


Dependencies
------------
None beyond the Python standard library.


Usage
-----

Install::

    pip install python-simple-hipchat

Instantiate::

    import hipchat
    hipster = hipchat.HipChat(token=YourHipChatToken)

Request a URI endpoint as described in the HipChat API docs::

    hipster.method(url='method/url/', method="GET/POST", parameters={'name':'value', })

Example::

    # List rooms
    hipster.method('rooms/list')

    # Post a message to a HipChat room
    hipster.method('rooms/message', method='POST', parameters={'room_id': 8675309, 'from': 'HAL', 'message': 'All your base...'})


API Sugar
---------

**Send a message to a room**::

    room_id = 8675309
    from_name = 'HAL'
    message = 'All your base...'

    hipster.message_room(room_id, from_name, message)

**List rooms**::
 
    hipster.list_rooms()
    
**Find room by name**::

    hipster.find_room('name')

**List users**::

    hipster.list_users()

**Find user by name**::

    hipster.find_user('John Doe')



Changelog
---------

**v0.3.x**

- Added shortcut method for listing users (thanks @Raizex)
- Added shortcut method for finding user by name (thanks @Raizex)
- Added shortcut method for finding room by name (thanks @Raizex)
- `Added trove classifiers <https://pypi.python.org/pypi?%3Aaction=list_classifiers>`_ (thanks @ghickman)

**v0.2.x**

- `Added Python 3 support without losing support for Python 2 <https://github.com/kurttheviking/python-simple-hipchat/pull/9>`_ (thanks @pimterry)
- `Expose timeout for safer synchronous use <https://github.com/kurttheviking/python-simple-hipchat/pull/3>`_ (thanks @zachsnow)

**v0.1.x**

- Added shortcut method for messaging a room
- Added shortcut method for listing rooms (requires admin token)
