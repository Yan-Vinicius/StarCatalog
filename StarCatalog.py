from Star import Star
from astroquery.gaia import Gaia
import numpy as np

class StarCatalog:
    """
    Container para um conjunto de estrelas, com métodos para carregar dados, filtrar, converter etc.
    """
    def __init__(self, stars=None):
        # lista de objetos
        self.stars = stars or []


    @classmethod
    def from_query_file(cls, query_file_path: str):
        """
        Carrega um catálogo de estrelas executando a query lida de um arquivo .sql
        Args:
            query_file_path (str): caminho para o arquivo que contém a consulta SQL/ADQL.
        Returns:
            stars: instância com a lista de estrelas carregadas.
        """
        with open(query_file_path, 'r') as f:
            query = f.read()
        job = Gaia.launch_job(query)
        table = job.get_results().to_pandas()
        stars = []
        for _, row in table.iterrows():
            star = Star(
                ra=row['ra'],
                dec=row['dec'],
                distance=None,
                magnitude=row.get('phot_g_mean_mag', "Magnitude não achada"),
                other_props=row.to_dict(),
                designation=row['designation'],
                source_id=row.get('source_id', "Source id não achado"),
            )
            stars.append(star)

        return cls(stars)

    @classmethod
    def from_gaia_query(cls, query_string, limit=500):
        """
        Metodo de classe para realizar consulta ao catálogo Gaia via astroquery,
        construir objetos Star e devolver instância de StarCatalog.
        """
        job = Gaia.launch_job(query_string)
        table = job.get_results().to_pandas()
        stars = []
        for _, row in table.iterrows():
            star = Star(
                ra = row['ra'],
                dec = row['dec'],
                distance = None,
                magnitude = row.get('phot_g_mean_mag', None),
                other_props = row.to_dict()
            )
            stars.append(star)
        return cls(stars)


    def filter_by_magnitude(self, max_mag):
        """
        Filtra o catálogo e retorna novo StarCatalog com magnitude menor que max_mag.
        """
        filtered = [s for s in self.stars if s.magnitude is not None and s.magnitude < max_mag]
        return StarCatalog(filtered)

    def to_cartesian_arrays(self):
        """
        Retorna arrays numpy x, y, z correspondentes a todas as estrelas.
        """
        xs, ys, zs = [], [], []
        for s in self.stars:
            x, y, z = s.to_cartesian()
            xs.append(x)
            ys.append(y)
            zs.append(z)

        return np.array(xs), np.array(ys), np.array(zs)

