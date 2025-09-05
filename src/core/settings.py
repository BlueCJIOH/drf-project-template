"""Django settings entrypoint using split settings."""
from split_settings.tools import include

include("conf/*.py", "conf/integrations/*.py")
