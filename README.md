# Teste de Performance com Locust

Este projeto utiliza o [Locust](https://locust.io/) para realizar testes de performance em aplicações web. O objetivo é simular diferentes cargas de usuários e coletar dados sobre o desempenho da aplicação.


## Instalação

Clone este repositório:
``` 
git clone https://github.com/rayanemelo/teste-de-performance-locust
cd teste-de-performance-locust
```

## Executando os Testes
Para executar os testes de performance, usando Docker Compose:

``` 
docker-compose up --abort-on-container-exit
``` 

Para executar localmente, certifique-se de ter o Locust instalado em sua máquina. Se ainda não tiver, você pode instalá-lo com o seguinte comando:
``` 
pip install locust
``` 

Depois de instalar o Locust, você pode executar os seguintes comandos para realizar os testes:
``` 
# Teste com 10 usuários
locust -f locustfile.py --headless -u 10 -r 1 --run-time 1m --csv=resultado_10_users

# Teste com 50 usuários
locust -f locustfile.py --headless -u 50 -r 5 --run-time 1m --csv=resultado_50_users

# Teste com 100 usuários
locust -f locustfile.py --headless -u 100 -r 10 --run-time 1m --csv=resultado_100_users

# Teste com 500 usuários
locust -f locustfile.py --headless -u 500 -r 10 --run-time 1m --csv=resultado_500_users 
``` 