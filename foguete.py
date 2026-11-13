import time


def contagem_regressiva(inicio=5):
    for i in range(inicio, 0, -1):
        print(i)
        time.sleep(1)
    print("🚀 Decolagem!")


if __name__ == "__main__":
    contagem_regressiva()
