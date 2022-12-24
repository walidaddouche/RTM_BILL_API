from setuptools import setup

setup(
    name='rtm_client',  # Nom de votre librairie
    version='0.1',  # Numéro de version de votre librairie
    py_modules=['rtm_client'],  # Liste des modules à inclure dans la librairie
    author='Walid',  # Nom de l'auteur de la librairie
    author_email='##',  # Adresse email de l'auteur
    url='https://github.com/walidaddouche/RTM_BILL_MAILER',  # URL du référentiel sur GitHub
    license='MIT',  # Licence sous laquelle votre librairie est publiée
    description='A RTM client library',  # Description de votre librairie
    install_requires=['requests'],  # Liste des dépendances de votre librairie
)
