<h1>RTM API Client</h1>
<p>Cette API permet de se connecter à l'API RTM et de récupérer des factures.</p>
<h2>Classe RtmClient</h2>
<p>La classe RtmClient permet de se connecter à l'API RTM et de récupérer des factures.</p>
<h3>Constructeur</h3>
<pre>
def __init__(self):
</pre>
<p>Le constructeur initialise les variables nécessaires pour se connecter à l'API RTM et récupérer des factures.</p>
<h3>Méthode login</h3>
<pre>
def login(self):
</pre>
<p>Cette méthode envoie une requête de connexion à l'API RTM avec l'email et le mot de passe de l'utilisateur. Si la connexion réussit, les variables user_id, token et code_client sont mises à jour et la méthode retourne True. Si la connexion échoue, la méthode retourne False.</p>
<h3>Méthode get_all_bills</h3>
<pre>
def get_all_bills(self):
</pre>
<p>Cette méthode envoie une requête à l'API RTM pour récupérer la liste des factures de l'utilisateur connecté. La méthode retourne la liste des factures sous forme de dictionnaire Python.</p>
<h3>Méthode get_bill_by_id</h3>
<pre>
def get_bill_by_id(self, id_bill):
</pre>
<p>Cette méthode retourne le lien d'une facture à partir de son identifiant .</p>
<h2>Exemple d'utilisation</h2>
<pre>
if __name__ == "__main__":
    rtm_client = RtmClient()
    # Connect to RTM API
    if rtm_client.login():
        # Get list of bills
        bills = rtm_client.get_all_bills()

        for bill in bills:
            print(rtm_client.get_bill_by_id(bill["PK_VENTES"]))
    else:
        print("Error: Login failed")
</pre>
<p>Cet exemple crée une instance de la classe RtmClient, se connecte à l'API RTM et récupère la liste des factures de l'utilisateur. Pour chaque facture de la liste, l'URL de la facture est affichée.</p>