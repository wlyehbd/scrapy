"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/6/2
@Desc    :

"""
# from spider.databases.mysqldb.mysqldb import MysqlDB
# from spider.databases.tidb.tidb import TiDB
# from spider.databases.pikadb.pikadb import PikaDB
from spider.databases.redisdb.redisdb import RedisDB
# from spider.databases.mongodb.mongodb import MongoDB
# from spider.databases.rabbitmqdb.rabbitmq import Rabbitmq
# from spider.databases.esdb.esdb import EsDB
# from spider.databases.kafkadb.kafkadb import KafkaDB


class dbfactory:
    # @staticmethod
    # def create_db(**kwargs):
    #     db_type = kwargs.get("db_type")
    #     return getattr(dbfactory, db_type)(**kwargs)

    # @staticmethod
    # def db_mysql(**kwargs):
    #     return MysqlDB(**kwargs)
    #
    # @staticmethod
    # def db_tidb(**kwargs):
    #     return TiDB(**kwargs)
    #
    # @staticmethod
    # def db_mongo(**kwargs):
    #     return MongoDB(**kwargs)
    #
    # @staticmethod
    # def db_es(**kwargs):
    #     return EsDB(**kwargs)

    @staticmethod
    def db_redis(**kwargs):
        return RedisDB.getRedisConn(**kwargs)

    # @staticmethod
    # def db_pika(**kwargs):
    #     return PikaDB.getPikaConn(**kwargs)
    #
    # @staticmethod
    # def db_rabbitmq(**kwargs):
    #     return Rabbitmq(**kwargs)
    #
    # @staticmethod
    # def db_kafka(**kwargs):
    #     return KafkaDB(**kwargs)