from io import BytesIO
from matplotlib import pyplot as plt

class Tex2Svg:

    def __init__(self, formula):

        self.formula = formula

    def tex2svg(self, fontsize=2, dpi=300):
        """Render TeX formula to SVG.
        Args:
            formula (str): TeX formula.
            fontsize (int, optional): Font size.
            dpi (int, optional): DPI.
        Returns:
            str: SVG render.
        """

        fig = plt.figure(figsize=(5, 5))
        fig.text(0, 0, r'{}'.format(self.formula), fontsize=fontsize, color="white")

        output = BytesIO()
        fig.savefig(output, dpi=dpi, transparent=True, format='svg',
                    bbox_inches='tight', pad_inches=0.01, frameon=False)
        plt.close(fig)

        output.seek(0)
        return output.read()