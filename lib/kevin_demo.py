import rabbit, json

url = "https://jsonplaceholder.typicode.com/posts/1/comments"
myJson = rabbit.Curler(url).getJson()

sender = rabbit.Sender(myJson)
sender.send()

recr = rabbit.Receiver()
print(recr.receive())
