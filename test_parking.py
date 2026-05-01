import requests

BASE_URL = "http://127.0.0.1:5000"

score = 0

def print_result(name, success):
    global score
    if success:
        print(f"[✔] {name}")
        score += 3
    else:
        print(f"[✘] {name}")


def test_create_parking():
    r = requests.post(f"{BASE_URL}/parkings", json={
        "nome": "Central",
        "endereco": "Rua A"
    })
    ok = r.status_code in [200, 201]
    print_result("Criar estacionamento", ok)
    return r.json()["data"]["id"] if ok else None


def test_create_spot(pid):
    r = requests.post(f"{BASE_URL}/spots", json={
        "codigo": "A1",
        "ocupada": False,
        "parking_id": pid
    })
    ok = r.status_code in [200, 201]
    print_result("Criar vaga", ok)
    return r.json()["data"]["id"] if ok else None


def test_update_spot(spot_id):
    r = requests.patch(f"{BASE_URL}/spots/{spot_id}", json={
        "ocupada": True
    })
    print_result("Atualizar status vaga", r.status_code == 200)


def test_invalid_parking():
    r = requests.post(f"{BASE_URL}/spots", json={
        "codigo": "X",
        "ocupada": False,
        "parking_id": 999
    })
    print_result("Erro estacionamento inválido", r.status_code == 404)


def test_list_spots():
    r = requests.get(f"{BASE_URL}/spots")
    print_result("Listar vagas", r.status_code == 200)


def test_spots_by_parking(pid):
    r = requests.get(f"{BASE_URL}/parkings/{pid}/spots")
    print_result("Vagas por estacionamento", r.status_code == 200)


def test_validation():
    r = requests.post(f"{BASE_URL}/parkings", json={})
    print_result("Validação estacionamento", r.status_code == 400)


print("\n🚀 Testes - Estacionamento\n")

pid = test_create_parking()

if pid:
    sid = test_create_spot(pid)
    test_spots_by_parking(pid)

    if sid:
        test_update_spot(sid)

test_invalid_parking()
test_list_spots()
test_validation()

print(f"\n🎯 Pontuação: {score}/30\n")