from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from starlette.routing import Route

async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, Plain!')
    await response(scope, receive, send)

# app = Starlette(debug=True, routes=[
#     Route('/', homepage)
# ])