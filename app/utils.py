from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_func(password):
    return pwd_context.hash(password)


def verify_func(password, hashed_password):
    return pwd_context.verify(password, hashed_password)
