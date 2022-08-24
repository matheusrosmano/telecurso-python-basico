from basico.escola import Escola
from basico.lista_escola import ListaEscola


class TestEscola:
    def test_escola_comparar_mesmo_cnpj_retorna_verdadeiro(self):
        entrada = 11111111111111
        esperado = True

        escola1 = Escola()
        escola1.cnpj = entrada

        escola2 = Escola()
        escola2.cnpj = entrada

        resultado = escola1 == escola2
        assert resultado == esperado

    def test_nao_add_escola_em_lista_caso_cnpj_igual(self):
        entrada_cnpj = 11111111111111
        esperado = False

        escola1 = Escola()
        escola1.cnpj = entrada_cnpj
        escola2 = Escola()
        escola2.cnpj = entrada_cnpj

        lista_escola = ListaEscola()
        lista_escola.append(escola1)
        resultado = lista_escola.append(escola2)
        assert resultado == esperado
