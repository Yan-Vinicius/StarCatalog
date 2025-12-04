import argparse
from StarCatalog import StarCatalog
from StarVisualizer import StarVisualizer3D


def parse_args():
    parser = argparse.ArgumentParser(
        description="Visualização 3D de estrelas usando catálogos Gaia"
    )
    parser.add_argument(
        "--query-file", type=str, required=True,
        help="Caminho para o arquivo .sql que contém a consulta ao catálogo Gaia"
    )
    parser.add_argument(
        "--max-mag", type=float, default=None,
        help="Filtrar estrelas com magnitude menor que este valor (opcional)"
    )
    parser.add_argument(
        "--show", action="store_true",
        help="Mostrar o gráfico interativo 3D"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Caminho de arquivo para salvar o gráfico (opcional)"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    catalog = StarCatalog.from_query_file(args.query_file)

    if args.max_mag is not None:
        catalog = catalog.filter_by_magnitude(args.max_mag)

    visualizer = StarVisualizer3D(catalog)
    if args.show:
        visualizer.plot(color_by='magnitude', cmap='viridis', size=6)
    if args.output:
        import matplotlib.pyplot as plt
        fig = plt.gcf()
        fig.savefig(args.output, dpi=300)

if __name__ == "__main__":
    main()
