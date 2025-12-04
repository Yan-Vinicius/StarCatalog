import numpy as np

class Star:
    """
    Representa uma estrela com propriedades básicas.
    """
    def __init__(self, ra, dec, distance, magnitude, other_props, designation, source_id):
        self.ra = ra                # em graus
        self.dec = dec              # em graus
        self.distance = distance    # em parsec ou outra unidade
        self.magnitude = magnitude
        self.other_props = other_props or {}
        self.designation = designation
        self.source_id = source_id


    def to_cartesian(self):
        """
        Converte ra, dec e distance em coordenadas cartesiana x, y, z
        """
        # converter graus para radianos
        ra_rad = np.deg2rad(self.ra)
        dec_rad = np.deg2rad(self.dec)
        r = self.distance if self.distance is not None else 1.0
        x = r * np.cos(dec_rad) * np.cos(ra_rad)
        y = r * np.cos(dec_rad) * np.sin(ra_rad)
        z = r * np.sin(dec_rad)
        return x, y, z


