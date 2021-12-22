from flask import Blueprint

main = Blueprint( 'main', __name__)



# Deixar sempre na última linha:
from . import views