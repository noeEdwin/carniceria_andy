import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
ID_BUSINESS = "50442855"

url_negocio = f"https://api.hubapi.com/crm/v3/objects/deals/{ID_BUSINESS}?associations=line_items"

headers = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}"
}

respuesta = requests.get(url_negocio, headers=headers)

business_data = respuesta.json()

print("\n--- Respuesta Completa de HubSpot ---")
print(json.dumps(business_data, indent=2))

try:
    # Navegamos dentro del diccionario para encontrar lo que necesitamos.
    # La ruta es: 'associations' -> 'line items' -> 'results'
    line_items = business_data['associations']['line items']['results']

    print("\n--- ¡Éxito! 🎉 Se encontraron los siguientes Line Items asociados: ---")

    # Recorremos la lista de line items encontrados e imprimimos su ID.
    for item in line_items:
        print(f"ID del Line Item: {item['id']}")

except KeyError:
    print("\n--- 😟 No se encontraron 'line items' asociados a este negocio. ---")
    print("Asegúrate de haber agregado productos al negocio en HubSpot.")
