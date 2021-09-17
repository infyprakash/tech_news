from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry
from scrapper.models import NyTimesModel,FoxNewsModel,PcMagModel,CnetModel


@registry.register_document
class NyTimesDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'newyorktimes'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = NyTimesModel # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'link',
            'description',
            'creator',
            'publication_date',
            'media_url',
            'media_description',
            'media_credit',
            'categories'
            ]

@registry.register_document
class  FoxNewsDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'foxnews'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = FoxNewsModel # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'link',
            'description',
            'creator',
            'publication_date',
            'media_url',
            'media_description',
            'media_credit',
            'categories'
            ]


@registry.register_document
class PcMagDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'pcmagazine'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = PcMagModel # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'link',
            'description',
            'creator',
            'publication_date',
            'media_url',
            'media_description',
            'media_credit',
            'categories'
            ]
    

@registry.register_document
class CnetDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'cnet'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = CnetModel # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'link',
            'description',
            'creator',
            'publication_date',
            'media_url',
            'media_description',
            'media_credit',
            'categories'
            ]


