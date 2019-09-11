import os
import importlib

cpath = os.environ.get("ZHUGE_CONFIG_SETTINGS", "spider.config.Config")
config_model = importlib.import_module(cpath)


class ConfigService(object):
    @staticmethod
    def get_log_config():
        return config_model.log_config

    @staticmethod
    def get_mongo_conf():
        return config_model.mongo_conf

    @staticmethod
    def get_redis_conf():
        return config_model.redis_conf

    @staticmethod
    def get_tidb_conf():
        return config_model.tidb_conf

    @staticmethod
    def get_rabbitmq_conf():
        return config_model.rabbitmq_conf

    @staticmethod
    def get_mysql_conf():
        return config_model.mysql_conf

    @staticmethod
    def get_pika_conf():
        return config_model.pika_conf

    @staticmethod
    def get_es_config():
        return config_model.es_config

    @staticmethod
    def get_kafka_conf():
        return config_model.kafka_conf