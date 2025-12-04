# StarCatalog 3D Visualizer 🔭  

Visualização 3D interativa de estrelas usando dados do catálogo Gaia DR3 + Python.  
Permite carregar um conjunto de estrelas, converter coordenadas celestes para coordenadas cartesianas e gerar um mapa 3D onde é possível clicar em uma estrela para exibir informações (RA, Dec, magnitude, etc.).  

## ✨ Funcionalidades  

- Consulta a catálogo Gaia via SQL/ADQL.  
- Conversão de coordenadas (RA, Dec, distância/paralaxe) para coordenadas cartesianas \(x, y, z\).  
- Plot 3D interativo com matplotlib — distribuição espacial de estrelas.  
- Seleção de estrelas com exibição de dados importantes (coordenadas, magnitude etc.).  
- Script principal para execução automatizada  

## 📦 Dependências  

- Python 3
- numpy  
- matplotlib  
- pandas  
- astropy  
- astroquery  

Você pode instalar todas de uma vez usando:

>> pip install -r requirements.txt
