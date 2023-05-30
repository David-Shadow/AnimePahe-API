import asyncio
from app import app

async def run_flask_app():
    app.run(debug=True, host='0.0.0.0')

async def run_async_app():
    # Your async app logic goes here
    # Replace this with your actual async app code
    pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    
    flask_task = loop.create_task(run_flask_app())
    async_task = loop.create_task(run_async_app())
    
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(asyncio.gather(flask_task, async_task))
        loop.close()
