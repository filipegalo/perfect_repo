from fastapi import FastAPI

app = FastAPI()


@app.get('/main')
async def main_route():
	return {'message': 'Hey, good job!'}


@app.get('/test')
def test_route():
	return {'message': 'Test route'}
