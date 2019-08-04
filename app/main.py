from aiohttp import web
import socketio
import redis
import random

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)

def initialize_room():
	return random.randint(1000,9999)
room = initialize_room()

redis_server = redis.Redis()
redis_server.set("rooms", room)

@sio.event
def begin_chat(sid):
   sio.enter_room(sid, 'chat_users')

# we can define aiohttp endpoints just as we normally
# would with no change
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('chat_message', room="room")

# @sio.on('message')
# async def print_message(sid, message):
#     print("Socket ID: " , sid)
#     print(message)
#     # await a successful emit of our reversed message
#     # back to the client
#     await sio.emit('message', message[::-1])

# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)

