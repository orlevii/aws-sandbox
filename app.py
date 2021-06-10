from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def hello():
    return dict(
        msg='Got to my app!'
    )


@app.get('/sum')
async def sum(a: float, b: float):
    return dict(
        res=a + b
    )


def main():
    uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
