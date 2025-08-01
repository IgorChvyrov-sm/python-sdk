from __future__ import absolute_import
from abc import ABC, abstractmethod
from typing import List

from conductor.client.http.models.integration import Integration
from conductor.client.http.models.integration_api import IntegrationApi
from conductor.client.http.models.integration_api_update import IntegrationApiUpdate
from conductor.client.http.models.integration_update import IntegrationUpdate
from conductor.client.http.models.prompt_template import PromptTemplate


class IntegrationClient(ABC):
    """Client for managing integrations with external systems.  Some examples of integrations are:
    1. AI/LLM providers (e.g. OpenAI, HuggingFace)
    2. Vector DBs (Pinecone, Weaviate etc.)
    3. Kafka
    4. Relational databases

    Integrations are configured as integration -> api with 1->N cardinality.
    APIs are the underlying resources for an integration and depending on the type of integration they represent underlying resources.
    Examples:
        LLM integrations
        The integration specifies the name of the integration unique to your environment, api keys and endpoint used.
        APIs are the models (e.g. text-davinci-003, or text-embedding-ada-002)

        Vector DB integrations,
        The integration represents the cluster, specifies the name of the integration unique to your environment, api keys and endpoint used.
        APIs are the indexes (e.g. pinecone) or class (e.g. for weaviate)

        Kafka
        The integration represents the cluster, specifies the name of the integration unique to your environment, api keys and endpoint used.
        APIs are the topics that are configured for use within this kafka cluster
    """

    @abstractmethod
    def associate_prompt_with_integration(self, ai_integration:str, model_name:str, prompt_name:str):
        """Associate a prompt with an AI integration and model"""
        ...

    @abstractmethod
    def delete_integration_api(self, api_name:str, integration_name:str):
        """Delete a specific integration api for a given integration"""
        ...

    @abstractmethod
    def delete_integration(self, integration_name:str):
        """Delete an integration"""


    @abstractmethod
    def get_integration_api(self, api_name:str, integration_name:str) -> IntegrationApi:
        ...

    @abstractmethod
    def get_integration_apis(self, integration_name:str) -> List[IntegrationApi]:
        ...

    @abstractmethod
    def get_integration(self, integration_name:str) -> Integration:
        ...

    @abstractmethod
    def get_integrations(self) -> List[Integration]:
        """Returns the list of all the available integrations"""


    @abstractmethod
    def get_prompts_with_integration(self, ai_integration:str, model_name:str) -> List[PromptTemplate]:
        ...

    @abstractmethod
    def get_token_usage_for_integration(self, name, integration_name) -> int:
        ...

    @abstractmethod
    def get_token_usage_for_integration_provider(self, name) -> dict:
        ...

    @abstractmethod
    def register_token_usage(self, body, name, integration_name):
        ...

    @abstractmethod
    def save_integration_api(self, integration_name, api_name, api_details: IntegrationApiUpdate):
        ...

    @abstractmethod
    def save_integration(self, integration_name, integration_details: IntegrationUpdate):
        ...

    # Tags

    @abstractmethod
    def delete_tag_for_integration(self, body, tag_name, integration_name):
        """Delete an integration"""


    @abstractmethod
    def delete_tag_for_integration_provider(self, body, name):
        ...

    @abstractmethod
    def put_tag_for_integration(self, body, name, integration_name):
        ...

    @abstractmethod
    def put_tag_for_integration_provider(self, body, name):
        ...

    @abstractmethod
    def get_tags_for_integration(self, name, integration_name):
        ...

    @abstractmethod
    def get_tags_for_integration_provider(self, name):
        ...
