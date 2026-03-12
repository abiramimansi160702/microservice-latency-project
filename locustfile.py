from locust import HttpUser, task

class MicroserviceUser(HttpUser):

    @task
    def call_gateway(self):
        self.client.get("/")