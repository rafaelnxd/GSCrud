
from flask import Flask, render_template, request, redirect, jsonify, url_for, send_file, make_response
from models.connection import SECRET_KEY, SQL_KEY, db
from models.insert import ProducaoPlastico, ParticipacaoDespejo
from models.despejo import despejo, excluirDespejo, editarDespejo, obterDadosDespejo
from models.producao import producao, excluirProducao, editarProducao, obterDadosProducao
from models.export_search import export_json, search_filter_despejo, search_filter_producao

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQL_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.config['SECRET_KEY'] = SECRET_KEY

## Crud ##

## Rotas da tabela de Produção de Plástico Global:
@app.route('/producao', methods=['GET', 'POST'])
def producaoRoute():
    return producao()

@app.route('/excluir/<int:id>', methods=['DELETE'])
def excluirProducaoRoute(id):
    return excluirProducao(id)
    
@app.route('/editar/<int:id>', methods=['GET'])
def obterDadosProducaoRoute(id):
    return obterDadosProducao(id)
    
@app.route('/editar', methods=['POST'])
def editarProducaoRoute():
    return editarProducao()

      
## Rotas da tabela de Produção de Despejo:
@app.route('/despejo', methods=['GET', 'POST'])
def despejoRoute():
    return despejo()

@app.route('/excluirDes/<int:id>', methods=['DELETE'])
def excluirDespejoRoute(id):
    return excluirDespejo(id)
 
@app.route('/editarDes', methods=['POST'])
def editarDespejoRoute():
    return editarDespejo()

@app.route('/editarDes/<int:id>', methods=['GET'])
def obterDadosDespejoRoute(id):
    return obterDadosDespejo(id)
   
    

## Rota para exportar como JSON
@app.route('/export_json', methods=['POST'])
def exportJsonRoute():
    return export_json()
    

## Filtro de Busca
# Produção:
@app.route('/search_filter_producao', methods=['POST'])
def searchFilterProducaoRoute():
    return search_filter_producao()
    
# Despejo:
@app.route('/search_filter_despejo', methods=['POST'])
def searchFilterDespejoRoute():
    return search_filter_despejo()
    

## Rota do menu:    
@app.route('/')
def mainRoute():
    return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True)