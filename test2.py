import pygal
b_chart = pygal.Bar()
b_chart.title = "Destiny Kill/Death Ratio"
b_chart.add("Dijiphos", [0.94])
b_chart.add("Punisherdonk", [1.05])
b_chart.add("Musclemuffins20", [1.10])
b_chart.render_in_browser()

