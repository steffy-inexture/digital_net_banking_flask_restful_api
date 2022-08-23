from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:harsh2022@localhost:5432/db_for_bs'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = 'sdfghjjjjjjjjjjjjjjjjjj'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
