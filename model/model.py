import networkx as nx
from database.DAO import DAO
import flet as ft

class Model:

    def __init__(self):
        self._listaPaesi = DAO.getStati()
        self._idMap = {}
        for paese in self._listaPaesi:
            self._idMap[paese.codice] = paese
        self._grafo = nx.Graph()

    def creaGrafo(self, anno):
        self._grafo.clear()
        situa = DAO.getSituaBeforeYear(anno)
        for confine in situa:
            if self._idMap[confine[0]] not in self._grafo.nodes:
                self._grafo.add_node(self._idMap[confine[0]])
            if self._idMap[confine[1]] not in self._grafo.nodes:
                self._grafo.add_node(self._idMap[confine[1]])
            self._grafo.add_edge(self._idMap[confine[0]], self._idMap[confine[1]])
        return self._grafo

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getStati(self):
        return self._grafo.nodes

    def trovaRaggiungibili(self, codStato):
        print(codStato)
        stato = self._idMap[int(codStato)]
        raggiungibili = nx.bfs_tree(self._grafo, stato)
        return [s for s in raggiungibili]