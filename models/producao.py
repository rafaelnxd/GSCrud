from flask import Flask, render_template, request, redirect, jsonify
from models.connection import db
from models.insert import ProducaoPlastico


def producao():
    try:
        if request.method == 'POST':
            entidade = request.form.get('entidade')
            ano = request.form.get('ano')
            producao_anual = request.form.get('producao_anual')

            nova_insercao = ProducaoPlastico(entidade=entidade, ano=ano, producao_anual=producao_anual)

            try:
                db.session.add(nova_insercao)
                db.session.commit()
                print("Inserido com sucesso!")
                return redirect('/producao')
            except Exception as e:
                print("Erro ao inserir:", str(e))
                db.session.rollback()
                return jsonify({'message': 'Erro ao inserir'}), 500

        # Use the session object to query the database
        dados = db.session.query(ProducaoPlastico).all()
        return render_template('producao.html', dados=dados)
    except Exception as e:
        print("Erro na rota principal:", str(e))
        return jsonify({'message': 'Erro na rota principal'}), 500
    
def excluirProducao(id):
    dado = db.session.query(ProducaoPlastico).filter_by(id=id).first_or_404()
    try:
        db.session.delete(dado)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'})
    except Exception as e:
        print("Erro ao excluir empresa:", str(e))
        db.session.rollback()
        return jsonify({'message': 'Erro ao excluir'}), 500
    


def obterDadosProducao(id):
    try:
        dado = db.session.query(ProducaoPlastico).filter_by(id=id).first_or_404()
        return jsonify({
            'id': dado.id,
            'entidade': dado.entidade,
            'ano': dado.ano,
            'producao_anual': dado.producao_anual,
        })
    except Exception as e:
        print("Erro ao obter dados", str(e))
        return jsonify({'message': 'Erro ao obter dados'}), 500
    


def editarProducao():
    id = request.form['id']
    dado = db.session.query(ProducaoPlastico).filter_by(id=id).first_or_404()
    
    dado.entidade = request.form['entidade']
    dado.ano = int(request.form['ano'])
    dado.producao_anual = float(request.form['producao_anual'])

    try:
        db.session.commit()
        return redirect('/producao')  
    except Exception as e:
        print("Erro ao atualizar", str(e))
        db.session.rollback()
        return jsonify({'message': 'Erro ao atualizar'}), 500