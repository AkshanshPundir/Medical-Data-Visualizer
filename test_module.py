import unittest
import medical_data_visualizer
import matplotlib as mpl

class DataVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.cat_plot = medical_data_visualizer.draw_cat_plot()
        self.heat_map = medical_data_visualizer.draw_heat_map()

    def test_cat_plot(self):
        self.assertEqual(type(self.cat_plot), mpl.figure.Figure, "Expected draw_cat_plot to return a matplotlib figure.")
        actual = [len(axes.containers) for axes in self.cat_plot.axes]
        self.assertEqual(actual, [2, 2], "Expected two sets of bar plots in the categorical plot.")

    def test_heat_map(self):
        self.assertEqual(type(self.heat_map), mpl.figure.Figure, "Expected draw_heat_map to return a matplotlib figure.")
        # Check collections instead of get_images() for modern seaborn compatibility
        actual = len(self.heat_map.axes[0].collections)
        self.assertGreaterEqual(actual, 1, "Expected at least one collection in the correlation heatmap.")

if __name__ == "__main__":
    unittest.main()