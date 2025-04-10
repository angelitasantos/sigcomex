import pytest
from .models import Teste1Categoria, Teste1Grupo, Teste1Cliente


@pytest.mark.django_db
def test_cria_categoria():
    categoria = Teste1Categoria.objects.create(nome="Categoria A", status="A")
    assert categoria.nome == "Categoria A"
    assert categoria.status == "A"
    assert str(categoria) == "Categoria A"


@pytest.mark.django_db
def test_cria_grupo():
    grupo = Teste1Grupo.objects.create(nome="Grupo B", status="I")
    assert grupo.nome == "Grupo B"
    assert grupo.status == "I"
    assert str(grupo) == "Grupo B"


@pytest.mark.django_db
def test_cria_cliente_completo():
    categoria = Teste1Categoria.objects.create(nome="Cat", status="A")
    grupo = Teste1Grupo.objects.create(nome="Grp", status="A")
    cliente = Teste1Cliente.objects.create(
        nome="Cliente X",
        razao_social="Razão X",
        cnpj="00.000.000/0001-00",
        insc_est="12345",
        sigla_imp="IMP",
        sigla_exp="EXP",
        serv_sigla_imp="SIM",
        serv_sigla_exp="SEX",
        cod_interno="C001",
        observacoes="Teste obs",
        status="A",
        grupo=grupo,
        categoria=categoria,
    )
    assert cliente.nome == "Cliente X"
    assert cliente.grupo == grupo
    assert cliente.categoria == categoria
    assert str(cliente) == "Cliente X"


@pytest.mark.django_db
def test_cria_cliente_minimo():
    cliente = Teste1Cliente.objects.create(
        nome="Cliente Y",
        status="I"
    )
    assert cliente.razao_social is None
    assert cliente.categoria is None
    assert str(cliente) == "Cliente Y"
