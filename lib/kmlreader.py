from pykml import parser
from pykml.factory import KML_ElementMaker as KML
from lxml import etree

import json

def read_kml_placemark(fileCoordinate: str, placemarkArea: str):
    print(fileCoordinate)
    # Load the KML file
    with open((fileCoordinate + ".kml"), "r") as f:
        doc = parser.parse(f)

    # Get the root element
    root = doc.getroot()

    # Define namespaces
    namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}
    # Find all Placemarks
    placemarks = root.findall('.//kml:Placemark', namespaces)

    coordinates = []
    # Iterate through placemarks
    for placemark in placemarks:
        # Check if the filename and the placemarks is the same
        if(placemark.name.text != placemarkArea):
            continue
        # Extract coordinates
        coordinates_node = placemark.LineString.coordinates
        coordinates = [coord.strip().split(',') for coord in coordinates_node.text.strip().split('\n')]

    return coordinates

def write_kml(JSONName, outputName, inputName):
    with open((JSONName + ".json"), "r") as f:
        data = json.load(f)

    # Create KML document
    kml_doc = KML.kml(
        KML.Document(
            KML.name(str(inputName) + ".kml"),
            KML.StyleMap(
                KML.id("inline"),
                KML.Pair(
                    KML.key("normal"),
                    KML.styleUrl("#inline1")
                ),
                KML.Pair(
                    KML.key("highlight"),
                    KML.styleUrl("#inline2")
                )
            ),
            KML.Style(
                KML.id("inline1"),
                KML.LineStyle(
                    KML.color("ff0000ff"),
                    KML.width("4")
                )
            ),
            KML.Style(
                KML.id("inline2"),
                KML.LineStyle(
                    KML.color("ff0000ff"),
                    KML.width("4")
                )
            )
        )
    )

    # Add placemarks
    folder = KML.Folder(KML.name(str(inputName)))

    for item in data:
        name = item["name"]
        coordinates = ''.join(item["coordinate"])

        placemark = KML.Placemark(
            KML.name(name),
            KML.Snippet(),
            KML.styleUrl("#inline"),
            KML.LineString(
                KML.tessellate("1"),
                KML.coordinates(coordinates)
            )
        )
        folder.append(placemark)

    kml_doc.Document.append(folder)

    # Write KML document to file
    with open(outputName + "." + "kml", "wb") as f:
        f.write(etree.tostring(kml_doc, pretty_print=True))

