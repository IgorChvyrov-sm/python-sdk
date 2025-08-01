from typing import ClassVar, Dict

class EmbeddingModel(object):
    swagger_types: ClassVar[Dict[str, str]] = {
        "provider": "str",
        "model": "str"
    }

    attribute_map: ClassVar[Dict[str, str]] = {
        "provider": "embeddingModelProvider",
        "model": "embeddingModel"
    }

    def __init__(self, provider: str, model: str):
        self._provider = provider
        self._model = model

    @property
    def provider(self) -> str:
        return self._provider

    @property
    def model(self) -> str:
        return self._model

    @provider.setter
    def provider(self, provider: str):
        self._provider = provider

    @model.setter
    def model(self, model: str):
        self._model = model
