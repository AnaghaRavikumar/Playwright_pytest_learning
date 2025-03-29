from playwright.sync_api import Playwright

orders_payload = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "67a8df1ac0d3e6622a297ccb"
        }
    ]
}
class APIUtils:

    def get_token(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data= {"userEmail":"aghirm@gmail.com","userPassword":"12345678"})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self,playwright:Playwright):
        token = self.get_token(playwright) #method has an argument, so we need to send it there, this is to  ensure  same instance of playwright
        api_request_contest  = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client") #need this to set context, set connection to the server
        response = api_request_contest.post("/api/ecom/order/create-order",
                                 data= orders_payload,
                                 headers={"Authorization": token,
                                          "Content-type":"application/json"
                                          })
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id


