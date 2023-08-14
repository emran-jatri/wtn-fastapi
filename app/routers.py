from .modules.users import users


routers = [
    {
        'router': users.router, 
        'prefix': '/users', 
        'tags': ['------------------ users --------------------']
    }
]