import xml.etree.ElementTree as ET

# Lista de archivos XML
xml_files = ['TA03.xml']

# Lista para almacenar los datos procesados
data_list = []

for xml_file in xml_files:
    # Cargar y parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extraer datos (ajusta según tu estructura XML)
    for Marca_de_temps in root.findall('tu_elemento'):
        data = {
            'campo1': element.find('campo1').text,
            'campo2': element.find('campo2').text,
            # Agrega más campos según tu necesidad
        }
        data_list.append(data)

# Ahora `data_list` contiene todos los datos extraídos
print(data_list)

