import flet as ft
import networkx as nx

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = int(self._view._txtAnno.value)
        if 1816 < anno < 2016:
            grafo = self._model.creaGrafo(anno)
            self._view._txt_result.controls.append(
                ft.Text(f"componenti connesse: {len(list(nx.connected_components(grafo)))}"))
            for stato in grafo.nodes:
                self._view._txt_result.controls.append(ft.Text(f"{stato.__str__()}: {grafo.degree()[stato]} stati confinanti"))
            self._view._btnRaggiungibili.disabled = False
            self.popolaStati()
        else:
            self._view.create_alert("Un anno tra il 1816 e il 2016 pirla")
        self._view.update_page()

    def popolaStati(self):
        paesi = self._model.getStati()
        for stato in paesi:
            self._view._ddStati.options.append(ft.dropdown.Option(text=stato.nome, key=stato.codice))

    def handleRaggiungibili(self, e):
        ragg = self._model.trovaRaggiungibili(self._view._ddStati.value)
        self._view._txt_result.controls.clear()
        for stato in ragg:
            self._view._txt_result.controls.append(ft.Text(f"{stato.__str__()}"))
        self._view.update_page()