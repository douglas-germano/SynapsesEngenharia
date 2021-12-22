from flask import Blueprint


auth = Blueprint( 'auth', __name__)



# Deixar sempre na última linha:
from . import views