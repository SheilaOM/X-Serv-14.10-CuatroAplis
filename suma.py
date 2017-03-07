import webapp


class suma(webapp.app):
    def __init__(self):
        self.cont = 0
        self.sumando = []

    def parse(self, request, rest):
        return rest

    def process(self, parsedRequest):
        if parsedRequest == "favicon.ico":
            return("404 Not Fount", "<html><body><h1>Not found" +
                   "</h1></body></html>")

        try:
            recurso = int(parsedRequest)
            self.sumando.insert(self.cont, recurso)
            self.cont += 1
            print("cont: " + str(self.cont))

        except ValueError:
            return("200 OK", "<html><body><h1>Suma</h1>" +
                             "<p>Me has dado un " + recurso + ". Vete" +
                             "</p></body></html>\r\n")

        if self.cont == 1:
            print("PPR: " + parsedRequest)

            return("200 OK", "<html><body><h1>Calculadora</h1>" +
                             "<p>Me has dado un " +
                             str(self.sumando[self.cont-1]) +
                             ". Dame otro</p></body></html>\r\n")
        elif self.cont == 2:
            suma = self.sumando[0] + self.sumando[1]
            contad = self.cont
            self.cont = 0
            return("200 OK", "<html><body><h1>Calculadora</h1>" +
                             "<p>Me habias dado un " +
                             str(self.sumando[contad-2]) +
                             ". Ahora me has dado un " +
                             str(self.sumando[contad-1]) +
                             ". La suma es " + str(suma) + "</p>" +
                             "</body></html>\r\n")

if __name__ == "__main__":
    sumaApp = suma()
    testSuma = webapp.webApp("localhost", 1234, {'/suma/': sumaApp})
