import os

PICTURES_SECRET_KEY = os.getenv("PICTURES_SECRET_KEY", "ac9dd0517ef9da9bd6a53c0d92f461f333037ea922f590a28c20f1f0fa6f102a")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30