from locust import HttpUser, task, between

class MercadoLivreUser(HttpUser):
    wait_time = between(1, 3)    
    host = "https://www.mercadolivre.com.br"

    @task(5)
    def acessar_home(self):
        self.client.get("/")

    @task(4)
    def buscar_produto(self):
        self.client.get("https://lista.mercadolivre.com.br/celular")

    @task(3)
    def navegar_categoria(self):
        self.client.get("/ofertas#nav-header")

    @task(2)
    def aplicar_filtros(self):
        self.client.get("https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/celular_PriceRange_1000")

    @task(4)
    def ver_detalhes_produto(self):
        self.client.get("/smartphone-samsung-galaxy-a25-5g-256gb-8gb-ram-dual-sim-android-14-azul-escuro-65/p/MLB31498601")  


