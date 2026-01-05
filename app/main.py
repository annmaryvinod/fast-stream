from contextlib import asynccontextmanager
from fastapi import FastAPI
from faststream import FastStream
from faststream.kafka import KafkaBroker
from app.config import settings
from app.schemas import UserEvent

broker = KafkaBroker(settings.kafka_bootstrap_servers)
app = FastStream(broker)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.start()
    yield
    await broker.close()

fastapi_app = FastAPI(lifespan=lifespan)

@fastapi_app.post("/publish")
async def publish_message(event: UserEvent):
    await broker.publish(event, topic="test-topic")
    return {"status": "published", "data": event}

@broker.subscriber("test-topic")
async def handle_msg(event: UserEvent):
    print(f"Consumed message: {event}")
