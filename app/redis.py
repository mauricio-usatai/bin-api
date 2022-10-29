from redis import Redis
import app as App

class RedisClient:
  @staticmethod
  def get_client():
    return Redis(
      host=App.Config.REDIS_URL,
      port=App.Config.REDIS_PORT,
    )
