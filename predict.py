from detecto import core, utils, visualize


def detecto_m(pic): 
    image = utils.read_image(pic)
    model = core.Model()
    labels, boxes, scores = model.predict_top(image)
    result = visualize.show_labeled_image(image, boxes, labels)
    return result