import webapp
import random

class aleat(webapp.app):

    def process(self, parsedRequest):
        num = random.randint(0, 100000000000)
        num = "/aleat/" + str(num)
        return ("200 OK", "<html><body><h1>" +
                          "<a href=" + num + ">Dame mas</a>" +
                          "</h1></body></html>")

if __name__ == "__main__":
    aleatApp = aleat()
    testAleat = webapp.webApp("localhost", 1234, {'/aleat': aleatApp})
