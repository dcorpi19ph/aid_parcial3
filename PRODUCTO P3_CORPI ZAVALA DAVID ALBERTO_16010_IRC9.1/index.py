import os
import xml.etree.ElementTree as ET

def obtener_datos_factura(archivo_xml):
    try:
        # Parsear el archivo XML
        tree = ET.parse(archivo_xml)
        root = tree.getroot()

        # Obtener los datos relevantes de la factura
        rfc_emisor = root.find(".//{http://www.sat.gob.mx/cfd/3}Emisor").attrib["rfc"]
        rfc_receptor = root.find(".//{http://www.sat.gob.mx/cfd/3}Receptor").attrib["rfc"]
        total = float(root.find(".//{http://www.sat.gob.mx/cfd/3}Comprobante").attrib["total"])
        uuid_factura = root.find(".//{http://www.sat.gob.mx/cfd/3}Complemento").find(".//{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital").attrib["UUID"]

        return rfc_emisor, rfc_receptor, total, uuid_factura
    except Exception as e:
        print("Error al obtener datos de la factura:", e)
        return None, None, None, None

def validar_factura(rfc_emisor, rfc_receptor, total, uuid_factura):
    import requests  # Importa la librería aquí para mantener el código modularizado

    url = "https://api.sat.gob.mx/ConsultaCFDIServiceREST/consultar"

    # Datos de la factura a validar
    data = {
        "rfcEmisor": rfc_emisor,
        "rfcReceptor": rfc_receptor,
        "total": total,
        "uuid": uuid_factura
    }

    # Realizar la petición POST a la API del SAT
    response = requests.post(url, json=data)

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # La solicitud fue exitosa
        resultado = response.json()
        if resultado["estado"] == "Vigente":
            return True, "La factura es válida."
        else:
            return False, "La factura no es válida: {}".format(resultado["estado"])
    else:
        # La solicitud falló
        return False, "Error al conectarse con la API del SAT. Código de estado: {}".format(response.status_code)

# Obtener la ruta completa del archivo XML
archivo_xml = os.path.join(os.path.dirname(__file__), "factura1.xml")

# Ejemplo de uso
rfc_emisor, rfc_receptor, total, uuid_factura = obtener_datos_factura(archivo_xml)

if rfc_emisor and rfc_receptor and total and uuid_factura:
    valido, mensaje = validar_factura(rfc_emisor, rfc_receptor, total, uuid_factura)
    print(mensaje)
else:
    print("No se pudieron obtener los datos de la factura.")
