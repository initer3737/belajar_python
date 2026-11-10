import re
class ElysiaClone:
    def __init__(self):
        self.routes = []

    def get(self, path, handler):
        self.routes.append({"method": "GET", "path": path, "handler": handler})
        return self
        
    def post(self, path, handler):
        self.routes.append({"method": "POST", "path": path, "handler": handler})
        return self  

    def listen(self, port):
        # print(f"🦊 Server running on port {port}")
        print(f"Server running on port {port}")
        for route in self.routes:
            print(f"  [{route['method']}] {route['path']} handler:{route['handler']()} is registered")
        return self

app = ElysiaClone()

app.get("/", lambda:"Hello World") \
   .post("/login", lambda: "Success") \
   .listen(3000)

server='/products/:id'
user='/products/3'
def elysia_get_data(path:str,handler):
    data_regex={}
    regex_data=re.findall(pattern=r":[\w]+",string=server)
    for data in regex_data:
        idx_list_data=user.split("/")
        idx_list_server=server.split("/")
        data_regex[data.replace(":","")]=idx_list_data[idx_list_server.index(data)]
    print(f"hasil1 {data_regex}")
    print(f"hasil {regex_data}")
    handler(data_regex)

elysia_get_data(path=server,handler=lambda x:print('x adalah ',x))    
