from flask import Flask, render_template, request, redirect, jsonify
from models.connection import db
from models.insert import ParticipacaoDespejo

def despejo():
    try:
        if request.method == 'POST':
            entidade = request.form.get('entidade')
            codigo = request.form.get('codigo')
            ano = request.form.get('ano')
            participacao = request.form.get('participacao')

            nova_insercao = ParticipacaoDespejo(entidade=entidade, codigo=codigo, ano=ano, participacao=participacao)

            try:
                db.session.add(nova_insercao)
                db.session.commit()
                print("Inserido com sucesso!")
                return redirect('/despejo')
            except Exception as e:
                print("Erro ao inserir:", str(e))
                db.session.rollback()
                return jsonify({'message': 'Erro ao inserir'}), 500

        # Use the session object to query the database
        dados = db.session.query(ParticipacaoDespejo).all()
        return render_template('despejo.html', dados=dados)
    except Exception as e:
        print("Erro na rota principal:", str(e))
        return jsonify({'message': 'Erro na rota principal'}), 500
    

def excluirDespejo(id):
    dado = db.session.query(ParticipacaoDespejo).filter_by(id=id).first_or_404()
    try:
        db.session.delete(dado)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'})
    except Exception as e:
        print("Erro ao excluir:", str(e))
        db.session.rollback()
        return jsonify({'message': 'Erro ao excluir'}), 500
    

def editarDespejo():
    id = request.form['id']
    dado = db.session.query(ParticipacaoDespejo).filter_by(id=id).first_or_404()
    
    dado.entidade = request.form.get('entidade')
    dado.codigo = request.form.get('codigo')
    dado.ano = request.form.get('ano')
    dado.participacao = request.form.get('participacao')

    try:
        db.session.commit()
        return redirect('/despejo')  
    except Exception as e:
        print("Erro ao atualizar", str(e))
        db.session.rollback()
        return jsonify({'message': 'Erro ao atualizar'}), 500


def obterDadosDespejo(id):
    try:
        dado = db.session.query(ParticipacaoDespejo).filter_by(id=id).first_or_404()
        return jsonify({
            'id': dado.id,
            'entidade': dado.entidade,
            'codigo': dado.codigo,
            'ano': dado.ano,
            'participacao': dado.participacao
        })
    except Exception as e:
        print("Erro ao obter dados", str(e))
        return jsonify({'message': 'Erro ao obter dados'}), 500