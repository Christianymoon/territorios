# Proyecto de Territorios de Google Maps 

## Indice

- [Codigos QR](#codigos-qr)
- [Creacion de mapas](#creacion-de-mapas)

## Codigos QR 
> Utilizamos la librerias de Python: [Pandas](https://pandas.pydata.org/), [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/) y [qrcode 8.0](https://pypi.org/project/qrcode/) para hacer un mini script que extrae las url del archivo Excel "Territorios URL"
> Cada url es convertida mediante la biblioteca estandar Pillow

### Uso del script
El script hace el trabajo de los codigos qr por usted solo hay que ejecutarlo en la misma ruta donde se encuentra el archivo excel "Territorios URL.xslx"
**Nota: si el archivo Territorios URL no esta presente en el mismo directorio raiz del script no funcionara ya que el script esta limitado a leer el archivo en 
la ruta raiz**

<code>python qrcode.py</code>

## Creacion de Mapas 

>Utilizamos la herramienta de creacion de mapas Google My Maps que puede encontrar en el siguiente [Enlace](mymaps.google.com) para crear un mapa sera necesario
>una cuenta de Google y Google Drive para almacenar los mapas creados una vez hecho puede comenzar a crear mapas

### Exportacion para edicion de mapas 
Un archivo KML (Keyhole Markup Language) es un formato de archivo basado en XML diseñado para representar datos geográficos en mapas y aplicaciones de visualización, como Google Earth, Google Maps o sistemas de información geográfica (GIS).

Un archivo KML puede ser importado directamente a aplicaciones como Google Earth, Google Maps o en la misma herramienta de Google MyMaps para su edicion, importacion, exportacion si el usuario asi lo desee 

# **NOTAS**
- **Este proyecto puede estar publico hasta tiempo determinado**



