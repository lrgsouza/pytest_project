## PYTEST

### Processo de instalação
```
pip install pytest
```

### Configuração dos testes
 - Para configurar os testes basta criar um arquivo com test_<>.py no diretorio onde deseja executar os testes.
- Dentro deste arquivo, importe as classes e modulos que deseja testar.
```
import calculadora
```
- para criar um caso de test, defina funções também com o prefixo test_
```
def test_somar():
    assert calculadora.somar(2,2) == 4
```
O assert é responsável por verificar se sua função está retornando corretamente o que é esperado, desta forma se sua função estiver funcionando corretamente. A execução do teste será dada como sucesso.
### Execução dos testes
- Para executar os testes presentes no seu diretório, basta rodar:
```
pytest
```
Desta forma todos os testes corretamente configurados serão executados.
