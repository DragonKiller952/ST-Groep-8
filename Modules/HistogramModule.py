from mesa.visualization.ModularVisualization import VisualizationElement

class HistogramModule(VisualizationElement):
    package_includes = ["Chart.min.js"]
    local_includes = ["HistogramModule.js"]

    def __init__(self, bins, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.bins = bins
        histogram = f'new HistogramModule({bins}, {bins}, {canvas_width}, {canvas_height})'
        self.js_code = "elements.push(" + histogram + ");"

    def render(self, model):
        all_vote_percentages = [model.get_percentage(party.votes) for party in model.partys]
        colors = [party.color for party in model.partys]
        return (all_vote_percentages, colors)