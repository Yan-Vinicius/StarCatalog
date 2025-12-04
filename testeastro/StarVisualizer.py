class StarVisualizer3D:
    """
    Classe para visualização de um StarCatalog em 3D usando matplotlib.
    """
    def __init__(self, star_catalog: StarCatalog):
        self.catalog = star_catalog

    def plot(self, color_by='magnitude', cmap='viridis', size=5, invert_ra=True):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        xs, ys, zs = self.catalog.to_cartesian_arrays()
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        colors = None
        if color_by == 'magnitude':
            # extrair magnitude
            mags = [s.magnitude for s in self.catalog.stars]
            colors = mags
        sc = ax.scatter(xs, ys, zs, c=colors, cmap=cmap, s=size)
        if colors is not None:
            fig.colorbar(sc, label=color_by)
        ax.set_xlabel('X (pc)')
        ax.set_ylabel('Y (pc)')
        ax.set_zlabel('Z (pc)')
        ax.set_title('3D map of stars')
        if invert_ra:
            ax.invert_xaxis()
        plt.show()