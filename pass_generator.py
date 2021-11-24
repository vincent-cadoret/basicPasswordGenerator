import secrets
import string


def getPass(size):
    i = 0
    alphabet = string.ascii_letters + string.punctuation + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(int(size)))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password


if __name__ == "__main__":
    print("Générateur de mot de passe - Vincent Cadoret")
    size = input("Quelle est la taille du mot de passe souhaité: ")
    print("Résultat: " + getPass(size))
    print("Fin normale du programme ! - v1.0")