from __future__ import annotations
from typing import Optional
from typing_extensions import Self

from conductor.client.workflow.task.task import TaskInterface
from conductor.client.workflow.task.task_type import TaskType


class LlmGenerateEmbeddings(TaskInterface):
    def __init__(self, task_ref_name: str, llm_provider: str, model: str, text: str, task_name: Optional[str] = None) -> Self:
        if task_name is None:
            task_name = "llm_generate_embeddings"
        super().__init__(
            task_name=task_name,
            task_reference_name=task_ref_name,
            task_type=TaskType.LLM_GENERATE_EMBEDDINGS,
            input_parameters={
                "llmProvider": llm_provider,
                "model": model,
                "text": text,
            }
        )
