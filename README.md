locust -f locustfile.py --headless -u 10 -r 1 --run-time 1m --csv=resultado_10_users

locust -f locustfile.py --headless -u 50 -r 5 --run-time 1m --csv=resultado_50_users

locust -f locustfile.py --headless -u 100 -r 10 --run-time 1m --csv=resultado_100_users

locust -f locustfile.py --headless -u 500 -r 10 --run-time 1m --csv=resultado_500_users