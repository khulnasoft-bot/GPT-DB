"""Import all models to make sure they are registered with SQLAlchemy."""

from gptdb.model.cluster.registry_impl.db_storage import ModelInstanceEntity
from gptdb.storage.chat_history.chat_history_db import (
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
)
from gptdb_app.openapi.api_v1.feedback.feed_back_db import ChatFeedBackEntity
from gptdb_serve.agent.app.recommend_question.recommend_question import (
    RecommendQuestionEntity,
)
from gptdb_serve.agent.hub.db.my_plugin_db import MyPluginEntity
from gptdb_serve.agent.hub.db.plugin_hub_db import PluginHubEntity
from gptdb_serve.datasource.manages.connect_config_db import ConnectConfigEntity
from gptdb_serve.evaluate.db.benchmark_db import BenchmarkSummaryEntity
from gptdb_serve.file.models.models import ServeEntity as FileServeEntity
from gptdb_serve.flow.models.models import ServeEntity as FlowServeEntity
from gptdb_serve.flow.models.models import VariablesEntity as FlowVariableEntity
from gptdb_serve.prompt.models.models import ServeEntity as PromptManageEntity
from gptdb_serve.rag.models.chunk_db import DocumentChunkEntity
from gptdb_serve.rag.models.document_db import KnowledgeDocumentEntity
from gptdb_serve.rag.models.models import KnowledgeSpaceEntity

_MODELS = [
    PluginHubEntity,
    FileServeEntity,
    MyPluginEntity,
    PromptManageEntity,
    KnowledgeSpaceEntity,
    KnowledgeDocumentEntity,
    DocumentChunkEntity,
    ChatFeedBackEntity,
    ConnectConfigEntity,
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
    ModelInstanceEntity,
    FlowServeEntity,
    RecommendQuestionEntity,
    FlowVariableEntity,
    BenchmarkSummaryEntity,
]
