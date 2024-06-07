from flask import Flask, render_template, request, redirect, jsonify, make_response
from models.connection import db
from models.insert import ParticipacaoDespejo, ProducaoPlastico
import json

def export_json():
    search_term = request.form.get('search')
    table = request.form.get('table')

    try:
        if table == 'despejo':
            if search_term:
                despejo_results = db.session.query(ParticipacaoDespejo).filter(
                    db.or_(ParticipacaoDespejo.entidade.ilike(f'%{search_term}%'),
                           ParticipacaoDespejo.codigo.ilike(f'%{search_term}%'),
                           ParticipacaoDespejo.ano.ilike(f'%{search_term}%'),
                           ParticipacaoDespejo.participacao.ilike(f'%{search_term}%'))
                ).all()
            else:
                despejo_results = db.session.query(ParticipacaoDespejo).all()

            despejo_data = [{'id': despejo.id, 'entidade': despejo.entidade, 'codigo': despejo.codigo,
                             'ano': despejo.ano, 'participacao': despejo.participacao} for despejo in despejo_results]

            data = {'despejo': despejo_data}
        else:
            if search_term:
                producao_results = db.session.query(ProducaoPlastico).filter(
                    db.or_(ProducaoPlastico.entidade.ilike(f'%{search_term}%'),
                           ProducaoPlastico.ano.ilike(f'%{search_term}%'),
                           ProducaoPlastico.producao_anual.ilike(f'%{search_term}%'))
                ).all()
            else:
                producao_results = db.session.query(ProducaoPlastico).all()

            producao_data = [{'id': producao.id, 'entidade': producao.entidade, 'ano': producao.ano,
                              'producao_anual': producao.producao_anual} for producao in producao_results]

            data = {'producao': producao_data}

        json_data = json.dumps(data, indent=4)

        response = make_response(json_data)
        response.headers['Content-Disposition'] = 'attachment; filename=data.json'
        response.headers['Content-Type'] = 'application/json'

        return response
    except Exception as e:
        print("Erro ao exportar como JSON:", str(e))
        return jsonify({'message': 'Erro ao exportar como JSON'}), 500

## Filtro de Busca
# Produção:


def search_filter_producao():
    search_term = request.form.get('search')

    try:
        if search_term:
            producao_results = db.session.query(ProducaoPlastico).filter(
                db.or_(ProducaoPlastico.entidade.ilike(f'%{search_term}%'),
                       ProducaoPlastico.ano.ilike(f'%{search_term}%'),
                       ProducaoPlastico.producao_anual.ilike(f'%{search_term}%'))
            ).all()
        else:
            producao_results = db.session.query(ProducaoPlastico).all()

        return render_template('producao.html', dados=producao_results)
    except Exception as e:
        print("Erro ao filtrar resultados:", str(e))
        return jsonify({'message': 'Erro ao filtrar resultados'}), 500

def search_filter_despejo():
    search_term = request.form.get('search')

    try:
        if search_term:
            despejo_results = db.session.query(ParticipacaoDespejo).filter(
                db.or_(ParticipacaoDespejo.entidade.ilike(f'%{search_term}%'),
                       ParticipacaoDespejo.codigo.ilike(f'%{search_term}%'),
                       ParticipacaoDespejo.ano.ilike(f'%{search_term}%'),
                       ParticipacaoDespejo.participacao.ilike(f'%{search_term}%'))
            ).all()
        else:
            despejo_results = db.session.query(ParticipacaoDespejo).all()

        return render_template('despejo.html', dados=despejo_results)
    except Exception as e:
        print("Erro ao filtrar resultados:", str(e))
        return jsonify({'message': 'Erro ao filtrar resultados'}), 500
