import geopandas as gpd
import matplotlib.pyplot as plt
import folium

def load_data():
    # Memuat data dari file GeoJSON
    world = gpd.read_file('data/world.geojson')
    return world

def plot_world_map(world):
    # Membuat plot batas negara
    world.plot(figsize=(15, 10))
    plt.title('Peta Dunia')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

def top_population_countries(world):
    # Menghitung negara dengan populasi tertinggi
    top_countries = world.nlargest(10, 'pop_est')
    return top_countries

def plot_top_population_countries(world, top_countries):
    # Membuat plot untuk negara dengan populasi tertinggi
    fig, ax = plt.subplots(figsize=(10, 6))
    world.boundary.plot(ax=ax, linewidth=1)
    top_countries.plot(ax=ax, color='red')
    plt.title('Negara dengan Populasi Tertinggi')
    plt.show()

def create_interactive_map(world):
    # Membuat peta dasar
    m = folium.Map(location=[20, 0], zoom_start=2)
    folium.GeoJson(world).add_to(m)
    m.save('world_map.html')

if __name__ == "__main__":
    world = load_data()
    plot_world_map(world)
    top_countries = top_population_countries(world)
    plot_top_population_countries(world, top_countries)
    create_interactive_map(world)
