import sys
import glob

def localize_objects(path):
    """Localize objects in the local image.

    Args:
        path: The path to the local file.
    Returns:
        obj_L:
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    objects = client.object_localization(image=image).localized_object_annotations

    """
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
    """

    obj_L = []
    for object_ in objects:
        obj_L.append(object_.name)
    return obj_L


def get_images(filepath):
    """get file path"""

    file_L = glob.glob(filepath)
    file_L.sort()

    return file_L

if __name__=="__main__":
    #image_name = sys.argv[1]
    file_L = get_images("./cloths/*")
    for f in file_L:
        localize_objects(f)
