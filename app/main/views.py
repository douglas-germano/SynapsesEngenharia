from . import main
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from wtforms.validators import DataRequired, Length
from app import app 
from app import db
from ..models import Vehicle
from .forms import RegisterVehicleForm

@app.route('/')
def main():
    return render_template("main/main.html")

@app.route('/cadastros', methods=['GET', 'POST'])
@login_required
def cadastros():
    form = RegisterVehicleForm()
    placa = form.placa.data
    modelo = form.modelo.data
    fabricante = form.fabricante.data
    renavan = form.renavan.data
    combustivel = form.combustivel.data
    lotacao = form.lotacao.data
    anofabricacao = form.anofabricacao.data

    if form.validate_on_submit():
        vehicle = Vehicle.query.filter_by(placa=placa).first()
        if not vehicle:
            vehicle = Vehicle(placa, modelo, fabricante, renavan, combustivel, lotacao, anofabricacao)
            db.session.add(vehicle)
            db.session.commit()
        return redirect(url_for('cadastros')) 
    return render_template("main/cadastros.html", form=form)

@app.route("/veiculos", methods=['GET'])
@login_required
def veiculos():
    vehicles = Vehicle.query.all()
    return render_template("main/veiculos.html", vehicles=vehicles)

@app.route("/veiculos/excluir-veiculo/<int:id>", methods=['GET', 'POST'])
@login_required
def delete_vehicle(id):
    delete_vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(delete_vehicle)
    db.session.commit()
    return redirect(url_for('veiculos'))

@app.route('/relatorios')
@login_required
def relatorios():
    return render_template("main/relatorios.html")

@app.route('/manutencoes')
@login_required
def manutencoes():
    return render_template("main/manutencoes.html")
