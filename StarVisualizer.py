import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from StarCatalog import StarCatalog


class StarVisualizer3D:
    """
    Classe para visualização 3D de um StarCatalog usando matplotlib.
    """

    def __init__(self, star_catalog: StarCatalog):
        """
        Args:
            star_catalog (StarCatalog): catálogo de estrelas a visualizar.
        """
        self.fig = None
        self.ax = None
        self.catalog = star_catalog


    def _show_star_info(self, star):
        x, y, z = star.to_cartesian()

        ra_val = star.ra if star.ra is not None else float('nan')
        dec_val = star.dec if star.dec is not None else float('nan')
        dist_val = star.distance if star.distance is not None else float('nan')

        label = (f"Designação: {star.designation}\n"
                 f"Source id: {star.source_id}\n"
                 f"RA: {ra_val:.4f}°\n"
                 f"Dec: {dec_val:.4f}°\n"
                 f"Dist: {dist_val:.2f} pc\n"
                 f"Magnitude: {star.magnitude}"
                 )
        x2, y2, _ = proj3d.proj_transform(x, y, z, self.ax.get_proj())
        star_info_fig = plt.figure("Dados da estrela", figsize=(4, 3))
        ax2 = star_info_fig.add_subplot(111)
        ax2.axis('off')
        ax2.text(0.5, 0.5, label, ha='center', va='center')
        plt.show(block=False)
        plt.title("Dados da estrela")


    def _on_pick(self, event):
        ind = event.ind[0]  # índice do ponto clicado
        star = self.catalog.stars[ind]
        # Mostrar janela ou anotação
        self._show_star_info(star)


    def plot(self, color_by: str = 'magnitude',
             cmap: str = 'viridis', size: float = 15, invert_ra: bool = True):
        """
        Plota as estrelas em 3D.
        Args:
            color_by (str): nome do atributo pelo qual colorir os pontos (ex: 'magnitude').
            cmap (str): colormap do matplotlib.
            size (float): tamanho dos pontos.
            invert_ra (bool): se True, inverte o eixo X (RA) para convenção astronômica.
        """
        xs, ys, zs = self.catalog.to_cartesian_arrays()

        self.fig = plt.figure("Estrelas",figsize=(8, 6))
        self.ax = self.fig.add_subplot(111, projection='3d')

        colors = None
        if color_by == 'magnitude':
            mags = [s.magnitude for s in self.catalog.stars]
            colors = mags

        sc = self.ax.scatter(xs, ys, zs, c=colors, cmap=cmap, s=size, picker=True)

        if colors is not None:
            self.fig.colorbar(sc, label=color_by)

        self.ax.set_xlabel('X - zero de RA')
        self.ax.set_ylabel('Y - ra')
        self.ax.set_zlabel('Z - dec')
        self.ax.set_title('Mapa das estrelas em 3D')

        if invert_ra:
            self.ax.invert_xaxis()

        self.fig.canvas.mpl_connect('pick_event', self._on_pick)
        plt.show(block=True)