from news_aggregator.settings import *


ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200',
        'timeout': 60
    },
}