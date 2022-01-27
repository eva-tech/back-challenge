from environ import Env

# Initialise environment variables
env = Env()
env.read_env(env_file=".env")

SECRET_KEY = env("SECRET_KEY")
DATABASE_HOST = env("DATABASE_HOST")
DATABASE_NAME = env("DATABASE_NAME")
DATABASE_PASS = env("DATABASE_PASS")
DATABASE_PORT = env("DATABASE_PORT")
DATABASE_USER = env("DATABASE_USER")
