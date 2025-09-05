import environ

from core.conf.boilerplate import BASE_DIR

env = environ.Env(
    ENVIRONMENT=(str, "develop"),
    DEBUG=(bool, False),
)

envpath = BASE_DIR / ".env"

if envpath.exists():
    env.read_env(envpath)


__all__  = [
    "env",
]
