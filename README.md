logging-loki
===================

Python logging handler for [Loki](https://grafana.com/loki).  


Installation
============
```bash
pip install logging-loki
```

Usage
=====

```python
import logging
import logging_loki


handler = logging_loki.LokiHandler(
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(
    "Something happened", 
    extra={"tags": {"service": "my-service"}},
)
```

Example above will send `Something happened` message along with these labels:
- Default labels from handler
- Message level as `serverity`
- Logger's name as `logger` 
- Labels from `tags` item of `extra` dict

The given example is blocking (i.e. each call will wait for the message to be sent).  
But you can use the built-in `QueueHandler` and` QueueListener` to send messages in a separate thread.  

```python
import logging.handlers
import logging_loki
from multiprocessing import Queue


queue = Queue(-1)
handler = logging.handlers.QueueHandler(queue)
handler_loki = logging_loki.LokiHandler(
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)
logging.handlers.QueueListener(queue, handler_loki)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(...)
```

Or you can use `LokiQueueHandler` shortcut, which will automatically create listener and handler.

```python
import logging.handlers
import logging_loki
from multiprocessing import Queue


handler = logging_loki.LokiQueueHandler(
    Queue(-1),
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(...)
```

If Multi-tenancy is enabled then you can use following configuration:


```python
import logging.handlers
import logging_loki

# Configuring the LokiQueueHandler with multi-tenancy enabled
handler = logging_loki.LokiHandler(
    url="https://my-loki-instance/loki/api/v1/push",  # Loki endpoint for log ingestion
    tags={"application": "my-app"},  # Additional tags for log identification
    auth=("username", "password"),  # Authentication credentials for accessing Loki
    version="1",  # Version of the Loki API being used
    tenant_id="som-tenant-id",  # Unique identifier for the tenant
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(...)
```
