from rich.console import Console
from rich.table import Table
from rich import box

# Lista de helipontos
helipontos_publicos_df = [
    {"Nome": "Residência Oficial de Águas Claras II", "Latitude": "15°49'39\"S", "Longitude": "048°01'23\"W"},
    {"Nome": "Base Resgate", "Latitude": "15°46'30\"S", "Longitude": "047°54'22\"W"},
    {"Nome": "Península", "Latitude": "15°49'49.5\"S", "Longitude": "047°52'00\"W"},
    {"Nome": "Hospital Anchieta", "Latitude": "15°49'26\"S", "Longitude": "048°04'02\"W"},
    {"Nome": "Toca PCDF", "Latitude": "15°46'47\"S", "Longitude": "047°54'47\"W"},
    {"Nome": "CADF", "Latitude": "15°50'10.3\"S", "Longitude": "048°05'02.3\"W"},
    {"Nome": "Condomínio Brasil 21", "Latitude": "15°47'34\"S", "Longitude": "047°53'38\"W"},
    {"Nome": "SENAI/SESI/CNI", "Latitude": "15°47'26\"S", "Longitude": "047°52'46\"W"},
    {"Nome": "Parque Cidade", "Latitude": "15°47'44\"S", "Longitude": "047°53'37\"W"},
    {"Nome": "Home", "Latitude": "15°50'07\"S", "Longitude": "047°54'36\"W"},
    {"Nome": "Heli Brasília", "Latitude": "15°50'18\"S", "Longitude": "047°44'46\"W"},
    {"Nome": "RAUL SABOIA", "Latitude": "15°51'14\"S", "Longitude": "047°51'43\"W"}
]

def listar_helipontos(helipontos):
    console = Console()
    table = Table(title="🚁 Helipontos Públicos Cadastrados na ANAC - DF", box=box.SIMPLE_HEAVY)

    table.add_column("Nº", justify="right", style="cyan", no_wrap=True)
    table.add_column("Nome", style="bold yellow")
    table.add_column("Latitude", style="green")
    table.add_column("Longitude", style="red")

    for i, h in enumerate(helipontos, start=1):
        table.add_row(str(i), h["Nome"], h["Latitude"], h["Longitude"])

    console.print(table)

# Executando a função
listar_helipontos(helipontos_publicos_df)
