from py2neo import Graph,Node,Relationship
import random

graph = Graph("bolt://localhost:7687", username="neo4j", password="1234")



num_intentos=3
def genera_pregunta2(num_intentos):

        cursor = graph.run("Match (a)-[r]->(m) return a.name,labels(a),TYPE(r),m.title,labels(m), rand() as l ORDER BY l LIMIT 1")


        cursor.forward()
        p="¿What" + " " + cursor.current["labels(a)"][0] + " " + cursor.current["TYPE(r)"] + " " + "the" + " " + cursor.current["labels(m)"][0] + " " + cursor.current["m.title"] + "?"
        p=p.replace("_"," ")

        #p =("¿Qué", cursor.current["labels(a)"], cursor.current["TYPE(r)"], "el/la", cursor.current["labels(m)"],cursor.current["m.title"], "?")
        v1=(cursor.current["a.name"])
        tipo_pregunta= cursor.current["labels(a)"][0]
        tipo_destino = cursor.current["labels(m)"][0]
        names = [v1]

        s = cursor.current["TYPE(r)"]
        #
        c = cursor.current["m.title"]
        #
        # print(s,c)
        # print("Match ("+tipo_pregunta+")-[:" + s + "]->(m) where not ("+tipo_pregunta+")-[:"+ s +"]->(:"+tipo_destino+"{title:'" + c  + "' }) return ("+tipo_pregunta+").name, rand() as l ORDER BY l LIMIT 3")
        cursor2 = graph.run("Match ("+tipo_pregunta+")-[:" + s + "]->(m) where not ("+tipo_pregunta+")-[:"+ s +"]->(:"+tipo_destino+"{title:'" + c  + "' }) return ("+tipo_pregunta+").name, rand() as l ORDER BY l LIMIT 3")

        # cursor2.forward()
        # print(cursor2.current["b.name"])



        names2 = []
        for field in cursor2:
            names2.append(field["("+tipo_pregunta+").name"])

        # print(names2)
        names +=names2


        random.shuffle(names)
        l=(names)

        inames=len(names)
        # print(inames)

        i=names.index(cursor.current["a.name"])

        if inames == 4:
                return p,l,i
        else:
                if num_intentos>0:
                        return genera_pregunta2(num_intentos-1)
                else:
                        return "No se pudo generar la pregunta", [], -1

print (genera_pregunta2(num_intentos))